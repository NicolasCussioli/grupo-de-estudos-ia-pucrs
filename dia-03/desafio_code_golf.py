# Adaptado do roteiro de Eduardo de Bastiani, commit 983e935.
# Fonte: https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.runtime import client, MODEL as MODELO_FLASH
import json
import os
from google.genai import types


entrada = "Oi, sou a Mariana, faco o quarto semestre de Engenharia de Software"

# Elabore o prompt mais enxuto possivel aqui:
prompt = f"Extraia JSON {{\"nome\",\"curso\",\"semestre\"}} de: {entrada}"

# 1. Medicao oficial de tokens
tokens = client.models.count_tokens(model=MODELO_FLASH, contents=prompt).total_tokens
print(f"Total de Tokens do Prompt: {tokens}")

# 2. Execucao com retorno estruturado
response = client.models.generate_content(
    model=MODELO_FLASH,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",

    )
)

print(f"\nResposta Bruta:\n{(response.text or "").strip()}")

# Valida formato, campos exatos e valores do desafio.
from estudos.validacao import validar_aluno
dados = validar_aluno(response.text or "")
print(f"Validacao JSON: SUCESSO! {dados}")
