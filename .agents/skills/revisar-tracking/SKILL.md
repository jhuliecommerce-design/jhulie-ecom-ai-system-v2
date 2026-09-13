---
name: revisar-tracking
description: Use when the user asks to review ecommerce tracking across GA4, Pixel/CAPI, Google Ads, events, or deduplication; do not use for a media-performance diagnosis without a tracking scope.
---

<!-- CODEX-ONLY:START command-adapter -->
Use como entrada o pedido atual do usuário e todo material disponibilizado no contexto: arquivos, screenshots, URLs, exports, métricas e observações. Não configure integrações externas. Não solicite credenciais.

Respeite o escopo solicitado. Se for um pedido pontual, responda somente ao ponto pedido; não force uma auditoria completa.

O especialista mapeado é `tracking_analyst`. Quando a delegação estiver disponível e trouxer benefício proporcional, encaminhe a análise a esse agente. Quando a delegação não estiver disponível ou não compensar, permaneça nesta sessão e siga diretamente o método especializado abaixo. Em ambos os casos, consolide a resposta final para o usuário.
<!-- CODEX-ONLY:END command-adapter -->

Avalie quando aplicável:
- Shopify events;
- GA4/GTM;
- Meta Pixel/CAPI;
- Google Ads conversions;
- deduplicação;
- purchase value/currency/order_id.

Retorne:
1. Mapa atual
2. Falhas críticas
3. Impacto
4. Correções por prioridade
5. Plano de validação
6. Evidências necessárias

Nunca declare tracking correto sem evidência.
