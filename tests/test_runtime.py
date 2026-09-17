import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch
from google.genai import errors
from estudos.runtime import Models


class RetryTest(unittest.TestCase):
    def test_repete_503_e_retorna_sucesso(self):
        models = Models()
        method = Mock(side_effect=[errors.APIError(503, {'message': 'indisponivel'}), 'ok'])
        models._client = SimpleNamespace(models=SimpleNamespace(count_tokens=method))
        with patch('estudos.runtime.time.sleep') as sleep:
            self.assertEqual(models.count_tokens(model='teste', contents='oi'), 'ok')
            sleep.assert_called_once_with(2)
        self.assertEqual(method.call_count, 2)

    def test_cota_nao_dispara_repeticao(self):
        models = Models()
        method = Mock(side_effect=errors.APIError(429, {'message': 'cota'}))
        models._client = SimpleNamespace(models=SimpleNamespace(count_tokens=method))
        with self.assertRaises(errors.APIError):
            models.count_tokens(model='teste', contents='oi')
        self.assertEqual(method.call_count, 1)

    def test_limite_de_tres_tentativas(self):
        models = Models()
        method = Mock(side_effect=errors.APIError(503, {'message': 'indisponivel'}))
        models._client = SimpleNamespace(models=SimpleNamespace(count_tokens=method))
        with patch('estudos.runtime.time.sleep'), self.assertRaises(errors.APIError):
            models.count_tokens(model='teste', contents='oi')
        self.assertEqual(method.call_count, 3)
