"""Perguntas do roteiro; gabarito conferido no PDF, por indice de pagina."""
import json
import sys
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estudos.busca import abrir_indice, buscar, busca_lexica, ler_paginas, identidade, EMBEDDING_MODEL

CASOS = [
    ('como resetar o relogio para as configuracoes de fabrica', {9}),
    ('posso mergulhar na piscina ou tomar banho com o relogio?', {9}),
    ('qual o aplicativo que devo baixar no celular para conectar?', {6}),
    ('qual a capacidade da bateria em mAh e como carrega?', {4, 11}),
    ('como limpar o relogio se sujar de suor no treino?', {8}),
    ('a tela travou e nao responde ao toque, o que fazer?', {8}),
]


if __name__ == '__main__':
    collection = abrir_indice()
    paginas, _ = ler_paginas()
    dados = []
    for query, expected in CASOS:
        hits = buscar(query, collection)
        lexical = busca_lexica(query, paginas)
        found = [h['pagina'] for h in hits]
        row = {'pergunta': query, 'paginas_relevantes': sorted(expected),
               'semantica': [{k: v for k, v in h.items() if k != 'texto'} for h in hits], 'lexica': lexical,
               'semantica_hit1': found[0] in expected,
               'semantica_hit2': bool(set(found) & expected),
               'lexica_hit2': bool({h['pagina'] for h in lexical} & expected),
               'cobertura_paginas_top2': len(set(found) & expected) / len(expected)}
        dados.append(row)
        print(f'{query}\n  Esperadas: {sorted(expected)}; semantica: {found}; lexica: {[h["pagina"] for h in lexical]}')
    for key in ['semantica_hit1', 'semantica_hit2', 'lexica_hit2']:
        print(f'{key}: {sum(r[key] for r in dados)}/{len(dados)}')
    # Consulta fora do escopo: o banco ainda devolve vizinhos, sem validar a resposta.
    negativa = buscar('Como preparar bolo de chocolate?', collection)
    print('Fora de escopo: paginas retornadas', [h['pagina'] for h in negativa])
    print('Nao ha receita no manual; vizinho mais proximo nao significa resposta valida.')
    folder = Path(__file__).resolve().parent / 'resultados'
    folder.mkdir(exist_ok=True)
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    report = {'modelo': EMBEDDING_MODEL, 'indice': identidade()[0], 'casos': dados,
              'fora_de_escopo': [{k: v for k, v in h.items() if k != 'texto'} for h in negativa]}
    (folder / f'avaliacao-{stamp}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
