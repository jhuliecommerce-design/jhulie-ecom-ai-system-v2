# Guia rápido de uso — Jhulie Ecom AI System V2

## 1. Pré-requisitos

Tenha Git e pelo menos um dos hosts instalados e autenticados: Claude Code ou Codex.

## 2. Baixe o projeto
No terminal:

```bash
git clone https://github.com/jhuliecommerce-design/jhulie-ecom-ai-system-v2.git
cd jhulie-ecom-ai-system-v2
```

## 3. Escolha o host

### Claude Code

Ainda dentro da pasta, execute:

```bash
claude
```

Confira os agentes:

```text
/agents
```

Você deve encontrar os especialistas do projeto.

### Codex

Inicie o Codex dentro da pasta do projeto:

```bash
codex
```

Confira as skills com:

```text
/skills
```

No Codex, as instruções ficam em `AGENTS.md`, os especialistas em `.codex/agents/` e as skills em `.agents/skills/`. Veja o guia completo em [`README_CODEX.md`](README_CODEX.md).

## 4. Use comandos rápidos no Claude Code

Exemplos:

```text
/diagnosticar-operacao
/diagnosticar-meta
/diagnosticar-google
/auditar-loja
/otimizar-pdp
/otimizar-tema
/revisar-tracking
/auditar-seo
/analisar-concorrente
/responder-sac
/decidir-verba
```

## 5. Use os fluxos equivalentes no Codex

No Codex, troque `/` por `$`. Exemplos:

```text
$diagnosticar-operacao
$diagnosticar-meta
$diagnosticar-google
$auditar-loja
$otimizar-pdp
$otimizar-tema
$revisar-tracking
$auditar-seo
$analisar-concorrente
$responder-sac
$decidir-verba
```

## 6. Use skills reutilizáveis

No Claude Code, as skills ficam em `.claude/skills/`. No Codex, ficam em `.agents/skills/`, podem ser descobertas automaticamente e são chamadas explicitamente com `$`.

Exemplos:

```text
/cro-audit
/pdp-optimization
/media-buying
/tracking-audit
/seo-product
/competitor-research
/daily-ops-report
```

Exemplo equivalente no Codex:

```text
$cro-audit
$pdp-optimization
$media-buying
$tracking-audit
$seo-product
$competitor-research
$daily-ops-report
```

## 7. Regra mais importante
Sem integração ou dado fornecido, o agente não possui acesso mágico à Shopify, Meta, Google ou GA4.

Quando APIs/MCP/backend forem conectados, os mesmos agentes podem trabalhar com dados reais dentro das permissões configuradas.

## Atualizando
Se você já clonou o projeto:

```bash
git pull
```

Execute Claude Code ou Codex sempre dentro da pasta do projeto para carregar as instruções, skills e especialistas corretos.
