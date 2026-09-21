# Dia 6 - Kickoff AskData

Tema escolhido: **Engenharia de Dados e DevOps**.
Recorte autorizado: **Airflow + Docker para executar e diagnosticar pipelines de dados**.

O projeto está em [askdata/](askdata/README.md), pronto para ser copiado para o
repositório colaborativo do trio. Ainda usamos o repositório pessoal de estudos.

## Conceitos do dia

- **RAG:** buscar trechos dos documentos e fornecer esses trechos à IA para responder.
- **Ingestão:** extrair texto, dividir em pedaços, gerar embeddings e guardar no banco.
- **Chunk:** trecho de texto; a sobreposição evita perder contexto na fronteira.
- **Embedding:** vetor que permite comparar o significado da pergunta com o dos trechos.
- **Grounding:** orientar a resposta pelas evidências recuperadas. Não garante acerto;
  vamos conferir as citações e recusar perguntas sem suporte.
- **DAG:** tarefas e dependências de um fluxo, sem ciclos. Airflow coordena a execução.
- **Docker Compose:** descreve serviços e sua configuração para executá-los juntos.

## Entregas e pendências

- [x] Tema e recorte definidos.
- [x] Corpus coletado: 4 PDFs / 38 páginas, exportados de documentação oficial.
- [x] Estrutura, exemplo de ambiente e teste offline preparados.
- [x] Pitch e perguntas de avaliação preparados.
- [ ] Confirmar nomes e GitHub dos três integrantes.
- [ ] Criar/definir repositório do trio e configurar colaboradores.
- [ ] Cada integrante clonar e executar o smoke test.
- [ ] Apresentar pitch para outro trio e registrar feedback.
- [ ] Definir piloto dos dias 7, 8 e 9 e canal de comunicação.
- [ ] Fazer leituras, quiz e formulário individualmente.

Nenhum formulário foi preenchido. O dia 6 não inclui implementar o RAG completo.

Fonte do roteiro: [material do professor](https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia/blob/main/sprint_1_fundamentos_rag/dia_06_kickoff_projeto_arquitetura_rag.md).
