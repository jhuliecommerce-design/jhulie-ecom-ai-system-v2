# Jhulie Ecom AI System V2

**AI Operating System for Ecommerce**

Um sistema de agentes, skills, comandos e workflows para operar ecommerce com Claude Code.

> Não é uma biblioteca de prompts. É uma arquitetura operacional.

---

## O que este sistema resolve

O V2 foi desenhado para transformar IA em uma camada de operação real para ecommerce:

- diagnóstico da operação;
- leitura de métricas e funil;
- CRO e otimização de loja;
- personalização segura de tema Shopify;
- Meta Ads;
- Google Ads;
- tracking e qualidade de sinal;
- SEO ecommerce;
- inteligência competitiva;
- SAC;
- relatórios diários;
- workflows com separação entre análise, decisão e execução.

---

## Arquitetura

```text
DADOS
Shopify + GA4 + Meta + Google + arquivos/contexto
                     ↓
               STORE ANALYST
                     ↓
            DIRETOR DA OPERAÇÃO
                     ↓
        ESPECIALISTA RESPONSÁVEL
      ↙       ↓        ↓        ↘
  STORE     TRAFFIC   SEO    TRACKING
    ↓          ↓
 THEME     META / GOOGLE
 ENGINEER
                     ↓
            EXECUÇÃO / TESTE
                     ↓
               NOVOS DADOS
```

O sistema trabalha em loop:

**DADOS → DIAGNÓSTICO → PRIORIDADE → EXECUÇÃO → VALIDAÇÃO**

---

## Agentes executáveis

Os subagentes vivem em `.claude/agents/`.

| Agente | Função |
|---|---|
| `diretor-operacao` | Prioridade estratégica e coordenação |
| `store-analyst` | Métricas, funil e saúde da operação |
| `store-optimizer` | CRO, UX, PDP, coleção e conversão |
| `theme-engineer` | Shopify theme, Liquid, CSS, JS e implementação |
| `traffic-director` | Alocação e leitura consolidada de mídia |
| `meta-media-buyer` | Meta Ads |
| `google-media-buyer` | Search, Shopping e PMax |
| `tracking-analyst` | GA4, Meta Pixel/CAPI e Google tracking |
| `seo-commerce` | SEO de produtos, coleções e arquitetura |
| `competitor-intelligence` | Concorrentes, ofertas, ads e funnels |
| `sac-operator` | Atendimento ecommerce |

---

## Commands

Atalhos práticos em `.claude/commands/`:

```text
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

---

## Skills

O V2 também usa skills nativas do Claude Code em `.claude/skills/`.

```text
/cro-audit
/pdp-optimization
/media-buying
/tracking-audit
/seo-product
/competitor-research
/daily-ops-report
```

Skills são procedimentos reutilizáveis. O Claude pode carregá-las quando forem relevantes ou você pode chamá-las diretamente.

---

## Instalação

### 1. Clone o projeto

No terminal:

```bash
git clone https://github.com/jhuliecommerce-design/jhulie-ecom-ai-system-v2.git
cd jhulie-ecom-ai-system-v2
```

### 2. Abra o Claude Code

```bash
claude
```

### 3. Confira os agentes

Dentro do Claude Code:

```text
/agents
```

---

## Primeiros testes

### Diagnóstico geral

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

Veja mais exemplos na pasta `examples/`.

---

## Como o sistema trata dados reais

Os agentes **não possuem acesso mágico** às suas contas.

Sem integração, eles trabalham com:
- dados fornecidos no chat;
- arquivos locais;
- páginas públicas acessíveis;
- contexto do projeto.

Com backend, APIs ou MCP configurados, eles podem trabalhar com dados reais dentro das permissões concedidas.

O sistema nunca deve afirmar que:
- leu uma conta que não estava conectada;
- alterou campanha sem API/tool;
- publicou tema sem execução real;
- enviou mensagem sem integração.

---

## Segurança

Antes de colocar o sistema em produção:

- não versione `.env`;
- nunca coloque tokens/API keys nos prompts ou no Git;
- use permissões mínimas;
- mantenha mudanças de tema reversíveis;
- mudanças financeiras exigem autorização;
- valide tracking antes de automatizar decisões;
- mantenha humano no loop para ações sensíveis.

Leia:
- `core/policies/data-integrity.md`
- `core/policies/execution-safety.md`

---

## Workflows

A pasta `core/workflows/` documenta a lógica operacional:

1. operação diária;
2. gestão de tráfego;
3. otimização de loja e tema;
4. SEO ecommerce.

---

## Documentação

- **Guia de uso:** `README_USO.md`
- **Regras do Claude Code:** `CLAUDE.md`
- **Exemplos:** `examples/`
- **Histórico:** `CHANGELOG.md`

---

## Status

**V2 Alpha**

A fundação operacional está pronta. As próximas camadas incluem integrações reais, backend Shopify, automações de relatório e execução assistida em plataformas externas.

---

## Princípio do projeto

> **IA sem dado é hipótese. IA com dado, processo e ação vira operação.**
