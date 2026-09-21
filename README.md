# Grupo de Estudos IA — PUCRS

## Dia 1 — Ambiente Python

Configuração inicial versionada. `smoke_test.py` mostra a versão do Python e o sistema operacional.

## Dia 2 — Google AI Studio (15/09)

Material preparado para o laboratório; testes de acesso registrados e exercícios pendentes:

- [Guia e prompts](dia-02/README.md)
- [Schema para extração de dados](dia-02/aluno.schema.json)
- [Registro de experimentos](dia-02/resultados.md)

## Dias 3 e 4

- [Dia 3](dia-03/README.md) — scripts preparados e chamadas compatíveis testadas.
- [Dia 4](dia-04/README.md) — laboratório, classificadores e guardião testados.

## Dia 5 - Embeddings e busca vetorial

[Laboratório e resultados](dia-05/README.md): manual indexado, busca semântica,
comparação lexical e similaridade cosseno validados.

## Dia 6 - AskData

[Kickoff e pendências do trio](dia-06/README.md): Airflow + Docker, corpus de documentação
oficial exportada em PDF e estrutura inicial do assistente.

## Materiais oficiais do curso

Fonte: [repositório do professor](https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia).
Clone local completo, com histórico, em `referencias/grupo-de-estudos-ia` (ignorado pelo nosso Git).
Referência inicial: commit `983e935`, consultado em 17/09/2026. Os originais permanecem nesse repositório independente; nossas adaptações ficam nas pastas de cada dia.

Para obter atualizações do professor sem criar merges locais:

```powershell
git -C referencias/grupo-de-estudos-ia pull --ff-only
```

Em outro computador, recrie a cópia com:

```powershell
git clone https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia.git referencias/grupo-de-estudos-ia
```

## Configuração local

Use `.env.example` como modelo para o arquivo `.env` na raiz do projeto.
Preencha `GEMINI_API_KEY` apenas na sua cópia local.
O modelo escolhido para os próximos exercícios é `gemini-3.5-flash-lite`, definido em `GEMINI_MODEL`.
Os scripts dos dias 3 e 4 carregam essas variáveis pela biblioteca compartilhada `estudos/runtime.py`; `smoke_test.py` apenas verifica o ambiente Python.

Setup no Windows (Python 3.12):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe executar.py dia-03/01_hello_gemini.py
```

`requirements.txt` contém as dependências diretas, e `requirements-lock.txt` registra as versões instaladas. O executor salva saídas datadas em cada pasta `resultados/`. Confira os READMEs dos dias para resultados, limitações e atividades humanas pendentes. Nenhum formulário foi preenchido.

Nunca inclua chaves de API no código ou nos resultados. O arquivo `.env` já está no `.gitignore`.
