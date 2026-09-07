# Workflow — Relatório diário + entrega

## Objetivo
Gerar uma leitura diária da operação e, quando houver integração, entregá-la automaticamente ao responsável.

```text
Shopify + GA4 + Meta + Google
             ↓
      normalização de dados
             ↓
       store-analyst
             ↓
     daily-ops-report
             ↓
      diretor-operacao
             ↓
        relatório final
             ↓
WhatsApp / Slack / Email / ClickUp
      (integração externa)
```

## Conteúdo recomendado
- Receita
- Pedidos
- AOV
- CVR
- Spend por canal
- CAC
- MER
- Top produtos
- Alertas de tracking
- Anomalias
- Prioridades do dia

## Guardrails
- Não enviar automaticamente se o destinatário não estiver configurado.
- Não expor dados pessoais desnecessários.
- Não dizer “enviado” sem confirmação da ferramenta externa.
- Alertas críticos devem conter evidência e nível de confiança.
