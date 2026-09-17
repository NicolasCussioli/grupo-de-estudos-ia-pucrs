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



prompt = "Crie uma metafora curta e poetica para explicar o que e uma funcao recursiva na programacao."
temperaturas = [0.0, 0.7, 1.5]

print(f"Prompt Testado: '{prompt}'\n")

for temp in temperaturas:
    print(f"\n" + "=" * 50)
    print(f"EXPERIMENTO COM TEMPERATURA = {temp}")
    print("=" * 50)

    # Executar 2 vezes para verificar determinismo vs aleatoriedade
    for tentativa in range(1, 3):
        response = client.models.generate_content(
            model=MODELO_FLASH,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temp,
                max_output_tokens=150
            )
        )
        print(f"\n[Tentativa {tentativa}]:")
        print((response.text or "").strip())
