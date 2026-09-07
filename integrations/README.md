# Integrações — Blueprint V2

Esta pasta documenta a camada de integração futura do Jhulie Ecom AI System V2.

## Princípio
Agente não é integração.

```text
AGENTE = raciocínio especializado
SKILL = procedimento reutilizável
INTEGRAÇÃO = acesso a dados/ações
WORKFLOW = sequência operacional
```

## Camadas previstas

### Shopify
Objetivo:
- produtos;
- pedidos;
- clientes;
- estoque;
- eventos;
- dados de loja.

Arquitetura recomendada:
```text
Shopify App / OAuth
        ↓
Backend Node.js
        ↓
camada normalizada de dados
        ↓
agentes
```

### Meta Ads
Objetivo:
- leitura de campanhas;
- criativos;
- spend/performance;
- execução assistida quando autorizada.

Acesso real depende de API/tool/MCP configurado.

### Google Ads
Objetivo:
- Search;
- Shopping;
- Performance Max;
- reporting;
- execução assistida.

### GA4
Objetivo:
- comportamento;
- eventos;
- funil;
- conversão;
- validação junto ao tracking.

### WhatsApp / mensagens
Objetivo:
- receber relatórios;
- alertas;
- aprovações.

O sistema gera o relatório com `daily-ops-report`.
A entrega automática exige um provedor/integrador de WhatsApp ou workflow externo configurado.

## Segurança
- OAuth quando aplicável.
- Least privilege.
- Secrets fora do Git.
- Logs sem tokens.
- Ações financeiras/publicação sempre com guardrails.
