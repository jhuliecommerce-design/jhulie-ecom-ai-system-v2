# Codex Dual-Native Compatibility Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a complete Codex-native interface to JHULIE ECOM AI SYSTEM while preserving the existing Claude Code interface.

**Architecture:** Keep `.claude/` and `CLAUDE.md` unchanged. Add project instructions in `AGENTS.md`, custom specialists in `.codex/agents`, and reusable plus command-style skills in `.agents/skills`; validate both host surfaces with a standard-library Python test suite.

**Tech Stack:** Markdown, YAML frontmatter, TOML, Python 3 standard library, `unittest`, Git.

---

### Task 1: Define the compatibility contract

**Files:**
- Create: `tests/test_codex_compat.py`

**Step 1: Write the failing structural tests**

Define the expected 11 agent names, 7 reusable skill names, and 12 command skill names. Test that every Codex artifact exists, parses, and exposes the required metadata. Snapshot the existing `.claude` tracked paths so the test also protects the original interface.

**Step 2: Run the tests to verify they fail**

Run: `python -m unittest tests.test_codex_compat -v`

Expected: FAIL because `AGENTS.md`, `.codex/agents`, `.agents/skills`, and `README_CODEX.md` do not exist.

**Step 3: Add a reusable validator entry point**

Create `scripts/validate_codex_compat.py` as a thin standard-library wrapper that runs the compatibility suite and returns a non-zero exit code on failure.

**Step 4: Run the validator to verify the same failure**

Run: `python scripts/validate_codex_compat.py`

Expected: FAIL with missing Codex artifacts.

**Step 5: Commit**

```bash
git add tests/test_codex_compat.py scripts/validate_codex_compat.py
git commit -m "test: define Codex compatibility contract"
```

### Task 2: Add Codex project instructions

**Files:**
- Create: `AGENTS.md`
- Test: `tests/test_codex_compat.py`

**Step 1: Confirm the relevant contract test is red**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_agents_md_defines_public_edition_operating_contract -v`

Expected: FAIL because `AGENTS.md` is absent.

**Step 2: Create `AGENTS.md`**

Translate the durable rules from `CLAUDE.md`: evidence taxonomy, routing, execution modes, Public Edition boundaries, data integrity, authorization, secrets, and output quality. Use Codex specialist identifiers in `snake_case` and point to the canonical policies in `core/policies/`.

**Step 3: Verify the test passes**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_agents_md_defines_public_edition_operating_contract -v`

Expected: PASS for `AGENTS.md`; the full suite remains red for later artifacts.

**Step 4: Commit**

```bash
git add AGENTS.md
git commit -m "feat: add Codex project instructions"
```

### Task 3: Port the specialists to Codex custom agents

**Files:**
- Create: `.codex/agents/*.toml` (11 files)
- Test: `tests/test_codex_compat.py`

**Step 1: Confirm custom-agent tests are red**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_custom_agents_match_expected_file_name_and_identity_mapping -v`

Expected: FAIL because the TOML files are absent.

**Step 2: Create each agent TOML**

For each `.claude/agents/*.md`, create a matching TOML with:

- a `snake_case` `name`;
- the original role description;
- the complete role body in `developer_instructions`;
- no hardcoded model or reasoning effort.

**Step 3: Validate TOML and one-to-one mapping**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_custom_agents_match_expected_file_name_and_identity_mapping -v`

Expected: PASS with 11 valid custom agents.

**Step 4: Commit**

```bash
git add .codex/agents tests/test_codex_compat.py
git commit -m "feat: add Codex ecommerce specialists"
```

### Task 4: Port reusable domain skills

**Files:**
- Create: `.agents/skills/competitor-research/SKILL.md`
- Create: `.agents/skills/cro-audit/SKILL.md`
- Create: `.agents/skills/daily-ops-report/SKILL.md`
- Create: `.agents/skills/media-buying/SKILL.md`
- Create: `.agents/skills/pdp-optimization/SKILL.md`
- Create: `.agents/skills/seo-product/SKILL.md`
- Create: `.agents/skills/tracking-audit/SKILL.md`
- Test: `tests/test_codex_compat.py`

**Step 1: Confirm reusable-skill tests are red**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_reusable_skills_map_one_to_one_from_claude_sources -v`

Expected: FAIL because the Codex skill directories are absent.

**Step 2: Create and validate skills one at a time**

For each reusable skill, preserve the public method, change the description into a precise `Use when...` trigger, and run the single-skill validation before moving to the next directory.

**Step 3: Verify the complete reusable-skill set**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_reusable_skills_map_one_to_one_from_claude_sources -v`

Expected: PASS with all seven skills discoverable.

**Step 4: Commit**

```bash
git add .agents/skills tests/test_codex_compat.py
git commit -m "feat: port JHULIE domain skills to Codex"
```

### Task 5: Convert Claude commands into Codex skills

**Files:**
- Create: `.agents/skills/analisar-concorrente/SKILL.md`
- Create: `.agents/skills/auditar-loja/SKILL.md`
- Create: `.agents/skills/auditar-seo/SKILL.md`
- Create: `.agents/skills/decidir-verba/SKILL.md`
- Create: `.agents/skills/diagnosticar-google/SKILL.md`
- Create: `.agents/skills/diagnosticar-meta/SKILL.md`
- Create: `.agents/skills/diagnosticar-operacao/SKILL.md`
- Create: `.agents/skills/jhulie-daily/SKILL.md`
- Create: `.agents/skills/otimizar-pdp/SKILL.md`
- Create: `.agents/skills/otimizar-tema/SKILL.md`
- Create: `.agents/skills/responder-sac/SKILL.md`
- Create: `.agents/skills/revisar-tracking/SKILL.md`
- Test: `tests/test_codex_compat.py`

**Step 1: Confirm command-skill tests are red**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_command_skills_map_one_to_one_from_claude_commands -v`

Expected: FAIL because the command adapters are absent.

**Step 2: Create and validate command skills one at a time**

Preserve the requested output and safety rules, replace `$ARGUMENTS` with the user's current prompt and attachments, and route to the mapped custom agent when delegation is appropriate. Keep each skill usable in a single-agent session.

**Step 3: Verify the complete command-skill set**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_command_skills_map_one_to_one_from_claude_commands -v`

Expected: PASS with twelve `$command-name` workflows and no Claude-only placeholders.

**Step 4: Commit**

```bash
git add .agents/skills tests/test_codex_compat.py
git commit -m "feat: add Codex command workflows"
```

### Task 6: Document dual-host usage

**Files:**
- Create: `README_CODEX.md`
- Modify: `README.md`
- Modify: `README_USO.md`
- Test: `tests/test_codex_compat.py`

**Step 1: Confirm documentation tests are red**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_codex_guide_documents_installation_discovery_and_limits -v`

Expected: FAIL because the Codex guide and usage markers are absent.

**Step 2: Add Codex documentation**

Document how to open the repository in Codex, list skills with `/skills`, invoke workflows with `$name`, request specialists, run the demo, and understand access limitations. Update the shared README files without removing Claude instructions.

**Step 3: Verify documentation**

Run: `python -m unittest tests.test_codex_compat.CodexCompatibilityContractTests.test_codex_guide_documents_installation_discovery_and_limits -v`

Expected: PASS.

**Step 4: Commit**

```bash
git add README.md README_USO.md README_CODEX.md
git commit -m "docs: add Codex usage guide"
```

### Task 7: Final verification and parity audit

**Files:**
- Modify if needed: `tests/test_codex_compat.py`
- Modify if needed: `scripts/validate_codex_compat.py`

**Step 1: Run the complete validator**

Run: `python scripts/validate_codex_compat.py`

Expected: all tests PASS with no warnings.

**Step 2: Verify the original Claude surface**

Run: `git diff origin/main -- .claude CLAUDE.md`

Expected: no output.

**Step 3: Inspect repository status and diff**

Run: `git status --short && git diff --check origin/main...HEAD`

Expected: clean worktree and no whitespace errors.

**Step 4: Review discoverability manually**

Confirm each `.agents/skills/*/SKILL.md` has a unique name and discriminating description, and every `.codex/agents/*.toml` has the required fields.

**Step 5: Commit any final corrections**

```bash
git add tests/test_codex_compat.py scripts/validate_codex_compat.py
git commit -m "test: finalize Codex compatibility validation"
```
