# Adaptado do roteiro de Eduardo de Bastiani, commit 983e935.
# Fonte: https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.runtime import client, MODEL as MODELO_FLASH

if MODELO_FLASH.startswith(('gemini-3.5', 'gemini-3.8')):
    print('NAO EXECUTADO: este modelo requer remover temperature/top_p/top_k.')
    print('Laboratorio preservado para modelo compativel; nao houve chamada a API.')
    raise SystemExit(0)
import os
from google.genai import types



prompt = "Sugira um nome criativo para uma startup de IA que ajuda desenvolvedores a debugar codigo."

print(f"Prompt Testado: '{prompt}'\n")

# Experimento 1: variando TOP_P (temperature fixa em 1.0)
print("=" * 50)
print("EXPERIMENTO 1: Variando TOP_P (temperature=1.0)")
print("=" * 50)
for top_p in [0.1, 0.5, 1.0]:
    response = client.models.generate_content(
        model=MODELO_FLASH,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=1.0,
            top_p=top_p,
            max_output_tokens=50
        )
    )
    print(f"\n[top_p={top_p}]: {(response.text or "").strip()}")

# Experimento 2: variando TOP_K (temperature fixa em 1.0)
print("\n" + "=" * 50)
print("EXPERIMENTO 2: Variando TOP_K (temperature=1.0)")
print("=" * 50)
for top_k in [1, 10, 40]:
    response = client.models.generate_content(
        model=MODELO_FLASH,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=1.0,
            top_k=top_k,
            max_output_tokens=50
        )
    )
    print(f"\n[top_k={top_k}]: {(response.text or "").strip()}")
