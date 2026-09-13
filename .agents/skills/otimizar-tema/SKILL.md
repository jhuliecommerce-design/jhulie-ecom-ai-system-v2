---
name: otimizar-tema
description: Use when the user asks to inspect or change a local Shopify theme using Liquid, CSS, or JavaScript; do not use when no theme change or local implementation is requested.
---

<!-- CODEX-ONLY:START command-adapter -->
Use como entrada o pedido atual do usuário e todo material disponibilizado no contexto: arquivos, screenshots, URLs, exports, métricas e observações. Não configure integrações externas. Não solicite credenciais.

Respeite o escopo solicitado. Se for um pedido pontual, responda somente ao ponto pedido; não force uma auditoria completa.

O especialista mapeado é `theme_engineer`. Quando a delegação estiver disponível e trouxer benefício proporcional, encaminhe a análise a esse agente. Quando a delegação não estiver disponível ou não compensar, permaneça nesta sessão e siga diretamente o método especializado abaixo. Em ambos os casos, consolide a resposta final para o usuário.
<!-- CODEX-ONLY:END command-adapter -->

Antes de editar:
1. localize os arquivos relevantes;
2. explique o plano;
3. identifique riscos.

Depois:
1. implemente somente se houver arquivos locais e a solicitação pedir execução;
2. preserve funcionalidades existentes;
3. liste arquivos alterados;
4. explique como testar;
5. explique como reverter.

Nunca publique em produção ou use credenciais sem autorização explícita.
