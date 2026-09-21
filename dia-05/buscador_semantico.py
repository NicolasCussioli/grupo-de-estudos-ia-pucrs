import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.busca import abrir_indice, buscar, busca_lexica, ler_paginas


def mostrar(query, collection, paginas):
    print(f'\nPergunta: {query}')
    print('Busca lexica (contagem de termos, nao BM25):', busca_lexica(query, paginas))
    for hit in buscar(query, collection):
        print(f"\nPagina PDF {hit['pagina']} | cosseno {hit['cosseno']:.4f} (nao e probabilidade)")
        print(hit['texto'])
    print('\nConfira o trecho: ranking sempre retorna vizinhos, mesmo sem resposta no documento.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pergunta')
    args = parser.parse_args()
    collection = abrir_indice()
    paginas, _ = ler_paginas()
    if args.pergunta:
        mostrar(args.pergunta, collection, paginas)
    else:
        while True:
            try:
                query = input('\nPergunta (sair encerra): ').strip()
            except EOFError:
                break
            if query.lower() in {'sair', 'exit', 'quit'}:
                break
            if query:
                mostrar(query, collection, paginas)
