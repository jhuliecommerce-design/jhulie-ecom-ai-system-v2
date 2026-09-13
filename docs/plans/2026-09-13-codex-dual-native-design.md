# JHULIE ECOM AI SYSTEM - compatibilidade dual Claude e Codex

## Objetivo

Adicionar suporte nativo ao Codex sem alterar nem remover a experiência existente do Claude Code.

## Decisão de arquitetura

A implementação será dual-native. Os arquivos em `.claude/` e `CLAUDE.md` continuarão sendo a fonte da experiência Claude. O Codex receberá estruturas próprias e versionadas no repositório:

- `AGENTS.md` para as regras persistentes do projeto;
- `.codex/agents/*.toml` para os especialistas;
- `.agents/skills/*/SKILL.md` para skills e atalhos operacionais;
- `README_CODEX.md` para instalação e uso no Codex.

Links simbólicos foram descartados porque tornam o clone menos portátil no Windows. Uma conversão exclusiva para Codex foi descartada porque quebraria a compatibilidade atual com Claude.

## Mapeamento

### Instruções do projeto

`CLAUDE.md` será traduzido para `AGENTS.md`, preservando integridade de dados, limites da Public Edition, roteamento, autorização para ações externas e distinção entre fato, hipótese, recomendação e execução confirmada.

### Especialistas

Cada arquivo em `.claude/agents/*.md` terá um equivalente em `.codex/agents/*.toml`. O frontmatter fornecerá `name` e `description`; o corpo será convertido em `developer_instructions`. Nenhum modelo será fixado, permitindo que o agente herde o modelo e o esforço de raciocínio da sessão principal.

Os nomes Codex usarão `snake_case`, enquanto a identidade visível `JHULIE // ...` permanecerá igual. A documentação mostrará a correspondência entre os nomes Claude e Codex.

### Skills reutilizáveis

As sete skills de `.claude/skills/` serão portadas para `.agents/skills/`. Cada `SKILL.md` terá frontmatter compatível com Codex, descrição precisa para descoberta implícita e o mesmo método operacional público.

### Comandos operacionais

Os doze arquivos em `.claude/commands/` serão convertidos em skills Codex com o mesmo nome. No Claude, o usuário continuará chamando `/diagnosticar-operacao`; no Codex, chamará `$diagnosticar-operacao`. A variável Claude `$ARGUMENTS` será substituída por instruções para usar o contexto e os anexos fornecidos pelo usuário.

Quando um especialista customizado estiver disponível, a skill poderá direcionar o trabalho a ele. Se a execução estiver em modo de agente único, o fluxo continuará utilizável diretamente pelas instruções da própria skill e pelas regras do `AGENTS.md`.

## Segurança e permissões

A camada Codex não adicionará integrações, credenciais ou capacidade externa. Ela manterá as regras existentes:

- não afirmar acesso a plataforma não conectada;
- não declarar ação executada sem confirmação de ferramenta;
- exigir autorização explícita para orçamento, publicação, comunicação externa, pagamento, exclusão ou produção;
- manter alterações locais pequenas, reversíveis e verificáveis;
- não expor conteúdo reservado às camadas privadas.

## Documentação

`README_CODEX.md` explicará requisitos, descoberta de skills, sintaxe `$skill`, especialistas customizados, exemplos e limites. O `README.md` receberá uma seção curta indicando o suporte dual e apontando para os guias de cada host.

## Validação

Uma suíte baseada apenas na biblioteca padrão do Python verificará:

- existência de `AGENTS.md` e do guia Codex;
- um TOML válido para cada agente Claude;
- presença de `name`, `description` e `developer_instructions` nos agentes Codex;
- uma skill Codex para cada skill e comando Claude;
- diretórios e nomes válidos;
- frontmatter obrigatório e descrições utilizáveis;
- ausência de `$ARGUMENTS` nos adaptadores Codex;
- permanência intacta da estrutura Claude rastreada no início da implementação.

O validador será executável diretamente e também por `unittest`.

## Critérios de aceite

1. O Claude continua encontrando todos os agentes, comandos e skills existentes.
2. O Codex encontra as skills em `.agents/skills` e os agentes em `.codex/agents`.
3. Todos os atalhos documentados possuem uma chamada equivalente no Codex.
4. As políticas públicas e de segurança permanecem equivalentes nos dois hosts.
5. A validação automatizada termina sem falhas.
