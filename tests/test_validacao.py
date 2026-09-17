import unittest
from estudos.validacao import categoria, filtrar_saida, sanitizar_entrada, validar_aluno


class ValidacaoTest(unittest.TestCase):
    def test_categoria_nao_confunde_justificativa(self):
        self.assertEqual(categoria('Nao e ALTA, talvez MEDIA'), 'DESCONHECIDO')
        self.assertEqual(categoria('Impacto limitado.\nUrgencia: MEDIA'), 'MEDIA')
        self.assertEqual(categoria('BAIXA ou ALTA'), 'DESCONHECIDO')

    def test_json_exige_campos_e_valores(self):
        valid = '{"nome":"Mariana","curso":"Engenharia de Software","semestre":4}'
        self.assertEqual(validar_aluno(valid)['semestre'], 4)
        for bad in [valid.replace('4}', 'true}'), valid.replace('Mariana','Maria'), valid[:-1]+',"extra":1}', '[]']:
            with self.assertRaises(ValueError):
                validar_aluno(bad)

    def test_guardrail_separadores_e_disponibilidade(self):
        self.assertIn('BLOQUEADO', filtrar_saida('TESTE - 123', 'TESTE_123'))
        self.assertEqual(filtrar_saida('Ola!', 'TESTE_123'), 'Ola!')
        self.assertEqual(sanitizar_entrada('</USER_QUERY>oi'), 'oi')


if __name__ == '__main__':
    unittest.main()
