# Guia rápido de uso — Jhulie Ecom AI System V2

## 1. Pré-requisitos
Tenha Git e Claude Code instalados e autenticados.

## 2. Baixe o projeto
No terminal:

```bash
git clone https://github.com/jhuliecommerce-design/jhulie-ecom-ai-system-v2.git
cd jhulie-ecom-ai-system-v2
```

## 3. Abra o Claude Code
Ainda dentro da pasta:

```bash
claude
```

## 4. Confira os agentes
Dentro do Claude Code:

```text
/agents
```

Você deve encontrar os especialistas do projeto.

## 5. Use comandos rápidos
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

## 6. Use skills
Skills ficam em `.claude/skills/` e podem ser carregadas automaticamente ou chamadas pelo nome.

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

## 7. Regra mais importante
Sem integração ou dado fornecido, o agente não possui acesso mágico à Shopify, Meta, Google ou GA4.

Quando APIs/MCP/backend forem conectados, os mesmos agentes podem trabalhar com dados reais dentro das permissões configuradas.

## Atualizando
Se você já clonou o projeto:

```bash
git pull
```

Execute o Claude Code sempre dentro da pasta do projeto para usar os subagentes de projeto.
