# Política — Segurança de execução

## Ações de baixo risco
Leitura de arquivos, diagnóstico, geração de relatórios e propostas podem ocorrer normalmente.

## Ações que exigem cuidado
Edição de tema, backend, scripts de tracking e configurações devem ser pequenas, revisáveis e testáveis.

## Ações que exigem autorização explícita
- alterar orçamento;
- pausar/ativar campanhas;
- publicar tema;
- enviar email/WhatsApp ao cliente;
- emitir/refundir pagamento;
- excluir dados;
- alterar credenciais;
- mudanças destrutivas ou de produção.

## Secrets
Nunca salve API keys, access tokens ou senhas no git. Use .env ou secret manager e mantenha .env fora do versionamento.
