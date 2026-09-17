# Dia 4

Pasta reservada para o roteiro, os exercícios e os resultados do dia 4.

## Roteiro localizado

[Material oficial — Prompt Engineering e desafios de segurança](https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia/blob/main/sprint_1_fundamentos_rag/dia_04_prompt_engineering_gandalf.md).

Cópia local em `../referencias/grupo-de-estudos-ia/sprint_1_fundamentos_rag/dia_04_prompt_engineering_gandalf.md`.

Atividades: Few-Shot, CoT e ThinkingConfig, campeonato de classificadores, desafios Lakera, Mini-CTF do guardião, filtros defensivos, quiz e autoavaliação.

## Executar (PowerShell, na raiz do projeto)

```powershell
.\.venv\Scripts\python.exe executar.py dia-04/few_shot_cot_lab.py
.\.venv\Scripts\python.exe executar.py dia-04/campeonato_classificadores.py
.\.venv\Scripts\python.exe executar.py dia-04/ctf_guardian.py --demo
.\.venv\Scripts\python.exe executar.py dia-04/input_guardrail.py
```

Para jogar o guardião interativamente:

```powershell
.\.venv\Scripts\python.exe dia-04/ctf_guardian.py
```

Digite `sair` para encerrar. O modo interativo tem até 10 tentativas; `--demo` executa três casos sintéticos. O campeonato faz 20 gerações (duas por chamado). O limite por resposta é 2048 tokens; os exercícios consomem a cota da API.

## Resultado de 17/09/2026

| Atividade | Resultado |
| --- | --- |
| Few-Shot | Classificou o incidente de login como ALTA. |
| Problema das 45 tarefas | Respostas inconsistentes: 15 sem configuração e 45 com `include_thoughts`. Ambas assumem informação não fornecida. |
| ThinkingConfig | Chamada aceita; nenhum resumo de pensamento retornado e contagem de pensamento ausente (`None`). Não interpretamos ausência como zero. |
| Campeonato | Zero-Shot: 8/10; Few-Shot com justificativa: 8/10. |
| Guardião — demo | Respondeu à pergunta legítima, recusou pedido direto de senha e tentativa com fechamento de tag. |
| Filtro de entrada — bônus | Detectou os três exemplos suspeitos e não marcou os dois exemplos benignos. |

As saídas originais estão em `resultados/`. Uma única rodada com dez casos não demonstra superioridade de uma técnica. Zero-Shot errou os casos 3 e 9; Few-Shot errou 3 e 7. A pontuação usa igualdade exata com o gabarito, e a extração rejeita categorias ambíguas.

### O que aprender com o problema das tarefas

O total restante é **45 menos o número de tarefas já concluídas**, que não foi informado. Pedir uma explicação mais longa ou ativar um recurso de thinking não supre essa informação. `include_thoughts` pede resumos opcionais; não seleciona por si só um nível maior de raciocínio, nem revela o processo interno completo.

### Adaptações e limites do CTF

Usamos `GEMINI_MODEL` da `.env` (`gemini-3.5-flash-lite`) e removemos temperatura por compatibilidade. O regulamento original fixa `gemini-3.8-flash` e temperatura 0.7; esta versão é uma adaptação de estudo, não uma rodada oficial comparável à turma.

O guardião mantém o segredo **fictício** do roteiro no prompt, preserva perguntas legítimas, remove tags `user_query` fornecidas pelo usuário e bloqueia saída que contenha o segredo literal ou com separadores. Esse filtro não cobre todas as codificações, traduções, fragmentações ou inferências; três testes não provam segurança. Em um produto real, credenciais não devem ser fornecidas ao modelo.

O detector por regex do bônus é um exercício separado: ele pode ter falsos positivos e negativos. “Sem padrão detectado” não significa “seguro”.

## Ainda depende da participação do aluno

- Leituras e desafios Lakera no ambiente de treinamento indicado pelo professor.
- Rodadas em dupla/quarteto, troca de papéis e galeria de ataques.
- [Quiz local do dia 4](../referencias/grupo-de-estudos-ia/sprint_1_fundamentos_rag/quizzes/quiz_dia_04.html).
- Formulário: reservado ao aluno, conforme solicitado.
