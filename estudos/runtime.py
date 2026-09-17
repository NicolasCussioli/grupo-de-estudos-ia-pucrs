"""Configuração local e chamadas limitadas, sem imprimir credenciais."""
import os
from pathlib import Path
import sys
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(ROOT / '.env', override=False)
MODEL = os.getenv('GEMINI_MODEL', 'gemini-3.5-flash-lite').strip()


def erro_seguro(tipo, valor, traceback):
    # Não imprime URLs, headers, corpos de resposta ou variáveis locais.
    code = getattr(valor, 'code', None)
    print(f'Falha: {tipo.__name__}' + (f' (HTTP {code})' if code else ''), file=sys.stderr)
    dicas = {400: 'Confira os parametros e a configuracao da chave.',
             401: 'Confira a chave local.', 403: 'Confira as permissoes do projeto.',
             404: 'Confira o identificador e a disponibilidade do modelo.',
             429: 'Cota ou limite atingido. Confira o painel antes de repetir.',
             503: 'Servico indisponivel apos tentativas limitadas; tente mais tarde.'}
    print(dicas.get(code, 'Confira configuracao local, conectividade e disponibilidade da API.'), file=sys.stderr)


sys.excepthook = erro_seguro


class Models:
    def __init__(self):
        self._client = None

    def call(self, method, **kwargs):
        if self._client is None:
            key = os.getenv('GEMINI_API_KEY', '').strip()
            if not key:
                raise ValueError('Preencha GEMINI_API_KEY na .env.')
            self._client = genai.Client(api_key=key, http_options=types.HttpOptions(
                timeout=30000, retry_options=types.HttpRetryOptions(attempts=1)))
        for attempt in range(3):
            try:
                result = getattr(self._client.models, method)(**kwargs)
                if method == 'generate_content' and not result.text:
                    raise ValueError('Resposta sem texto; verifique limite de saída ou bloqueio.')
                return result
            except errors.APIError as exc:
                if exc.code not in {500, 502, 503, 504} or attempt == 2:
                    raise
                print(f'HTTP {exc.code}; nova tentativa em {2 ** (attempt + 1)}s.')
                time.sleep(2 ** (attempt + 1))

    def generate_content(self, **kwargs):
        config = kwargs.get('config') or types.GenerateContentConfig()
        if config.max_output_tokens is None:
            config.max_output_tokens = 2048
        kwargs['config'] = config
        if config.automatic_function_calling is None:
            config.automatic_function_calling = types.AutomaticFunctionCallingConfig(disable=True)
        return self.call('generate_content', **kwargs)

    def count_tokens(self, **kwargs):
        return self.call('count_tokens', **kwargs)


class Client:
    def __init__(self):
        self.models = Models()


client = Client()
