import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.busca import embedding, similaridade_cosseno

if __name__ == '__main__':
    textos = ['como resetar o relogio para as configuracoes de fabrica',
              'restaurar padroes de fabrica e apagar todos os dados',
              'receita de bolo de chocolate com cobertura de morango']
    vetores = [embedding(texto, 'SEMANTIC_SIMILARITY') for texto in textos]
    print('Textos:', textos)
    print(f'Mesmo tema: {similaridade_cosseno(vetores[0], vetores[1]):.4f}')
    print(f'Temas diferentes: {similaridade_cosseno(vetores[0], vetores[2]):.4f}')
    print('Escala de -1 a 1; nao representa porcentagem de certeza.')
