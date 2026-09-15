# Dia 2 — Registro de experimentos

Status: preparação concluída; testes de acesso realizados em 14/09/2026, entre 23:32 e 23:34 (horário de Brasília). Exercícios ainda sem resposta validada.

## Checklist

- [x] Acessar o Studio e conferir os modelos disponíveis.
- [ ] Testar instruções de sistema.
- [ ] Validar extração em JSON.
- [ ] Comparar parâmetros suportados (três repetições por configuração).
- [ ] Comparar thinking e verificar as travessias.
- [ ] Testar Search, Code Execution, URL Context e Maps, quando disponíveis.
- [ ] Testar anexo de PDF ou imagem.
- [ ] Inspecionar Safety Settings e usar Compare.
- [ ] Exportar Python com Get Code e revisar antes de versionar.

## Ficha — copie uma por execução

- Data/hora:
- Experimento e repetição:
- Identificador do modelo:
- Conversa nova ou histórico usado:
- Instruções de sistema e prompt:
- Temperatura / Top-P / Top-K (inclua padrão ou indisponível):
- Limite de saída / thinking:
- Ferramentas e filtros:
- Tempo aproximado de resposta:
- Resposta obtida (sem dados pessoais ou chaves):
- Fontes consultadas, se houver:
- Verificação manual e erros encontrados:

## Conclusão após os testes

- O que mudou entre as configurações?
- O formato foi respeitado? O conteúdo estava correto?
- A ferramenta ajudou? Que evidência confirma isso?
- Quais recursos ficaram indisponíveis?
- O que queremos investigar no dia 3?


## Testes de acesso — 14/09/2026

| Teste | Modelo | Resultado observado |
| --- | --- | --- |
| Mensagem manual "teste", na conversa anterior | gemini-3.8-flash | Resposta visível: "acesso funcionando.teste". |
| Revisão de buscar_item em conversa nova, com as instruções do guia | gemini-3.8-flash | Erro interno e aviso "Failed to generate content: permission denied. Please try again." |
| Novo envio da revisão após trocar de modelo, mantendo o turno com erro no histórico | gemini-3.5-flash-lite | Mesmo erro de permissão. |

Configuração: ferramentas desligadas, nenhuma chave de API selecionada; thinking Medium no 3.8 e Minimal no 3.5 Flash Lite. Não houve resposta de revisão para avaliar. O teste entre modelos foi diagnóstico de acesso, não comparação de qualidade.

A causa permanece indeterminada. A resposta manual bem-sucedida não demonstra que todas as chamadas estão liberadas; os erros também não demonstram necessidade de plano pago.

### Próximos passos

1. Enviar manualmente o código e as instruções do guia no Studio, para comparar com os envios automatizados.
2. Se funcionar, registrar os três tópicos e seguir para Structured Output.
3. Se falhar, repetir em uma sessão normal do navegador com a mesma conta e registrar o erro; persistindo, consultar o suporte do AI Studio antes de contratar outro plano.
4. Para a etapa Python/API, verificar separadamente a chave, o projeto e as cotas do modelo. Acesso ao Playground não comprova acesso pela API.

As conversas estavam em modo temporário. Este registro preserva os resultados observados sem depender do histórico do Studio.
