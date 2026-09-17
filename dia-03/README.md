# Dia 3

Pasta reservada para o roteiro, os exercícios e os resultados do dia 3.

## Roteiro localizado

[Material oficial — Fundamentos de LLMs, tokenização e SDK Python](https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia/blob/main/sprint_1_fundamentos_rag/dia_03_fundamentos_llms_tokens_python.md).

Cópia local em `../referencias/grupo-de-estudos-ia/sprint_1_fundamentos_rag/dia_03_fundamentos_llms_tokens_python.md`.

Atividades: Hello Gemini, contagem de tokens, laboratório de temperatura, Top-P/Top-K e desafio Code Golf de JSON. Inclui dinâmica de estimativa manual de tokens, quiz e autoavaliação.

## Executar (PowerShell, na raiz do projeto)

```powershell
.\.venv\Scripts\python.exe executar.py dia-03/01_hello_gemini.py
.\.venv\Scripts\python.exe executar.py dia-03/02_token_counter.py
.\.venv\Scripts\python.exe executar.py dia-03/03_temperature_lab.py
.\.venv\Scripts\python.exe executar.py dia-03/04_top_p_top_k_lab.py
.\.venv\Scripts\python.exe executar.py dia-03/desafio_code_golf.py
.\.venv\Scripts\python.exe executar.py dia-03/05_tiktoken_compare.py
```

Cada execução salva uma saída datada em `resultados/`. Chamadas à API usam a cota do projeto associado à chave. Modelo: `gemini-3.5-flash-lite`, carregado da `.env`.

## Resultado de 17/09/2026

| Atividade | Resultado |
| --- | --- |
| Hello Gemini | Funcionou: 21 tokens de entrada, 61 de saída, 82 no total. |
| Contagem Gemini | Inglês: 15; português com acentos: 22; código: 42. |
| Code Golf | Prompt de 30 tokens; JSON válido, chaves exatas e valores corretos. Não foi feita busca pelo menor prompt possível. |
| Comparação tiktoken `cl100k_base` | Gemini/tiktoken: inglês 15/15, português 22/24, código 40/35. |
| Temperatura e Top-P/Top-K | Scripts preparados, execução de API dispensada por incompatibilidade com o modelo escolhido. |

O exemplo de código do comparativo não tem as quebras de linha inicial/final do contador; por isso 40 e 42 tokens não representam a mesma entrada. Não compare essas duas contagens como se fossem idênticas.

`count_tokens` fornece a contagem, não o fatiamento do Gemini. O fatiamento mostrado pelo tiktoken pertence ao encoding `cl100k_base`. Os resultados de idiomas são deste pequeno conjunto, não uma regra universal.

### Adaptações ao roteiro

- Carregamento explícito da `.env` na raiz, sem imprimir credenciais.
- Modelo definido por `GEMINI_MODEL`; nenhuma troca automática para outro modelo.
- Até três tentativas em erros 500/502/503/504; falhas de autenticação ou cota não entram em repetição automática.
- Validação do Code Golf verifica valores e rejeita campos extras, além de analisar o JSON.
- Português acentuado preservado nos exemplos.
- Os laboratórios de amostragem ficam preparados para um modelo compatível. Não removemos um parâmetro em silêncio para simular que foi testado. [Documentação sobre os modelos recentes](https://ai.google.dev/gemini-api/docs/generate-content/latest-model).
- Temperatura zero não garante correção nem repetibilidade absoluta.

## Ainda depende da participação do aluno

- Dinâmica do Tokenizador Humano, adiada a pedido do aluno (a contagem já foi revelada; para um teste cego, usar novos textos).
- Experimentar versões menores do prompt e discutir os resultados com a dupla.
- [Quiz local do dia 3](../referencias/grupo-de-estudos-ia/sprint_1_fundamentos_rag/quizzes/quiz_dia_03.html).
- Leituras, vídeo e formulário do roteiro. O formulário será respondido pelo aluno.
