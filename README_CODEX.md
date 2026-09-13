# Guia do Codex — JHULIE ECOM AI SYSTEM V2

Este repositório possui uma implementação nativa para Codex sem remover a implementação existente para Claude Code.

## Pré-requisitos

- Git instalado;
- Codex instalado e autenticado;
- este repositório aberto como pasta de trabalho no Codex.

## Instalação

Clone o projeto e entre na pasta:

```bash
git clone https://github.com/jhuliecommerce-design/jhulie-ecom-ai-system-v2.git
cd jhulie-ecom-ai-system-v2
```

Inicie o Codex nessa pasta ou abra a pasta pelo aplicativo/IDE que hospeda o Codex:

```bash
codex
```

O Codex lê `AGENTS.md`, descobre as skills de `.agents/skills/` e encontra os especialistas de `.codex/agents/` a partir do contexto deste projeto. Se o projeto já estava aberto antes de uma atualização, reinicie a sessão do Codex caso as novas skills ainda não apareçam.

## Descobrir e chamar skills

Use `/skills` para conferir as skills disponíveis. O Codex também pode escolhê-las automaticamente pelo pedido, mas você pode solicitar uma explicitamente com `$nome-da-skill`.

Os antigos comandos do Claude possuem equivalentes Codex:

| Trabalho | Claude Code | Codex |
|---|---|---|
| Check-up diário | `/jhulie-daily` | `$jhulie-daily` |
| Diagnóstico geral | `/diagnosticar-operacao` | `$diagnosticar-operacao` |
| Auditoria CRO | `/auditar-loja` | `$auditar-loja` |
| Otimização de PDP | `/otimizar-pdp` | `$otimizar-pdp` |
| Implementação no tema | `/otimizar-tema` | `$otimizar-tema` |
| Meta Ads | `/diagnosticar-meta` | `$diagnosticar-meta` |
| Google Ads | `/diagnosticar-google` | `$diagnosticar-google` |
| Alocação de verba | `/decidir-verba` | `$decidir-verba` |
| Tracking | `/revisar-tracking` | `$revisar-tracking` |
| SEO | `/auditar-seo` | `$auditar-seo` |
| Concorrentes | `/analisar-concorrente` | `$analisar-concorrente` |
| Atendimento | `/responder-sac` | `$responder-sac` |

As sete skills reutilizáveis também estão disponíveis:

```text
$cro-audit
$pdp-optimization
$media-buying
$tracking-audit
$seo-product
$competitor-research
$daily-ops-report
```

Você pode colocar o contexto na mesma mensagem ou anexar arquivos, screenshots, URLs, exports e métricas. Exemplo:

```text
$jhulie-daily

Receita: R$ 8.300
Pedidos: 118
CVR: 1,2%
Meta spend: R$ 2.100
Google spend: R$ 900
Observação: a conversão mobile caiu nos últimos dias.
```

## Especialistas

Os especialistas customizados ficam em `.codex/agents/` e usam nomes `snake_case`:

```text
diretor_operacao
store_analyst
store_optimizer
theme_engineer
traffic_director
meta_media_buyer
google_media_buyer
tracking_analyst
seo_commerce
competitor_intelligence
sac_operator
```

As skills operacionais já indicam o especialista adequado. Quando a delegação estiver disponível, você também pode pedir, por exemplo: “use o especialista `diretor_operacao` para consolidar este diagnóstico”. Sem delegação, a própria skill executa o mesmo método especializado na sessão atual.

## Demo WOW

Abra `examples/demo-wow.md`, copie o cenário e envie:

```text
$diagnosticar-operacao

[cole aqui o cenário da demo]
```

A demo usa dados fictícios para verificar se o sistema reconhece problemas de tracking e conversão antes de recomendar mudanças precipitadas em mídia.

## Limites e segurança

O sistema não possui acesso mágico a Shopify, Meta, Google, GA4 ou atendimento. Sem integração real, ele trabalha somente com dados fornecidos, arquivos locais, páginas públicas acessíveis e contexto do projeto.

Uma integração real amplia apenas o acesso autorizado; não elimina as regras de segurança. Mudanças financeiras, pausa ou ativação de campanhas, publicação, comunicação externa, pagamentos, reembolsos, exclusões, produção e uso de credenciais sempre exigem autorização explícita.

O sistema não deve afirmar que acessou uma conta, publicou um tema, alterou uma campanha ou enviou uma mensagem sem confirmação de ferramenta real.

## Estrutura dual e manutenção

- Claude Code: `CLAUDE.md`, `.claude/agents/`, `.claude/commands/` e `.claude/skills/`;
- Codex: `AGENTS.md`, `.codex/agents/` e `.agents/skills/`.

As duas superfícies são versionadas separadamente para funcionar de modo nativo em cada host. Ao alterar agentes, comandos ou skills, mantenha a paridade pública e execute:

```bash
python scripts/validate_codex_compat.py
```

O validador verifica inventário, frontmatter, TOML, políticas críticas, conteúdo operacional e preservação da superfície Claude.
