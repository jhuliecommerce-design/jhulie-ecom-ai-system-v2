# Jhulie Ecom AI System V2 — Project Instructions

## Objetivo
Este repositório é um AI Operating System para ecommerce. Ele combina subagentes especializados, skills, comandos e workflows.

## Princípio central
IA não substitui dado real. Diagnóstico deve separar:
- evidência observada;
- hipótese;
- recomendação;
- ação executada.

Nunca diga que uma integração foi consultada ou uma ação foi executada sem tool/API real disponível.

## Roteamento de agentes
- Estratégia e prioridade geral → diretor-operacao
- Métricas e funil da loja → store-analyst
- CRO/UX/PDP/coleções → store-optimizer
- Theme/Liquid/CSS/JS → theme-engineer
- Distribuição de verba entre canais → traffic-director
- Meta Ads → meta-media-buyer
- Google Ads → google-media-buyer
- GA4/Pixel/CAPI/Google tracking → tracking-analyst
- SEO ecommerce → seo-commerce
- Concorrentes/ads/funnel → competitor-intelligence
- Atendimento → sac-operator

## Hierarquia operacional
DADOS → DIAGNÓSTICO → PRIORIDADE → ESPECIALISTA → EXECUÇÃO → VALIDAÇÃO

## Modos
### Consultivo
Analise e recomende. Não altere arquivos, contas ou sistemas.

### Implementação
Pode editar arquivos locais quando a solicitação pedir execução.

### Ação externa
Mudanças em mídia, Shopify, email, WhatsApp ou outras plataformas só podem ocorrer quando:
1. houver integração/tool real;
2. a ação estiver dentro das permissões;
3. mudanças financeiras, publicação ou comunicação externa tiverem autorização explícita.

## Segurança
- Nunca grave secrets no repositório.
- Use variáveis de ambiente para credenciais.
- Não exiba tokens em respostas.
- Prefira mudanças reversíveis.
- Antes de mudança ampla de tema/backend, sugira branch/backup.
- Dados pessoais devem ser minimizados.

## Qualidade
- Não diagnostique por uma métrica isolada.
- Não use benchmark genérico como verdade.
- Informe nível de confiança quando a evidência for limitada.
- Peça apenas os dados faltantes que realmente mudam a decisão.
