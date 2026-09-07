---
name: tracking-audit
description: Procedimento de auditoria de tracking para Shopify, GA4, Meta Pixel/CAPI e Google Ads. Use ao investigar divergências, duplicações e eventos ausentes.
---

# Tracking Audit

## Mapa esperado
Liste origem, evento, destino e identificadores.

Eventos comuns:
- page_view
- view_item
- add_to_cart
- begin_checkout
- purchase

## Verificações
1. Evento dispara?
2. Dispara uma vez?
3. Browser e server deduplicam corretamente?
4. value/currency/order_id são consistentes?
5. GA4 recebe evento esperado?
6. Meta recebe Pixel/CAPI quando configurados?
7. Google Ads recebe a conversão correta?
8. Consentimento interfere na coleta?
9. Diferença é coleta quebrada ou apenas atribuição?

## Severidade
- P0: purchase ausente/duplicado ou valor incorreto
- P1: evento de funil crítico inconsistente
- P2: parâmetros secundários
- P3: melhoria de observabilidade

## Entrega
Mapa → falhas → impacto → correção → teste de validação.
