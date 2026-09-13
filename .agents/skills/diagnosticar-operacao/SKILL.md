---
name: diagnosticar-operacao
description: Use when the user asks to diagnose the overall ecommerce operation across acquisition, conversion, offer, tracking, retention, and operations; do not use for a narrow specialist question.
---

<!-- CODEX-ONLY:START command-adapter -->
Use como entrada o pedido atual do usuário e todo material disponibilizado no contexto: arquivos, screenshots, URLs, exports, métricas e observações. Não configure integrações externas. Não solicite credenciais.

Respeite o escopo solicitado. Se for um pedido pontual, responda somente ao ponto pedido; não force uma auditoria completa.

O especialista mapeado é `diretor_operacao`. Quando a delegação estiver disponível e trouxer benefício proporcional, encaminhe a análise a esse agente. Quando a delegação não estiver disponível ou não compensar, permaneça nesta sessão e siga diretamente o método especializado abaixo. Em ambos os casos, consolide a resposta final para o usuário.
<!-- CODEX-ONLY:END command-adapter -->

Objetivo:
- identificar o maior gargalo financeiro;
- separar aquisição, conversão, oferta, tracking, retenção e operação;
- definir prioridade imediata;
- indicar quais especialistas devem ser acionados.

Retorne:
1. Resumo executivo
2. Saúde da operação
3. Gargalo principal
4. Evidências
5. Hipóteses
6. Plano 24h
7. Plano 7d
8. Plano 30d
9. Especialistas a acionar
10. Dados faltantes

Não invente dados nem integrações.
