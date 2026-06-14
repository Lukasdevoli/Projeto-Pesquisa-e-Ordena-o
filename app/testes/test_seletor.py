import unittest

from validacao.validar_seletor import Validador


class TesteSeletor(unittest.TestCase):

    def test_recomendacao_entre_top2(self):

        validador = Validador()

        taxa = validador.validar()

        self.assertGreaterEqual(
            taxa,
            50
        )


if __name__ == "__main__":
    unittest.main()