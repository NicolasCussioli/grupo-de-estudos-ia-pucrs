# Adaptado do roteiro de Eduardo de Bastiani, commit 983e935.
# Fonte: https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.runtime import client, MODEL as MODELO_FLASH
import os



textos = {
    "Ingles": "Artificial Intelligence is transforming how we build software systems and interact with data.",
    "Portugues": "A Inteligência Artificial está transformando a forma como construímos sistemas de software e interagimos com dados.",
    "Codigo Python": """
def calcular_media(valores: list[float]) -> float:
    if not valores:
        return 0.0
    return sum(valores) / len(valores)
"""
}

print(f"{'Categoria':<15} | {'Caracteres':<12} | {'Palavras':<10} | {'Tokens':<8} | {'Razao Token/Palavra'}")
print("-" * 70)

for categoria, texto in textos.items():
    res = client.models.count_tokens(model=MODELO_FLASH, contents=texto)
    qtd_chars = len(texto)
    qtd_palavras = len(texto.split())
    qtd_tokens = res.total_tokens
    razao = qtd_tokens / max(qtd_palavras, 1)
    print(f"{categoria:<15} | {qtd_chars:<12} | {qtd_palavras:<10} | {qtd_tokens:<8} | {razao:.2f}")
