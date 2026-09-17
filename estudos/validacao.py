import json
import re


def categoria(texto):
    """Aceita apenas uma categoria isolada ou uma linha final explícita."""
    texto = texto.strip().upper()
    if texto in {"ALTA", "MEDIA", "BAIXA"}:
        return texto
    linha = texto.splitlines()[-1] if texto else ""
    match = re.fullmatch(r"URG[EÊ]NCIA:\s*(ALTA|MEDIA|BAIXA)", linha)
    return match.group(1) if match else "DESCONHECIDO"


def validar_aluno(texto):
    dados = json.loads(texto)
    if not isinstance(dados, dict) or set(dados) != {"nome", "curso", "semestre"}:
        raise ValueError("O JSON deve conter exatamente nome, curso e semestre.")
    if dados['nome'] != 'Mariana' or dados['curso'] != 'Engenharia de Software':
        raise ValueError("Nome ou curso incorreto.")
    if not ((type(dados['semestre']) is int and dados['semestre'] == 4) or dados['semestre'] == 'quarto'):
        raise ValueError("Semestre incorreto.")
    return dados


def normalizar(texto):
    return re.sub(r'[^A-Za-z0-9]', '', texto).upper()


def filtrar_saida(texto, segredo):
    """Filtro didático: cobre segredo literal e separadores; não toda codificação."""
    if normalizar(segredo) in normalizar(texto):
        return '[BLOQUEADO PELO FILTRO DE SAIDA]'
    return texto


def sanitizar_entrada(texto):
    return re.sub(r'<\s*/?\s*user_query\s*>', '', texto, flags=re.I)
