"""Dia 5: índice por página, embeddings Google e Chroma local.

Base pedagógica: eduardo-de-bastiani/grupo-de-estudos-ia, commit 983e935.
"""
import hashlib
import math
from pathlib import Path
import re
import unicodedata

import chromadb
from chromadb.config import Settings
from google.genai import types
from pypdf import PdfReader

from estudos.runtime import ROOT, client

EMBEDDING_MODEL = 'gemini-embedding-001'
DIMENSIONS = 768
PDF = ROOT / 'referencias/grupo-de-estudos-ia/sprint_1_fundamentos_rag/data/manual_xiaomi_watch5.pdf'
DB = ROOT / 'dia-05/chroma_data'
POLICY = 'pagina-nfkc-fonttools-v2'


def normalizar_vetor(vetor):
    if not vetor or not all(math.isfinite(x) for x in vetor):
        raise ValueError('Vetor vazio ou nao finito.')
    norma = math.sqrt(sum(x*x for x in vetor))
    if norma == 0:
        raise ValueError('Vetor nulo nao tem direcao.')
    return [x / norma for x in vetor]


def similaridade_cosseno(a, b):
    if len(a) != len(b):
        raise ValueError('Vetores com dimensoes diferentes.')
    a, b = normalizar_vetor(a), normalizar_vetor(b)
    return max(-1.0, min(1.0, sum(x*y for x, y in zip(a, b))))


def embedding(texto, task_type):
    if not texto.strip():
        raise ValueError('Texto vazio.')
    response = client.models.embed_content(model=EMBEDDING_MODEL, contents=texto,
        config=types.EmbedContentConfig(task_type=task_type, output_dimensionality=DIMENSIONS))
    if not response.embeddings or not response.embeddings[0].values:
        raise ValueError('API nao retornou embedding.')
    vetor = response.embeddings[0].values
    if len(vetor) != DIMENSIONS:
        raise ValueError('Dimensao inesperada.')
    return normalizar_vetor(vetor)


def ler_paginas(pdf=PDF):
    pdf = Path(pdf)
    if not pdf.is_file():
        raise FileNotFoundError('Clone o repositorio do professor conforme README.')
    reader = PdfReader(pdf)
    paginas = []
    for numero, page in enumerate(reader.pages, 1):
        texto = unicodedata.normalize('NFKC', page.extract_text() or '').strip()
        if len(texto) > 30:
            paginas.append({'id': f'pagina_{numero:02d}', 'pagina': numero, 'texto': texto})
    if not paginas:
        raise ValueError('PDF sem texto extraivel. OCR nao implementado neste laboratorio.')
    return paginas, len(reader.pages)


def identidade(pdf=PDF):
    digest = hashlib.sha256(Path(pdf).read_bytes()).hexdigest()
    spec = f'{digest}:{EMBEDDING_MODEL}:{DIMENSIONS}:{POLICY}:RETRIEVAL_DOCUMENT'
    name = 'manual_' + hashlib.sha256(spec.encode()).hexdigest()[:24]
    return name, {'source_sha256': digest, 'embedding_model': EMBEDDING_MODEL,
                  'dimensions': DIMENSIONS, 'policy': POLICY}


def banco(path=DB):
    return chromadb.PersistentClient(path=str(path), settings=Settings(anonymized_telemetry=False))


def indexar(pdf=PDF, path=DB, embed=embedding):
    paginas, total = ler_paginas(pdf)
    name, metadata = identidade(pdf)
    collection = banco(path).get_or_create_collection(name=name, embedding_function=None,
        metadata=metadata, configuration={'hnsw': {'space': 'cosine'}})
    existentes = set(collection.get(include=[])['ids'])
    novos = 0
    for pagina in paginas:
        if pagina['id'] in existentes:
            continue
        vetor = embed(pagina['texto'], 'RETRIEVAL_DOCUMENT')
        collection.upsert(ids=[pagina['id']], embeddings=[vetor], documents=[pagina['texto']],
            metadatas=[{'pagina': pagina['pagina'], 'arquivo': Path(pdf).name}])
        novos += 1
        print(f"Indexada pagina PDF {pagina['pagina']:02d}")
    print(f'PDF: {total} paginas; indexadas: {collection.count()}; novas: {novos}.')
    print(f'Colecao: {name}; modelo: {EMBEDDING_MODEL}; dimensoes: {DIMENSIONS}.')
    return collection


def abrir_indice(pdf=PDF, path=DB):
    name, _ = identidade(pdf)
    try:
        collection = banco(path).get_collection(name=name, embedding_function=None)
    except chromadb.errors.NotFoundError:
        raise ValueError('Indice ausente: execute indexar_documentos.py primeiro.') from None
    paginas, _ = ler_paginas(pdf)
    if set(collection.get(include=[])['ids']) != {p['id'] for p in paginas}:
        raise ValueError('Indice incompleto: execute indexar_documentos.py novamente.')
    return collection


def tokens(texto):
    texto = unicodedata.normalize('NFKD', texto.casefold())
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return set(re.findall(r'\w+', texto))


STOPWORDS = set('a o as os de da do das dos e em na no nas nos um uma como qual que para por com se ao ou posso devo meu minha'.split())


def busca_lexica(query, paginas, k=2):
    termos = {t for t in tokens(query) - STOPWORDS if len(t) > 2}
    scores = [(len(termos & tokens(p['texto'])), p['pagina']) for p in paginas]
    return [{'pagina': page, 'termos_encontrados': score}
            for score, page in sorted(scores, key=lambda item: (-item[0], item[1]))[:k] if score]


def buscar(query, collection, embed=embedding, k=2):
    if not query.strip() or k < 1 or collection.count() == 0:
        raise ValueError('Consulta vazia, k invalido ou indice vazio.')
    result = collection.query(query_embeddings=[embed(query, 'RETRIEVAL_QUERY')],
        n_results=min(k, collection.count()), include=['documents', 'metadatas', 'distances'])
    return [{'pagina': meta['pagina'], 'distancia': float(dist), 'cosseno': 1.0-float(dist),
             'texto': text} for text, meta, dist in zip(result['documents'][0], result['metadatas'][0], result['distances'][0])]
