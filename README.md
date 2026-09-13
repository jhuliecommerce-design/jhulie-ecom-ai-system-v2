# JHULIE ECOM AI SYSTEM — PUBLIC EDITION

**A camada pública da minha lógica operacional, transformada em agentes para ecommerce.**

Este projeto não é um pack de prompts.

É uma arquitetura operacional dual para Claude Code e Codex, com agentes especializados, comandos, skills e workflows para ecommerce.

> A Public Edition entrega uma parte prática e funcional da forma como eu estruturo análise e operação com IA. A versão completa — com metodologia proprietária, playbooks internos, integrações avançadas, automações e infraestrutura de execução — é reservada às camadas privadas do ecossistema Jhulie Ecom.

---

## O que você recebe nesta edição

- agentes executáveis para Claude Code e Codex;
- comandos rápidos;
- skills reutilizáveis;
- workflows públicos;
- regras de integridade de dados;
- segurança de execução;
- exemplos de uso;
- arquitetura preparada para evoluir com integrações reais.

---

## A ideia

Você não está recebendo uma IA genérica.

Está recebendo uma **camada pública da minha lógica operacional aplicada a ecommerce** — organizada em especialistas que trabalham dentro do seu projeto.

Os agentes usam uma identidade discreta:

```text
JHULIE // DIRECTOR
JHULIE // STORE ANALYST
JHULIE // META BUYER
JHULIE // GOOGLE BUYER
JHULIE // TRACKING ANALYST
JHULIE // SEO COMMERCE
```

O nome técnico continua simples em cada host. O prefixo `JHULIE //` é a identidade do sistema, não um comando diferente.

---

## Arquitetura pública

```text
DADOS
Shopify / GA4 / Meta / Google / arquivos / contexto
                     ↓
               STORE ANALYST
                     ↓
               JHULIE // DIRECTOR
                     ↓
        ESPECIALISTA RESPONSÁVEL
      ↙       ↓        ↓        ↘
  STORE     TRAFFIC   SEO    TRACKING
    ↓          ↓
 THEME     META / GOOGLE
 ENGINEER
                     ↓
        EXECUÇÃO ASSISTIDA / TESTE
                     ↓
               NOVOS DADOS
```

Princípio:

**DADOS → DIAGNÓSTICO → PRIORIDADE → EXECUÇÃO → VALIDAÇÃO**

---

## Agentes executáveis

Os agentes ficam em `.claude/agents/` para Claude Code e `.codex/agents/` para Codex. Os nomes Claude usam hífen; os nomes Codex equivalentes usam `snake_case`.

| Identidade | Nome técnico | Função |
|---|---|---|
| JHULIE // DIRECTOR | `diretor-operacao` | Prioridade estratégica, conflitos e coordenação |
| JHULIE // STORE ANALYST | `store-analyst` | Métricas, funil e saúde da operação |
| JHULIE // STORE OPTIMIZER | `store-optimizer` | CRO, UX, PDP, coleções e conversão |
| JHULIE // THEME ENGINEER | `theme-engineer` | Shopify theme, Liquid, CSS e JS |
| JHULIE // TRAFFIC DIRECTOR | `traffic-director` | Leitura consolidada de mídia e verba |
| JHULIE // META BUYER | `meta-media-buyer` | Meta Ads |
| JHULIE // GOOGLE BUYER | `google-media-buyer` | Search, Shopping e PMax |
| JHULIE // TRACKING ANALYST | `tracking-analyst` | GA4, Meta Pixel/CAPI e Google tracking |
| JHULIE // SEO COMMERCE | `seo-commerce` | SEO de produtos, coleções e arquitetura |
| JHULIE // COMPETITOR INTELLIGENCE | `competitor-intelligence` | Concorrentes, ads, oferta e funnel |
| JHULIE // SAC OPERATOR | `sac-operator` | Atendimento ecommerce |

---

## Commands

Atalhos disponíveis em `.claude/commands/`:

```text
/jhulie-daily
/diagnosticar-operacao
/auditar-loja
/otimizar-pdp
/otimizar-tema
/diagnosticar-meta
/diagnosticar-google
/decidir-verba
/revisar-tracking
/auditar-seo
/analisar-concorrente
/responder-sac
```

No Codex, use os mesmos nomes como skills, trocando `/` por `$`. Exemplo: `$diagnosticar-operacao`. Veja o guia completo em [`README_CODEX.md`](README_CODEX.md).

### JHULIE DAILY
Use `/jhulie-daily` para fazer um check-up rápido da operação.

Você não precisa preencher um formulário completo. Pode usar:
- um screenshot;
- um CSV/export;
- algumas métricas principais;
- uma observação do que está acontecendo.

O sistema começa com o que estiver disponível e só deve pedir 1–3 dados adicionais quando forem realmente necessários.

---

## Skills

Skills reutilizáveis em `.claude/skills/`:

```text
/cro-audit
/pdp-optimization
/media-buying
/tracking-audit
/seo-product
/competitor-research
/daily-ops-report
```

No Codex, elas ficam em `.agents/skills/` e podem ser chamadas com `$`, por exemplo `$cro-audit`.

---

## Instalação

### 1. Clone o projeto

No terminal:

```bash
git clone https://github.com/jhuliecommerce-design/jhulie-ecom-ai-system-v2.git
cd jhulie-ecom-ai-system-v2
```

### 2. Escolha o host

Para Claude Code:

```bash
claude
```

Dentro do Claude Code, confira os agentes com:


```text
/agents
```

Para Codex:

```bash
codex
```

Dentro do Codex, confira as skills com `/skills`. Consulte [`README_CODEX.md`](README_CODEX.md) para instalação, especialistas e exemplos.

---

## Primeiros testes

Os exemplos abaixo usam a sintaxe Claude. No Codex, use `$` no lugar de `/`, como em `$diagnosticar-operacao`.

### JHULIE DAILY

```text
/jhulie-daily

Receita: $8.300
Pedidos: 118
CVR: 1,2%
Meta spend: $2.100
Google spend: $900
Observação: mobile caiu bastante nos últimos dias.
```

### Diagnóstico da operação

```text
/diagnosticar-operacao

Receita: $12.400
Spend Meta: $3.100
Spend Google: $1.900
Pedidos: 162
AOV: $76,54
CVR: 1,42%
MER: 2,48
```

### Concorrente

```text
/analisar-concorrente https://site-do-concorrente.com
```

### CRO

```text
/auditar-loja https://sua-loja.com/products/produto
```

Veja mais em `examples/`.

---

## Demo WOW

Quer entender rapidamente o nível de raciocínio do sistema?

Abra `examples/demo-wow.md` e rode o cenário proposto com `/diagnosticar-operacao` no Claude Code ou `$diagnosticar-operacao` no Codex.

A demo foi desenhada para testar se o JHULIE // DIRECTOR evita uma decisão precipitada de mídia ao perceber sinais de tracking inconsistente e queda de conversão mobile.

Todos os dados da demo são fictícios e educacionais.

---

## Input sem fricção

Veja `examples/00-quick-input.md`.

O sistema foi desenhado para começar com o que você tiver: print, export, métricas principais ou contexto. Não para transformar análise em preenchimento de formulário.

---

## O que esta edição NÃO promete

Os agentes não possuem acesso mágico às suas contas.

Sem integração real, eles trabalham com:
- dados que você fornecer;
- arquivos locais;
- páginas públicas acessíveis;
- contexto do projeto.

Com backend, APIs ou MCP configurados, eles podem trabalhar com dados reais dentro das permissões concedidas.

O sistema nunca deve afirmar que:
- leu uma conta não conectada;
- alterou campanha sem API/tool;
- publicou tema sem execução real;
- enviou mensagem sem integração.

---

## Public Edition vs. estrutura privada

Esta versão foi criada para compartilhar valor real sem publicar toda a estrutura proprietária.

A Public Edition **não inclui**:
- metodologia Jhulie completa;
- thresholds e critérios privados de escala;
- playbooks internos;
- executores avançados de mídia;
- backend Shopify completo;
- automações privadas;
- infraestrutura completa usada nas camadas de mentoria.

---

## Segurança

- não versione `.env`;
- nunca coloque API keys ou tokens no Git;
- use permissões mínimas;
- mantenha mudanças de tema reversíveis;
- mudanças financeiras exigem autorização;
- valide tracking antes de automatizar decisões.

Leia:
- `core/policies/data-integrity.md`
- `core/policies/execution-safety.md`

---

## Documentação

- Guia de uso: `README_USO.md`
- Guia do Codex: `README_CODEX.md`
- Instruções do Claude Code: `CLAUDE.md`
- Instruções do Codex: `AGENTS.md`
- Quick input: `examples/00-quick-input.md`
- Demo WOW: `examples/demo-wow.md`
- Exemplos: `examples/`
- Roadmap: `ROADMAP.md`

---

## Status

**PUBLIC EDITION — V2 Alpha**

A fundação pública está pronta para diagnóstico, análise e execução assistida. Integrações reais e automações avançadas pertencem às próximas camadas do ecossistema.

---

## Princípio

> **Uma camada pública da minha lógica operacional. Dentro da sua operação.**
