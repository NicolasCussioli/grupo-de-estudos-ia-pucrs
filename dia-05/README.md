# Dia 5 - Embeddings e busca vetorial

Laboratório técnico validado em 21/09/2026: extração do manual Redmi Watch 5,
embeddings Google, índice persistente Chroma e comparação com busca por palavras.

## Como funciona

Cada página é convertida em um vetor de 768 números pelo modelo
`gemini-embedding-001`. A pergunta também vira um vetor; o Chroma recupera as
páginas com direções mais parecidas usando distância cosseno. Os vetores são
normalizados. Documentos usam `RETRIEVAL_DOCUMENT`; consultas, `RETRIEVAL_QUERY`.

O banco fica local, mas o texto é enviado à API Google para gerar embeddings.
Este laboratório recupera trechos; não gera uma resposta RAG com um modelo de texto.
O modelo de geração do restante do projeto continua `gemini-3.5-flash-lite`.

## Executar a partir da raiz

Requisitos: Python 3.12, dependências instaladas, `.env` com `GEMINI_API_KEY`
e cópia do repositório do professor em `referencias/grupo-de-estudos-ia`
(instruções no README principal).

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe executar.py dia-05/indexar_documentos.py
.\.venv\Scripts\python.exe executar.py dia-05/avaliar_buscas.py
.\.venv\Scripts\python.exe executar.py dia-05/similaridade_manual.py
.\.venv\Scripts\python.exe dia-05/buscador_semantico.py
```

O último comando é interativo; digite `sair` para encerrar. Os demais salvam registros
em `resultados/`. A indexação ignora páginas já presentes e retoma índices incompletos.
Uma mudança no PDF ou na política de extração cria outra coleção, preservando a anterior.
O banco `chroma_data/` é ignorado pelo Git e deve ser recriado em cada computador.

## Resultados observados

- Manual: 13 páginas indexadas.
- Testes offline: 9 aprovados, incluindo persistência, retomada, cosseno e validações.
- Busca semântica: página relevante em primeiro lugar em **6/6** perguntas.
- Busca semântica e lexical: ao menos uma página relevante entre as duas primeiras
  em **6/6** perguntas para cada método. A lexical conta termos; não implementa BM25.
- Pergunta sobre bateria/carregamento: recuperadas as duas páginas esperadas, 4 e 11.
- Similaridade de frases sobre restauração: **0,8756**; restauração versus bolo: **0,7000**.
- Pergunta fora do escopo (bolo): o banco ainda retornou páginas 13 e 12.

Os números de similaridade não são probabilidades nem garantem resposta correta.
Os seis casos são uma amostra pequena do roteiro, não uma avaliação geral de qualidade.
No teste fora do escopo, o sistema mostra o problema; ainda não há recusa automática.

## Cuidados com as fontes

As páginas são contadas a partir de 1 no PDF, não pelo número impresso no rodapé.
O gabarito foi ajustado após inspeção visual. O manual contém texto extraível repetido
ou fora da região visível em algumas páginas; por isso uma recuperação pode conter
texto cuja posição visual exige conferência. Não confundir recuperação com citação validada.

Base pedagógica: repositório `eduardo-de-bastiani/grupo-de-estudos-ia`, commit `983e935`.
Os registros antigos de indexação preservam avisos da primeira execução; a execução de
21/09 usa fonttools e a política `pagina-nfkc-fonttools-v2`.

Dinâmicas em grupo, quiz e formulário continuam como atividades individuais/presenciais;
estes resultados comprovam somente o laboratório técnico.
