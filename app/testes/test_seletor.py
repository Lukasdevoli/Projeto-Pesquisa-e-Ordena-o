import unittest
from app.validacao.validar_seletor import Validador


class TesteSeletorCompleto(unittest.TestCase):
    """Testa o seletor de algoritmos"""
    
    def test_recomendacao_entre_top2_baseline(self):
        """Taxa mínima: 40% (baseline) com seed para reproduzibilidade"""
        validador = Validador()
        # Usamos seed pra ter dados iguais
        taxa = validador.validar(seed=42)
        self.assertGreaterEqual(taxa, 40, 
            f"Taxa de acertos ({taxa}%) deve ser >= 40% (baseline)")
    
    def test_recomendacao_entre_top2_padrao(self):
        """Taxa mínima: 50% (meta)"""
        validador = Validador()
        taxa = validador.validar(seed=123)
        self.assertGreaterEqual(taxa, 50, 
            f"Taxa de acertos ({taxa}%) deve ser >= 50%")
    
    def test_recomendacao_entre_top2_otimizado(self):
        """Taxa mínima: 60% (depois de melhorias)"""
        validador = Validador()
        taxa = validador.validar(seed=999) 
        self.assertGreaterEqual(taxa, 60,
            f"Taxa de acertos ({taxa}%) deve ser >= 60% após otimizações")


if __name__ == "__main__":
    unittest.main()