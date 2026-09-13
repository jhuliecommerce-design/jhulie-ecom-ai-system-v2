"""Compatibility contract for the dual-native Claude/Codex distribution."""

from __future__ import annotations

import json
import re
import subprocess
import tempfile
import tomllib
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CLAUDE_BASELINE_COMMIT = "26d10115ec838e4deaa5434e30a3689b3b7bb6f3"

EXPECTED_AGENT_FILE_TO_NAME = {
    "competitor-intelligence": "competitor_intelligence",
    "diretor-operacao": "diretor_operacao",
    "google-media-buyer": "google_media_buyer",
    "meta-media-buyer": "meta_media_buyer",
    "sac-operator": "sac_operator",
    "seo-commerce": "seo_commerce",
    "store-analyst": "store_analyst",
    "store-optimizer": "store_optimizer",
    "theme-engineer": "theme_engineer",
    "tracking-analyst": "tracking_analyst",
    "traffic-director": "traffic_director",
}

EXPECTED_AGENT_FILE_STEMS = tuple(EXPECTED_AGENT_FILE_TO_NAME)
EXPECTED_AGENT_NAMES = tuple(EXPECTED_AGENT_FILE_TO_NAME.values())

EXPECTED_AGENT_IDENTITY_MARKERS = {
    "competitor-intelligence": "# JHULIE // COMPETITOR INTELLIGENCE",
    "diretor-operacao": "# JHULIE // DIRECTOR",
    "google-media-buyer": "# JHULIE // GOOGLE BUYER",
    "meta-media-buyer": "# JHULIE // META BUYER",
    "sac-operator": "# JHULIE // SAC OPERATOR",
    "seo-commerce": "# JHULIE // SEO COMMERCE",
    "store-analyst": "# JHULIE // STORE ANALYST",
    "store-optimizer": "# JHULIE // STORE OPTIMIZER",
    "theme-engineer": "# JHULIE // THEME ENGINEER",
    "tracking-analyst": "# JHULIE // TRACKING ANALYST",
    "traffic-director": "# JHULIE // TRAFFIC DIRECTOR",
}

EXPECTED_AGENT_SAFETY_MARKERS = {
    "competitor-intelligence": (
        "Nunca diga que consultou uma fonte se não conseguiu acessá-la.",
        "não cópias",
    ),
    "diretor-operacao": (
        "Nunca invente dados ausentes.",
        "Não execute mudanças de alto impacto sem autorização explícita.",
    ),
    "google-media-buyer": (
        "Só execute com API/tool real e autorização explícita",
        "ROAS de plataforma não equivale a lucro.",
    ),
    "meta-media-buyer": (
        "Só execute quando API/tool real estiver disponível",
        "ROAS de plataforma não é lucro.",
    ),
    "sac-operator": (
        "Nunca invente status, prazo individual, reembolso ou ação executada.",
        "Minimize dados pessoais.",
    ),
    "seo-commerce": (
        "Não invente volume de busca, ranking ou dados de Search Console.",
        "Não prometa ganho de posição.",
    ),
    "store-analyst": (
        "Não diagnostique por uma única métrica.",
        "Nunca diga que leu Shopify, GA4 ou Ads sem integração",
    ),
    "store-optimizer": (
        "Não invente problemas visuais se não acessou página, screenshot ou arquivos.",
        "Não recomende redesign completo sem necessidade.",
    ),
    "theme-engineer": (
        "Nunca publique em produção sem autorização explícita.",
        "Nunca exponha tokens, secrets ou credenciais.",
    ),
    "tracking-analyst": (
        "Nunca declare tracking correto sem evidência.",
        "Não exponha tokens, IDs sensíveis ou dados pessoais.",
    ),
    "traffic-director": (
        "Não use ROAS isolado para alocação.",
        "Não execute budget sem integração real e autorização explícita.",
    ),
}

FORBIDDEN_AGENT_CONFIGURATION_KEYS = {
    "model",
    "model_reasoning_effort",
    "reasoning_effort",
    "sandbox",
    "sandbox_mode",
}

EXPECTED_REUSABLE_SKILL_NAMES = (
    "competitor-research",
    "cro-audit",
    "daily-ops-report",
    "media-buying",
    "pdp-optimization",
    "seo-product",
    "tracking-audit",
)

EXPECTED_COMMAND_SKILL_NAMES = (
    "analisar-concorrente",
    "auditar-loja",
    "auditar-seo",
    "decidir-verba",
    "diagnosticar-google",
    "diagnosticar-meta",
    "diagnosticar-operacao",
    "jhulie-daily",
    "otimizar-pdp",
    "otimizar-tema",
    "responder-sac",
    "revisar-tracking",
)

EXPECTED_SKILL_NAMES = (
    EXPECTED_REUSABLE_SKILL_NAMES + EXPECTED_COMMAND_SKILL_NAMES
)

EXPLICIT_AUTHORIZATION_ACTIONS = (
    "financeiras",
    "pausar ou ativar campanhas",
    "publicação",
    "mensagens externas",
    "pagamento",
    "reembolso",
    "exclusão",
    "destrutivas",
    "produção",
    "credenciais",
)
EXPLICIT_AUTHORIZATION_REQUIREMENT = "sempre exigem autorização explícita"

FRONTMATTER_KEY = re.compile(r"[A-Za-z][A-Za-z0-9_-]*\Z")
YAML_NON_STRING_SCALAR = re.compile(
    r"""
    (?:
        ~|null|true|false|yes|no|on|off|y|n
        |[-+]?\.(?:inf|nan)
        |[-+]?0b[01_]+
        |[-+]?0o[0-7_]+
        |[-+]?0x[0-9a-f_]+
        |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+(?:\.[0-9_]*)?
        |[-+]?(?:
            (?:[0-9][0-9_]*)?\.[0-9_]+(?:e[-+]?[0-9]+)?
            |[0-9][0-9_]*\.(?:e[-+]?[0-9]+)?
            |[0-9][0-9_]*(?:\.[0-9_]*)?e[-+]?[0-9]+
            |[0-9][0-9_]*
        )
    )\Z
    """,
    re.IGNORECASE | re.VERBOSE,
)
YAML_TIMESTAMP_SCALAR = re.compile(
    r"""
    [0-9]{4}-[0-9]{1,2}-[0-9]{1,2}
    (?:
        [Tt\x20\t]+[0-9]{1,2}:[0-9]{2}:[0-9]{2}
        (?:\.[0-9]+)?
        (?:[\x20\t]*(?:Z|[-+][0-9]{1,2}(?::?[0-9]{2})?))?
    )?
    \Z
    """,
    re.VERBOSE,
)


def parse_frontmatter_scalar(value: str) -> str:
    """Parse the strict string-scalar subset accepted by this contract."""
    value = value.strip()
    if not value:
        raise ValueError("frontmatter values cannot be empty")

    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid double-quoted scalar: {value!r}") from error
        if not isinstance(parsed, str):
            raise ValueError(f"frontmatter scalar must be a string: {value!r}")
        return parsed

    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise ValueError(f"unterminated single-quoted scalar: {value!r}")
        inner = value[1:-1]
        if re.fullmatch(r"(?:[^']|'')*", inner) is None:
            raise ValueError(f"invalid single-quoted scalar: {value!r}")
        return inner.replace("''", "'")

    if value.endswith(("'", '"')):
        raise ValueError(f"unmatched quote in scalar: {value!r}")
    if value.endswith(":"):
        raise ValueError(f"unsupported terminal mapping indicator: {value!r}")
    if value[0] in "-?:,[]{}#&*!|>'\"%@`":
        raise ValueError(f"unsupported YAML scalar indicator: {value!r}")
    if ": " in value or ":\t" in value or " #" in value or "\t" in value:
        raise ValueError(f"ambiguous plain YAML scalar: {value!r}")
    if YAML_NON_STRING_SCALAR.fullmatch(value) or YAML_TIMESTAMP_SCALAR.fullmatch(
        value
    ):
        raise ValueError(f"frontmatter scalar must be a string: {value!r}")
    return value


def read_frontmatter(path: Path) -> dict[str, str]:
    """Read the scalar YAML frontmatter fields used by Codex skills."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("frontmatter must start with '---'")

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return fields
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0].isspace():
            raise ValueError(f"frontmatter keys must start at column zero: {line!r}")
        key, separator, value = line.partition(":")
        key = key.strip()
        if (
            not separator
            or FRONTMATTER_KEY.fullmatch(key) is None
            or not value.strip()
        ):
            raise ValueError(f"invalid scalar frontmatter line: {line!r}")
        if key in fields:
            raise ValueError(f"duplicate frontmatter key: {key!r}")
        fields[key] = parse_frontmatter_scalar(value)

    raise ValueError("frontmatter must end with '---'")


def read_markdown_body_after_frontmatter(path: Path) -> str:
    """Return the complete Markdown body after a valid frontmatter block."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("frontmatter must start with '---'")
    try:
        closing_delimiter = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("frontmatter must end with '---'") from error
    return "\n".join(lines[closing_delimiter + 1 :]).strip()


def expected_codex_agent_body(claude_body: str) -> str:
    """Adapt only custom-agent identifiers from Claude to Codex syntax."""
    adapted_body = claude_body
    for file_stem, agent_name in EXPECTED_AGENT_FILE_TO_NAME.items():
        adapted_body = adapted_body.replace(file_stem, agent_name)
    return adapted_body


def read_markdown_section(document: str, heading: str, level: int) -> str | None:
    """Return a Markdown section body up to the next peer or parent heading."""
    marker = "#" * level
    match = re.search(
        rf"(?ms)^{re.escape(marker)}\s+{re.escape(heading)}\s*$\n"
        rf"(?P<body>.*?)(?=^#{{1,{level}}}\s+|\Z)",
        document,
    )
    return match.group("body").strip() if match else None


def find_affirmative_external_authorization_sentence(
    document: str,
) -> str | None:
    """Find an affirmative authorization rule in the external-action section."""
    section = read_markdown_section(document, "Ação externa", level=3)
    if section is None:
        return None

    for sentence in re.split(r"(?<=[.!?])\s+", section):
        normalized_sentence = " ".join(sentence.casefold().split())
        requirement_start = normalized_sentence.find(
            EXPLICIT_AUTHORIZATION_REQUIREMENT
        )
        if requirement_start < 0:
            continue
        subject = normalized_sentence[:requirement_start]
        if re.search(r"\b(?:não|nunca|nem)\b", subject):
            continue
        if all(action in subject for action in EXPLICIT_AUTHORIZATION_ACTIONS):
            return sentence.strip()
    return None


class FrontmatterParserTests(unittest.TestCase):
    def test_rejects_frontmatter_outside_supported_scalar_yaml_subset(self) -> None:
        invalid_documents = {
            "unterminated quote": "---\nname: 'broken\ndescription: valid\n---\n",
            "duplicate key": "---\nname: first\nname: second\ndescription: valid\n---\n",
            "flow collection": "---\nname: valid\ndescription: [broken\n---\n",
            "flow mapping": "---\nname: valid\ndescription: {broken\n---\n",
            "block scalar": "---\nname: valid\ndescription: >\n  broken\n---\n",
            "literal block scalar": "---\nname: valid\ndescription: |\n  broken\n---\n",
            "indented key": "---\nname: valid\n  description: broken\n---\n",
            "terminal mapping indicator": (
                "---\nname: valid\ndescription: broken:\n---\n"
            ),
            "indented opening delimiter": (
                " ---\nname: valid\ndescription: broken\n---\n"
            ),
            "indented closing delimiter": (
                "---\nname: valid\ndescription: broken\n ---\n"
            ),
            "implicit infinity": "---\nname: valid\ndescription: .inf\n---\n",
            "implicit not-a-number": "---\nname: valid\ndescription: .NaN\n---\n",
            "implicit boolean": "---\nname: valid\ndescription: true\n---\n",
            "implicit null": "---\nname: valid\ndescription: null\n---\n",
            "implicit integer": "---\nname: valid\ndescription: 42\n---\n",
            "implicit float": "---\nname: valid\ndescription: 4.2\n---\n",
            "implicit hexadecimal": "---\nname: valid\ndescription: 0x2A\n---\n",
            "implicit octal": "---\nname: valid\ndescription: 0o52\n---\n",
            "implicit binary": "---\nname: valid\ndescription: 0b101010\n---\n",
            "implicit date": "---\nname: valid\ndescription: 2026-09-13\n---\n",
            "implicit timestamp": (
                "---\nname: valid\ndescription: 2026-09-13T10:30:00Z\n---\n"
            ),
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "SKILL.md"
            for scenario, document in invalid_documents.items():
                with self.subTest(scenario=scenario):
                    path.write_text(document, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        read_frontmatter(path)

    def test_parses_plain_and_quoted_scalar_fields(self) -> None:
        document = (
            "---\n"
            "name: competitor-research\n"
            'description: "Analyze competitors: positioning and offers."\n'
            "audience: 'operator''s team'\n"
            'quoted-infinity: ".inf"\n'
            "quoted-hexadecimal: '0x2A'\n"
            'quoted-timestamp: "2026-09-13T10:30:00Z"\n'
            'quoted-collection: "[safe]"\n'
            "quoted-block-indicator: '>'\n"
            "---\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "SKILL.md"
            path.write_text(document, encoding="utf-8")
            self.assertEqual(
                read_frontmatter(path),
                {
                    "name": "competitor-research",
                    "description": "Analyze competitors: positioning and offers.",
                    "audience": "operator's team",
                    "quoted-infinity": ".inf",
                    "quoted-hexadecimal": "0x2A",
                    "quoted-timestamp": "2026-09-13T10:30:00Z",
                    "quoted-collection": "[safe]",
                    "quoted-block-indicator": ">",
                },
            )


class InstructionContractAssertionTests(unittest.TestCase):
    def test_external_authorization_rejects_negated_requirement(self) -> None:
        negated_contract = """\
### Ação externa

Mudanças financeiras, pausar ou ativar campanhas, publicação, envio de
mensagens externas, emissão de pagamento ou reembolso, exclusão de dados,
mudanças destrutivas, mudanças em produção e alterações de credenciais nem
sempre exigem autorização explícita do usuário.
"""

        self.assertIsNone(
            find_affirmative_external_authorization_sentence(negated_contract)
        )

    def test_external_authorization_ignores_rule_outside_section(self) -> None:
        misplaced_contract = """\
### Ação externa

Consulte as regras gerais abaixo.

## Segurança

Mudanças financeiras, pausar ou ativar campanhas, publicação, envio de
mensagens externas, emissão de pagamento ou reembolso, exclusão de dados,
mudanças destrutivas, mudanças em produção e alterações de credenciais sempre
exigem autorização explícita do usuário.
"""

        self.assertIsNone(
            find_affirmative_external_authorization_sentence(misplaced_contract)
        )


class CodexCompatibilityContractTests(unittest.TestCase):
    def test_contract_has_expected_number_of_adapters(self) -> None:
        approved_names = (
            "competitor_intelligence",
            "diretor_operacao",
            "google_media_buyer",
            "meta_media_buyer",
            "sac_operator",
            "seo_commerce",
            "store_analyst",
            "store_optimizer",
            "theme_engineer",
            "tracking_analyst",
            "traffic_director",
        )
        self.assertEqual(EXPECTED_AGENT_NAMES, approved_names)

        for file_stem, agent_name in EXPECTED_AGENT_FILE_TO_NAME.items():
            with self.subTest(file_stem=file_stem, agent_name=agent_name):
                self.assertRegex(file_stem, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                self.assertRegex(agent_name, r"^[a-z][a-z0-9_]*$")
                self.assertEqual(agent_name, file_stem.replace("-", "_"))

        self.assertEqual(len(EXPECTED_AGENT_FILE_STEMS), 11)
        self.assertEqual(len(EXPECTED_AGENT_NAMES), 11)
        self.assertEqual(len(set(EXPECTED_AGENT_FILE_STEMS)), 11)
        self.assertEqual(len(set(EXPECTED_AGENT_NAMES)), 11)
        self.assertEqual(len(EXPECTED_REUSABLE_SKILL_NAMES), 7)
        self.assertEqual(len(EXPECTED_COMMAND_SKILL_NAMES), 12)
        self.assertEqual(len(set(EXPECTED_SKILL_NAMES)), 19)

        agent_root = REPO_ROOT / ".codex" / "agents"
        if agent_root.is_dir():
            self.assertSetEqual(
                {path.name for path in agent_root.iterdir()},
                {f"{file_stem}.toml" for file_stem in EXPECTED_AGENT_FILE_STEMS},
                "Codex agent directory does not match the compatibility inventory",
            )

        skill_root = REPO_ROOT / ".agents" / "skills"
        if skill_root.is_dir():
            self.assertSetEqual(
                {path.name for path in skill_root.iterdir()},
                set(EXPECTED_SKILL_NAMES),
                "Codex skill directory does not match the compatibility inventory",
            )

    def test_codex_entrypoint_documents_exist(self) -> None:
        for relative_path in ("AGENTS.md", "README_CODEX.md"):
            with self.subTest(path=relative_path):
                self.assertTrue(
                    (REPO_ROOT / relative_path).is_file(),
                    f"missing Codex entrypoint document: {relative_path}",
                )

    def test_agents_md_defines_public_edition_operating_contract(self) -> None:
        path = REPO_ROOT / "AGENTS.md"
        self.assertTrue(path.is_file(), "missing Codex project instructions: AGENTS.md")

        instructions = path.read_text(encoding="utf-8")
        normalized = instructions.casefold()

        for required_text in (
            "JHULIE ECOM AI SYSTEM",
            "PUBLIC EDITION",
            "FATO",
            "HIPÓTESE",
            "RECOMENDAÇÃO",
            "EXECUTADO",
            "Consultivo",
            "Implementação local",
            "Ação externa",
        ):
            with self.subTest(required_text=required_text):
                self.assertIn(required_text.casefold(), normalized)

        hierarchy_section = read_markdown_section(
            instructions, "Hierarquia operacional", level=2
        )
        self.assertIsNotNone(hierarchy_section)
        hierarchy_normalized = hierarchy_section.casefold()
        hierarchy_terms = (
            "dados",
            "diagnóstico",
            "prioridade",
            "especialista",
            "execução assistida",
            "validação",
        )
        hierarchy_positions = [
            hierarchy_normalized.find(term) for term in hierarchy_terms
        ]
        self.assertTrue(
            all(position >= 0 for position in hierarchy_positions),
            "the operational hierarchy must contain every required stage",
        )
        self.assertEqual(
            hierarchy_positions,
            sorted(hierarchy_positions),
            "the operational hierarchy stages must appear in decision order",
        )

        for agent_name in EXPECTED_AGENT_NAMES:
            with self.subTest(agent_name=agent_name):
                self.assertIn(f"`{agent_name}`", instructions)

        for decision_input in ("screenshots", "CSVs", "métricas", "contexto"):
            with self.subTest(decision_input=decision_input):
                self.assertIn(decision_input.casefold(), normalized)
        self.assertRegex(normalized, r"1\s*[–-]\s*3")
        self.assertRegex(normalized, r"(?:mudem?|alterem?)\s+(?:a\s+)?decis")

        authorization_sentence = (
            find_affirmative_external_authorization_sentence(instructions)
        )
        self.assertIsNotNone(
            authorization_sentence,
            "the 'Ação externa' section must require explicit authorization",
        )
        authorization_sentence_normalized = authorization_sentence.casefold()
        for explicit_authorization_action in EXPLICIT_AUTHORIZATION_ACTIONS:
            with self.subTest(action=explicit_authorization_action):
                self.assertIn(
                    explicit_authorization_action,
                    authorization_sentence_normalized,
                )
        self.assertIn(
            EXPLICIT_AUTHORIZATION_REQUIREMENT,
            authorization_sentence_normalized,
        )

        self.assertIn("sem ferramenta real", normalized)
        self.assertIn("nunca grave secrets", normalized)
        self.assertIn("minimize dados pessoais", normalized)
        for policy_path in (
            "core/policies/data-integrity.md",
            "core/policies/execution-safety.md",
        ):
            with self.subTest(policy_path=policy_path):
                self.assertIn(f"]({policy_path})", instructions)
                self.assertTrue(
                    (path.parent / policy_path).is_file(),
                    f"AGENTS.md links to missing policy: {policy_path}",
                )
        self.assertIn("não diagnostique por uma métrica isolada", normalized)
        self.assertIn("benchmark genérico", normalized)
        self.assertIn("nível de confiança", normalized)
        self.assertIn("funcional e discreta", normalized)

    def test_custom_agents_match_expected_file_name_and_identity_mapping(self) -> None:
        for file_stem, agent_name in EXPECTED_AGENT_FILE_TO_NAME.items():
            relative_path = Path(".codex") / "agents" / f"{file_stem}.toml"
            path = REPO_ROOT / relative_path
            source_path = REPO_ROOT / ".claude" / "agents" / f"{file_stem}.md"
            with self.subTest(file_stem=file_stem, agent_name=agent_name):
                self.assertTrue(path.is_file(), f"missing Codex agent: {relative_path}")
                try:
                    document = tomllib.loads(path.read_text(encoding="utf-8"))
                except tomllib.TOMLDecodeError as error:
                    self.fail(f"invalid TOML in {relative_path}: {error}")

                for required_field in (
                    "name",
                    "description",
                    "developer_instructions",
                ):
                    self.assertIsInstance(
                        document.get(required_field),
                        str,
                        f"{relative_path} requires string field {required_field!r}",
                    )
                    self.assertTrue(
                        document[required_field].strip(),
                        f"{relative_path} has empty field {required_field!r}",
                    )
                self.assertEqual(document["name"], agent_name)
                self.assertEqual(
                    document["description"],
                    read_frontmatter(source_path)["description"],
                    f"{relative_path} must preserve the Claude role description",
                )

    def test_custom_agents_preserve_complete_public_role_instructions(self) -> None:
        for file_stem in EXPECTED_AGENT_FILE_STEMS:
            relative_path = Path(".codex") / "agents" / f"{file_stem}.toml"
            path = REPO_ROOT / relative_path
            source_path = REPO_ROOT / ".claude" / "agents" / f"{file_stem}.md"
            with self.subTest(file_stem=file_stem):
                self.assertTrue(path.is_file(), f"missing Codex agent: {relative_path}")
                document = tomllib.loads(
                    path.read_text(encoding="utf-8")
                )
                expected_body = expected_codex_agent_body(
                    read_markdown_body_after_frontmatter(source_path)
                )
                self.assertEqual(
                    document["developer_instructions"].strip(),
                    expected_body,
                    f"{relative_path} does not preserve the complete public role body",
                )

    def test_custom_agents_preserve_identity_and_critical_safety_rules(self) -> None:
        for file_stem in EXPECTED_AGENT_FILE_STEMS:
            relative_path = Path(".codex") / "agents" / f"{file_stem}.toml"
            path = REPO_ROOT / relative_path
            with self.subTest(file_stem=file_stem):
                self.assertTrue(path.is_file(), f"missing Codex agent: {relative_path}")
                document = tomllib.loads(
                    path.read_text(encoding="utf-8")
                )
                instructions = document["developer_instructions"]
                self.assertIn(
                    EXPECTED_AGENT_IDENTITY_MARKERS[file_stem], instructions
                )
                self.assertIn(
                    "JHULIE ECOM AI SYSTEM — PUBLIC EDITION", instructions
                )
                self.assertIn("## Missão", instructions)
                self.assertIn("## Saída padrão", instructions)
                for safety_marker in EXPECTED_AGENT_SAFETY_MARKERS[file_stem]:
                    self.assertIn(safety_marker, instructions)

    def test_custom_agents_inherit_parent_runtime_configuration(self) -> None:
        for file_stem in EXPECTED_AGENT_FILE_STEMS:
            relative_path = Path(".codex") / "agents" / f"{file_stem}.toml"
            path = REPO_ROOT / relative_path
            with self.subTest(file_stem=file_stem):
                self.assertTrue(path.is_file(), f"missing Codex agent: {relative_path}")
                document = tomllib.loads(
                    path.read_text(encoding="utf-8")
                )
                configured_keys = {key.casefold() for key in document}
                self.assertTrue(
                    FORBIDDEN_AGENT_CONFIGURATION_KEYS.isdisjoint(configured_keys),
                    f"{relative_path} must inherit model, reasoning, and sandbox settings",
                )

    def test_expected_codex_skills_have_valid_frontmatter(self) -> None:
        for skill_name in EXPECTED_SKILL_NAMES:
            relative_path = Path(".agents") / "skills" / skill_name / "SKILL.md"
            path = REPO_ROOT / relative_path
            with self.subTest(skill=skill_name):
                self.assertTrue(path.is_file(), f"missing Codex skill: {relative_path}")
                try:
                    frontmatter = read_frontmatter(path)
                except ValueError as error:
                    self.fail(f"invalid frontmatter in {relative_path}: {error}")

                self.assertEqual(frontmatter.get("name"), skill_name)
                self.assertTrue(
                    frontmatter.get("description", "").strip(),
                    f"{relative_path} requires a non-empty description",
                )

    def test_codex_adapters_do_not_contain_claude_arguments_placeholder(self) -> None:
        adapter_paths: list[Path] = []
        for adapter_root in (REPO_ROOT / ".agents", REPO_ROOT / ".codex"):
            if not adapter_root.exists():
                continue
            adapter_paths.extend(path for path in adapter_root.rglob("*") if path.is_file())
        agents_md = REPO_ROOT / "AGENTS.md"
        if agents_md.is_file():
            adapter_paths.append(agents_md)

        for path in adapter_paths:
            with self.subTest(path=path.relative_to(REPO_ROOT)):
                self.assertNotIn(
                    b"$ARGUMENTS",
                    path.read_bytes(),
                    f"Claude placeholder remains in {path.relative_to(REPO_ROOT)}",
                )

    def test_claude_surface_matches_pinned_baseline(self) -> None:
        self.assertTrue((REPO_ROOT / "CLAUDE.md").is_file())
        self.assertTrue((REPO_ROOT / ".claude").is_dir())

        baseline = subprocess.run(
            ["git", "cat-file", "-e", f"{CLAUDE_BASELINE_COMMIT}^{{commit}}"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            baseline.returncode,
            0,
            "Pinned Claude baseline commit is unavailable: "
            f"{CLAUDE_BASELINE_COMMIT}\n{baseline.stderr}",
        )

        baseline_tree = subprocess.run(
            [
                "git",
                "ls-tree",
                "-r",
                "--name-only",
                CLAUDE_BASELINE_COMMIT,
                "--",
                ".claude",
                "CLAUDE.md",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            baseline_tree.returncode,
            0,
            f"Could not read pinned Claude baseline inventory: {baseline_tree.stderr}",
        )

        expected_inventory = {
            line for line in baseline_tree.stdout.splitlines() if line
        }
        for relative_path in tuple(expected_inventory):
            parts = relative_path.split("/")
            expected_inventory.update(
                "/".join(parts[:depth]) for depth in range(1, len(parts))
            )

        actual_inventory = {"CLAUDE.md", ".claude"}
        actual_inventory.update(
            path.relative_to(REPO_ROOT).as_posix()
            for path in (REPO_ROOT / ".claude").rglob("*")
        )
        self.assertSetEqual(
            actual_inventory,
            expected_inventory,
            "Claude filesystem inventory differs from the pinned baseline",
        )

        diff = subprocess.run(
            [
                "git",
                "diff",
                "--exit-code",
                "--name-status",
                CLAUDE_BASELINE_COMMIT,
                "--",
                ".claude",
                "CLAUDE.md",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            diff.returncode,
            0,
            "Claude content differs from the pinned baseline:\n"
            f"{diff.stdout}{diff.stderr}",
        )


if __name__ == "__main__":
    unittest.main()
