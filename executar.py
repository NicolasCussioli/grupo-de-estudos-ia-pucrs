"""Executa um exercício e guarda sua saída UTF-8 sem copiar a .env."""
import argparse
from datetime import datetime
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
parser = argparse.ArgumentParser()
parser.add_argument('script', help='Exemplo: dia-03/01_hello_gemini.py')
parser.add_argument('args', nargs=argparse.REMAINDER)
args = parser.parse_args()
script = (ROOT / args.script).resolve()
if script.parent not in [ROOT / 'dia-03', ROOT / 'dia-04'] or script.suffix != '.py' or not script.is_file():
    parser.error('Escolha um script existente de dia-03 ou dia-04.')
env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
run = subprocess.run([sys.executable, str(script), *args.args], cwd=ROOT, env=env,
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
# Redação defensiva também no arquivo de resultado.
from dotenv import dotenv_values
settings = dotenv_values(ROOT / '.env')
key = settings.get('GEMINI_API_KEY')
model = os.getenv('GEMINI_MODEL') or settings.get('GEMINI_MODEL') or 'gemini-3.5-flash-lite'
output = run.stdout
for secret in {key, os.getenv('GEMINI_API_KEY')} - {None, ''}:
    output = output.replace(secret, '[CHAVE OMITIDA]')
folder = script.parent / 'resultados'
folder.mkdir(exist_ok=True)
stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
path = folder / f'{script.stem}-{stamp}.txt'
path.write_text(f'Script: {args.script}\nModelo configurado: {model}\nData local: {stamp}\nExit code: {run.returncode}\n\n{output}', encoding='utf-8')
print(output)
print(f'Registro: {path.relative_to(ROOT)}')
sys.exit(run.returncode)
