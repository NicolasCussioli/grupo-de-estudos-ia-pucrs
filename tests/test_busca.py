import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from estudos.busca import (similaridade_cosseno, normalizar_vetor, busca_lexica,
                           indexar, abrir_indice, buscar, identidade)


class VetoresTest(unittest.TestCase):
    def test_cosseno_e_validacao(self):
        self.assertAlmostEqual(similaridade_cosseno([1, 0], [2, 0]), 1)
        self.assertAlmostEqual(similaridade_cosseno([1, 0], [0, 1]), 0)
        self.assertAlmostEqual(similaridade_cosseno([1, 0], [-1, 0]), -1)
        for a, b in [([0, 0], [1, 0]), ([1], [1, 2]), ([math.nan], [1]), ([], [])]:
            with self.assertRaises(ValueError):
                similaridade_cosseno(a, b)

    def test_lexica_palavra_inteira_e_acentos(self):
        docs = [{'pagina': 1, 'texto': 'Bateria e fábrica.'},
                {'pagina': 2, 'texto': 'Fabricação de carregadores.'}]
        self.assertEqual(busca_lexica('fabrica?', docs), [{'pagina': 1, 'termos_encontrados': 1}])
        self.assertEqual(busca_lexica('como o que?', docs), [])
        self.assertEqual(busca_lexica('bateria', docs)[0]['pagina'], 1)


class IndiceTest(unittest.TestCase):
    def test_persistencia_reexecucao_e_indice_incompleto(self):
        # Chroma real com dados sintéticos; nenhuma chamada externa.
        temp_root = Path(__file__).resolve().parents[1] / 'tmp' / 'tests'
        temp_root.mkdir(parents=True, exist_ok=True)
        # Chroma pode manter arquivos abertos no Windows ate o processo terminar.
        with tempfile.TemporaryDirectory(dir=temp_root, ignore_cleanup_errors=True) as temp:
            pdf = Path(temp) / 'teste.pdf'
            pdf.write_bytes(b'fixture')
            path = Path(temp) / 'db'
            pages = [{'id': 'pagina_01', 'pagina': 1, 'texto': 'bateria'},
                     {'id': 'pagina_02', 'pagina': 2, 'texto': 'aplicativo'}]
            embed = Mock(side_effect=lambda text, task: [1., 0.] if text == 'bateria' else [0., 1.])
            with patch('estudos.busca.ler_paginas', return_value=(pages, 2)):
                coll = indexar(pdf, path, embed)
                indexar(pdf, path, embed)
                self.assertEqual(embed.call_count, 2)
                reopened = abrir_indice(pdf, path)
                hit = buscar('bateria', reopened, embed, k=5)
                self.assertEqual(hit[0]['pagina'], 1)
                self.assertAlmostEqual(hit[0]['cosseno'], 1., places=5)
                self.assertEqual(len(hit), 2)
                self.assertEqual(embed.call_args.args[1], 'RETRIEVAL_QUERY')
                coll.delete(ids=['pagina_02'])
                with self.assertRaises(ValueError):
                    abrir_indice(pdf, path)
                indexar(pdf, path, embed)
                self.assertEqual(abrir_indice(pdf, path).count(), 2)
            first = identidade(pdf)[0]
            pdf.write_bytes(b'outra versao')
            self.assertNotEqual(first, identidade(pdf)[0])
