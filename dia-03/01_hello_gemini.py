# Adaptado do roteiro de Eduardo de Bastiani, commit 983e935.
# Fonte: https://github.com/eduardo-de-bastiani/grupo-de-estudos-ia
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.runtime import client, MODEL as MODELO_FLASH
import os

# Carregar credenciais do arquivo .env


# Inicializar o cliente oficial do Google GenAI

# Definir o Modelo Gemini

# Chamada ao Modelo Gemini
response = client.models.generate_content(
    model=MODELO_FLASH,
    contents="Explique em exatamente 2 frases por que entender tokens e importante para um desenvolvedor de software.",
)

print("\n--- Resposta do Gemini ---")
print(response.text)
print("\n--- Metadados de Uso (Tokens) ---")
print(f"Tokens de Entrada (Prompt): {getattr(response.usage_metadata, "prompt_token_count", None)}")
print(f"Tokens de Saida (Resposta): {getattr(response.usage_metadata, "candidates_token_count", None)}")
print(f"Total de Tokens: {getattr(response.usage_metadata, "total_token_count", None)}")
