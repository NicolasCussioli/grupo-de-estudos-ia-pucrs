# Adaptado do roteiro de Eduardo de Bastiani, commit 983e935.
# Fonte: https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.runtime import client, MODEL as MODELO_FLASH
import os
import tiktoken


# Inicializar o tokenizador oficial da familia OpenAI (usado no GPT-4)
enc = tiktoken.get_encoding("cl100k_base")

textos = {
    "Ingles": "Artificial Intelligence is transforming how we build software systems and interact with data.",
    "Portugues": "A Inteligência Artificial está transformando a forma como construímos sistemas de software e interagimos com dados.",
    "Codigo Python": """def calcular_media(valores: list[float]) -> float:
    if not valores:
        return 0.0
    return sum(valores) / len(valores)"""
}

print(f"{'Categoria':<15} | {'Tokens Gemini':<15} | {'Tokens Tiktoken':<15} | {'Diferenca'}")
print("-" * 65)

for categoria, texto in textos.items():
    # Contagem no Gemini
    res_gemini = client.models.count_tokens(model=MODELO_FLASH, contents=texto)
    tokens_gemini = res_gemini.total_tokens

    # Contagem no Tiktoken (OpenAI)
    tokens_tiktoken = len(enc.encode(texto))

    diferenca = tokens_gemini - tokens_tiktoken
    print(f"{categoria:<15} | {tokens_gemini:<15} | {tokens_tiktoken:<15} | {diferenca:+d}")

# Inspecao detalhada dos bytes de cada token no tiktoken
exemplo_pt = "inteligencia artificial"
tokens_ids = enc.encode(exemplo_pt)
tokens_bytes = [enc.decode_single_token_bytes(tid) for tid in tokens_ids]

print("\nFatiamento detalhado no tiktoken para 'inteligencia artificial':")
for tid, tbytes in zip(tokens_ids, tokens_bytes):
    print(f"ID {tid:<6}: {tbytes}")
