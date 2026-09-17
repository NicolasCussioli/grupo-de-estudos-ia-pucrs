# Adaptado do roteiro de Eduardo de Bastiani, commit 983e935.
# Fonte: https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.runtime import client, MODEL as MODELO_FLASH
import os
from google.genai import types



# --- Parte 1: Few-Shot Prompting ---
# Ensinamos o padrao de resposta fornecendo 3 exemplos antes da classificacao real.
prompt_few_shot = """
Classifique a urgencia do chamado de suporte como BAIXA, MEDIA ou ALTA.

Chamado: "O botao de exportar CSV esta com a cor errada."
Urgencia: BAIXA

Chamado: "Nao conseguimos processar pagamentos ha 10 minutos, clientes reclamando."
Urgencia: ALTA

Chamado: "O relatorio mensal demora 5 segundos a mais que o normal para carregar."
Urgencia: MEDIA

Chamado: "O sistema de login caiu para todos os usuarios da empresa."
Urgencia:
"""

response_few_shot = client.models.generate_content(
    model=MODELO_FLASH,
    contents=prompt_few_shot,
)
print("=" * 60)
print("1. FEW-SHOT PROMPTING")
print("=" * 60)
print(f"Resposta do modelo: {(response_few_shot.text or "").strip()}")

# --- Parte 2: Chain-of-Thought (CoT) Classico via Prompt ---
# Nao requer flag na API: a instrucao "Pense passo a passo" guia o raciocinio.
# O texto intermediario vem misturado diretamente em response.text.
prompt_cot = """
Um trio tem 45 tarefas para dividir igualmente entre si na Sprint.
No meio da sprint, 2 integrantes saem de ferias e sobra so 1 pessoa para terminar
o restante das tarefas do trio inteiro. Quantas tarefas essa pessoa vai assumir sozinha?

Pense passo a passo antes de dar a resposta final.
"""

response_cot = client.models.generate_content(
    model=MODELO_FLASH,
    contents=prompt_cot,
)
print("\n" + "=" * 60)
print("2. CHAIN-OF-THOUGHT CLASSICO VIA PROMPT (Sem flags)")
print("=" * 60)
print((response_cot.text or "").strip())

# --- Parte 3: Raciocinio Nativo com ThinkingConfig (Recurso do SDK) ---
# include_thoughts solicita resumos quando disponiveis.
# Nao garante raciocinio correto, nem expoe o processo interno completo.
config_thinking = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
        include_thoughts=True
    ),

)

response_thinking = client.models.generate_content(
    model=MODELO_FLASH,
    contents=prompt_cot,
    config=config_thinking
)

print("\n" + "=" * 60)
print("3. RACIOCINIO NATIVO DA LLM (ThinkingConfig no SDK)")
print("=" * 60)
print(f"Texto da resposta (response.text):\n{(response_thinking.text or "").strip()}")

# Inspecionar resumos opcionais fornecidos pela API
print("\nResumos de pensamento (quando fornecidos) (candidates[0].content.parts):")
parts = (response_thinking.candidates[0].content.parts or []) if response_thinking.candidates and response_thinking.candidates[0].content else []
for i, part in enumerate(parts, 1):
    if getattr(part, "thought", False):
        trecho = (part.text or "").strip().replace("\n", " ")[:160]
        print(f"  [Resumo #{i}]: {trecho}...")

if response_thinking.usage_metadata:
    tokens_pensamento = getattr(response_thinking.usage_metadata, "thoughts_token_count", 0)
    print(f"\nTokens de Pensamento dedicados: {tokens_pensamento}")

print("Observacao: faltam as tarefas ja concluidas; o restante e 45 menos esse total.")
