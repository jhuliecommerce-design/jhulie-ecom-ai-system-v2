---
name: jhulie-daily
description: Use when the user asks for a daily ecommerce operational health check and today's priorities; do not use for an exhaustive one-off audit.
---

<!-- CODEX-ONLY:START command-adapter -->
Use como entrada o pedido atual do usuário e todo material disponibilizado no contexto: arquivos, screenshots, URLs, exports, métricas e observações. Não configure integrações externas. Não solicite credenciais.

Respeite o escopo solicitado. Se for um pedido pontual, responda somente ao ponto pedido; não force uma auditoria completa.

O especialista mapeado é `diretor_operacao`. Quando a delegação estiver disponível e trouxer benefício proporcional, encaminhe a análise a esse agente. Quando a delegação não estiver disponível ou não compensar, permaneça nesta sessão e siga diretamente o método especializado abaixo. Em ambos os casos, consolide a resposta final para o usuário.
<!-- CODEX-ONLY:END command-adapter -->

Aceite como entrada:
- screenshot de Shopify, Meta, Google ou GA4;
- CSV/export;
- relatório colado;
- poucas métricas principais;
- observações do operador.

Não exija um formulário completo. Trabalhe com o que existe e peça no máximo 1–3 dados adicionais somente se forem realmente críticos.

Analise:
- saúde geral da operação;
- qualidade/confiabilidade dos dados;
- mudanças relevantes versus comparação disponível;
- maior gargalo do momento;
- riscos;
- o que não deve ser alterado agora;
- prioridades de hoje.

Retorne exatamente nesta estrutura:

JHULIE // DAILY — PUBLIC EDITION

1. HEALTH CHECK
- classificação: FORTE / ESTÁVEL / ATENÇÃO / CRÍTICO
- uma frase de contexto

2. O QUE MUDOU
- até 5 bullets

3. GARGALO PRINCIPAL
- uma frase

4. RISCOS / ALERTAS
- somente os relevantes

5. PRIORIDADES DE HOJE
- máximo 5

6. NÃO MEXER AGORA
- proteja a operação de mudanças precipitadas

7. ESPECIALISTAS A ACIONAR
- apenas os necessários

8. O QUE REVISAR AMANHÃ
- métricas/sinais que confirmam ou invalidam a leitura

9. DADOS FALTANTES
- somente se forem realmente necessários

Nunca invente acesso a plataformas. Nunca diga que executou ação sem confirmação de ferramenta real.
