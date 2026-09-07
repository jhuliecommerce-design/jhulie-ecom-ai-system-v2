# Demo WOW — JHULIE ECOM AI SYSTEM PUBLIC EDITION

Objetivo: mostrar em poucos minutos por que o sistema não é apenas um pack de prompts.

## Como testar
Abra o Claude Code dentro do projeto e rode:

```text
/diagnosticar-operacao
```

Depois cole este cenário fictício:

```text
PERÍODO: últimos 3 dias
COMPARAÇÃO: 3 dias anteriores

SHOPIFY
Revenue: $21.480 → $19.960
Orders: 286 → 241
AOV: $75,10 → $82,82
CVR: 1,94% → 1,31%
Mobile CVR: 1,72% → 0,98%
Desktop CVR: 2,36% → 2,21%
Refund rate 30d: 4,6%

META
Spend: $6.200 → $6.450
Platform revenue: $14.900 → $16.200
Purchases reported: 198 → 214
CPA: $31,31 → $30,14
CTR link: 1,48% → 1,51%
CPC link: $1,17 → $1,15
Frequency: 2,3 → 2,5

GOOGLE
Spend: $2.450 → $2.510
Platform revenue: $5.800 → $5.420
CPA: $34 → $39
CTR: estável

OBSERVAÇÃO
Nenhuma grande mudança de criativo foi feita.
```

## O que um diagnóstico raso pode fazer
- concluir que Meta melhorou e deve escalar imediatamente;
- culpar Google pela queda geral;
- recomendar troca de criativo sem evidência.

## O que o sistema deve perceber
- Shopify mostra queda relevante de orders e CVR, especialmente mobile;
- Meta reporta mais purchases mesmo enquanto Shopify registra menos orders no total;
- CTR e CPC do Meta estão praticamente estáveis;
- há possível inconsistência de tracking/atribuição;
- existe um sinal forte de problema pós-clique/mobile;
- escalar mídia antes de validar tracking e conversão aumenta risco.

## Resultado esperado do JHULIE // DIRECTOR
A resposta não precisa ser idêntica, mas deve chegar a uma lógica próxima de:

1. **Não escalar Meta ainda.**
2. **Prioridade #1:** validar discrepância de purchase/revenue entre plataforma e Shopify.
3. **Prioridade #2:** investigar queda de CVR mobile.
4. **Google merece diagnóstico próprio, mas não explica sozinho a queda da operação.**
5. **Não trocar criativos apenas porque a operação piorou; os sinais de clique do Meta estão estáveis.**
6. Acionar tracking-analyst + store-analyst/store-optimizer antes de decisões agressivas de budget.

## Por que esta demo existe
Ela demonstra a diferença entre ler uma métrica isolada e coordenar a operação como um sistema.

> O valor não está em dar mais respostas. Está em evitar a decisão errada primeiro.

Todos os dados acima são fictícios e existem apenas para demonstração educacional.
