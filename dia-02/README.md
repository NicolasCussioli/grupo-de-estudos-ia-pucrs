# Dia 2 — Laboratório Google AI Studio

## O que já está preparado

Prompts, schema e ficha de resultados preparados. Consulte `resultados.md` para os testes de acesso; ainda não obtivemos resposta validada dos exercícios.

## Começar pelo navegador — cerca de 20 minutos

1. Abra o [Google AI Studio](https://aistudio.google.com/) e entre na sua conta.
2. Confira os termos, os modelos disponíveis e as condições de uso da sua conta.
3. Localize o Playground e o campo de instruções de sistema.
4. Faça o exercício 1 abaixo e registre a resposta em `resultados.md`.
5. Faça o exercício 2 usando o arquivo `aluno.schema.json`.

A chave de API será necessária para executar código local. Quando for criá-la, use a área de chaves do Studio e guarde-a localmente; não cole a chave nas anotações ou no GitHub. Confirme as cotas e a disponibilidade de nível gratuito do modelo escolhido antes de usar a API.

## 1. Instruções de sistema

Cole no campo System Instructions:

```text
Você é um revisor de código sênior da DataLakers.
Sua função é identificar potenciais bugs e problemas de performance em Python.
Responda em exatamente três tópicos numerados, de forma técnica e direta.
Se não houver bug, diga isso explicitamente. Distinga melhoria de estilo de erro.
```

Mensagem do usuário:

```python
def buscar_item(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return True
    return False
```

Critérios: exatamente três tópicos; não inventar um bug; reconhecer que a busca é linear, O(n). Usar `alvo in lista` simplifica esse caso, mas continua O(n) para listas. Instruções de sistema orientam o comportamento; não garantem obediência.

## 2. Saída estruturada

Ative Structured Output e use `aluno.schema.json`. Envie:

```text
Oi, sou a Mariana, faço o quarto semestre de Engenharia de Software na PUCRS
e manjo bastante de Python, Docker e PostgreSQL.
```

Confira se o JSON contém nome Mariana, curso Engenharia de Software, semestre inteiro 4 e as três tecnologias. JSON válido não garante que os fatos extraídos estejam corretos.

## 3. Temperatura e Top-K

```text
Complete a frase com uma metáfora poética e original:
"Um banco de dados vetorial é como..."
```

- Escolha um modelo que exponha e suporte o parâmetro desejado.
- Execute três vezes por configuração, em conversas novas, mantendo prompt, modelo e demais controles iguais.
- Se suportado, compare temperaturas 0.0, 1.0 e 1.8. Depois teste Top-K = 1 com temperatura 1.0.
- Registre controles indisponíveis como "não disponível"; não force parâmetros incompatíveis.

**Ajustes ao roteiro:** temperatura zero não é garantia de respostas idênticas nem de exatidão. Top-K = 1 corresponde à escolha do token mais provável, mas a repetibilidade deve ser observada. A faixa de Top-K não é universalmente 1–40. A documentação atual desaconselha alterar temperatura, Top-P e Top-K nos Gemini 3.x; use um modelo compatível com o objetivo didático ou registre essa limitação.

## 4. Thinking e Compare

```text
Um fazendeiro precisa atravessar um rio com um lobo, uma cabra e um repolho.
O barco leva o fazendeiro e mais um item. Sem o fazendeiro, o lobo come a
cabra e a cabra come o repolho. Liste as travessias e os itens em cada margem
após cada viagem. Verifique se alguma restrição foi violada.
```

Compare níveis de thinking suportados, mantendo o restante fixo. Avalie a solução e a latência; uma seção de Thoughts pode ser um resumo, não um registro completo do raciocínio interno. No Compare, altere apenas modelo OU parâmetro por comparação. Use `gemini-3.5-flash-lite` como modelo padrão dos próximos exercícios, conforme escolha de 17/09/2026. Confira sempre a disponibilidade na sua conta.

## 5. Ferramentas — testar uma de cada vez

| Recurso | Prompt | Como conferir |
| --- | --- | --- |
| Google Search | Considerando a data de hoje, quando ocorreu o último Gre-Nal, quem ganhou e qual foi o placar? Informe data e fontes. | Compare busca desligada/ligada; abra as fontes e confira as datas. |
| Code Execution | Calcule 84938291 × 72918471 usando Python e mostre o resultado exato. | Confira o código executado e compare com uma multiplicação local. A execução não garante que o código esteja correto. |
| URL Context | Leia https://ai.google.dev/gemini-api/docs/ai-studio-quickstart e resuma três recursos descritos, indicando a fonte. | Verifique se a página foi acessada e se o resumo corresponde a ela. |
| Google Maps | Localize três cafés próximos ao Tecnopuc, em Porto Alegre, e informe endereços e fontes. | Se disponível para o modelo, confira estabelecimentos e localização nos links. |

Para multimodalidade, anexe um PDF ou imagem de estudo sem dados pessoais e peça uma extração curta que você consiga conferir manualmente.

## 6. Safety Settings e Get Code

Inspecione as categorias e os controles disponíveis. Para observar possíveis falsos positivos, use um pedido benigno, como: "Explique como reconhecer e denunciar assédio em um fórum de estudos, sem reproduzir insultos". Registre a configuração e se houve bloqueio.

Ao terminar um teste, use Get Code → Python, se disponível. Confira o SDK `google-genai`, o identificador do modelo e os parâmetros exportados. Remova qualquer chave literal antes de salvar o código. A execução local fica para a etapa seguinte, após verificar o Python e configurar a chave.

## Referências oficiais

- [AI Studio Quickstart](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart)
- [Parâmetros dos modelos](https://ai.google.dev/api/models)
- [Estratégias de prompting](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Mudanças no Gemini 3.5 e parâmetros dos Gemini 3.x](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5)
- [Saída estruturada](https://ai.google.dev/gemini-api/docs/structured-output)

A interface, os modelos e os controles podem variar. Registre o que realmente estiver disponível na sua conta.
