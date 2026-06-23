import unittest
from app.analizador.caracteristicas import AnalisadorCaracteristicas

class TestAnalisadorCaracteristicas(unittest.TestCase):
    """Testa se as métricas são extraídas corretamente"""
    
    def test_tamanho(self):
        """Deve contar elementos corretamente"""
        dados = [1, 2, 3, 4, 5]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_tamanho(), 5)
    
    def test_duplicatas_nenhuma(self):
        """Com elementos únicos, duplicatas = 0%"""
        dados = [1, 2, 3, 4, 5]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_duplicatas(), 0.0)
    
    def test_duplicatas_todas(self):
        """Com todos iguais, duplicatas = 80%"""
        dados = [5, 5, 5, 5, 5]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_duplicatas(), 80.0)
    
    def test_duplicatas_parcial(self):
        """Com 50% iguais: [1, 1, 2, 2] → 50%"""
        dados = [1, 1, 2, 2]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_duplicatas(), 50.0)
    
    def test_grau_ordenacao_totalmente_ordenado(self):
        """Lista ordenada deve ter grau 100%"""
        dados = [1, 2, 3, 4, 5]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_grau_ordenacao(), 100.0)
    
    def test_grau_ordenacao_totalmente_desordenado(self):
        """Lista inversa deve ter grau ~0%"""
        dados = [5, 4, 3, 2, 1]
        analisador = AnalisadorCaracteristicas(dados)
        ordenacao = analisador.analisar_grau_ordenacao()
        self.assertLess(ordenacao, 5.0)  # Próximo de 0
    
    def test_amplitude(self):
        """Amplitude = max - min"""
        dados = [10, 5, 20, 15]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_amplitude(), 15)  # 20 - 5
    
    def test_amplitude_zero(self):
        """Elementos iguais → amplitude 0"""
        dados = [7, 7, 7, 7]
        analisador = AnalisadorCaracteristicas(dados)
        self.assertEqual(analisador.analisar_amplitude(), 0)
    
    def test_tipo(self):
        """Deve identificar o tipo dos dados"""
        int_data = [1, 2, 3]
        analisador = AnalisadorCaracteristicas(int_data)
        self.assertEqual(analisador.analisar_tipo(), "int")
    
    def test_analise_completa(self):
        """Método analisar() retorna dicionário completo"""
        dados = [3, 1, 2, 1, 3]
        analisador = AnalisadorCaracteristicas(dados)
        resultado = analisador.analisar()
        
        self.assertIn("tamanho", resultado)
        self.assertIn("tipo", resultado)
        self.assertIn("amplitude", resultado)
        self.assertIn("duplicatas", resultado)
        self.assertIn("grau_ordenacao", resultado)
        
        self.assertEqual(resultado["tamanho"], 5)