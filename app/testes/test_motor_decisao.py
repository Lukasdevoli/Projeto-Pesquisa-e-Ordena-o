import unittest
from app.analizador.motor_decisao import MotorDecisao

class TestMotorDecisao(unittest.TestCase):
    """Testa a lógica de recomendação"""
    
    def setUp(self):
        self.motor = MotorDecisao()
    
    # Helper características padrão
    def make_caracteristicas(self, tamanho=100, grau_ordenacao=50, duplicatas=10):
        """Factory para criar características de forma fácil"""
        return {
            "tamanho": tamanho,
            "tipo": "int",
            "amplitude": 10000,
            "duplicatas": duplicatas,
            "grau_ordenacao": grau_ordenacao
        }
    
    def make_requisitos(self, tamanho=100, operacao="ordenar", **kwargs):
        """Factory pra requisitos"""
        req = {
            "quantidade_elementos": tamanho,
            "parcialmente_ordenado": kwargs.get("parcialmente_ordenado", False),
            "muitos_repetidos": kwargs.get("muitos_repetidos", False),
            "estabilidade": kwargs.get("estabilidade", False),
            "memoria_limitada": kwargs.get("memoria_limitada", False),
            "operacao": operacao
        }
        return req
    
    # TESTES DE SAIDA
    def test_retorna_tupla(self):
        """recomendar() deve retornar (algoritmo, scores)"""
        car = self.make_caracteristicas()
        req = self.make_requisitos()
        
        resultado = self.motor.recomendar(car, req)
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)
    
    def test_recomendacao_valida(self):
        """Deve recomendar um algoritmo válido"""
        car = self.make_caracteristicas(tamanho=100)
        req = self.make_requisitos(tamanho=100)
        
        algoritmo, scores = self.motor.recomendar(car, req)
        algoritmos_validos = [
            "Bubble Sort", "Selection Sort", "Insertion Sort",
            "Merge Sort", "Quick Sort", "Heap Sort"
        ]
        self.assertIn(algoritmo, algoritmos_validos)
    
    #  TESTES DE LOGICA
    def test_dataset_muito_grande(self):
        """Com tamanho > 10000, deve evitar O(n²)"""
        car = self.make_caracteristicas(tamanho=50000)
        req = self.make_requisitos(tamanho=50000)
        
        algoritmo, scores = self.motor.recomendar(car, req)
        
        # Bubble, Selection, Insertion devem ter score muito baixo
        self.assertLess(scores["Bubble Sort"], 0)
        self.assertLess(scores["Selection Sort"], 0)
        self.assertLess(scores["Insertion Sort"], 0)
        
        # Deve recomendar algo eficiente
        self.assertIn(algoritmo, ["Merge Sort", "Quick Sort", "Heap Sort"])
    
    #  TESTES DE LOGICA: DADOS ORDENADOS
    def test_dados_parcialmente_ordenados(self):
        """Se parcialmente_ordenado=True, Insertion Sort recebe bonus"""
        car = self.make_caracteristicas(tamanho=100, grau_ordenacao=80)
        req = self.make_requisitos(tamanho=100, parcialmente_ordenado=True)
        
        _, scores = self.motor.recomendar(car, req)
        
        # Score de Insertion Sort deve ser boosted
        self.assertGreater(
            scores["Insertion Sort"], 
            50,
            f"Insertion Sort score: {scores['Insertion Sort']}, esperado > 50"
        )
    
    #  TESTES DE LOGICA: ESTABILIDADE
    def test_requisito_estabilidade(self):
        """Se estabilidade=True, Merge/Insertion ganham, Quick/Heap perdem"""
        car = self.make_caracteristicas()
        req = self.make_requisitos(estabilidade=True)
        
        _, scores = self.motor.recomendar(car, req)
        
        # Merge e Insertion devem ganhar de Quick e Heap
        self.assertGreater(
            scores["Merge Sort"],
            scores["Quick Sort"],
            "Merge Sort deve ganhar de Quick Sort com estabilidade"
        )
        self.assertGreater(
            scores["Insertion Sort"],
            scores["Heap Sort"],
            "Insertion Sort deve ganhar de Heap Sort com estabilidade"
        )
    
    #  TESTES DE LOGICA: MEMÓRIA
    def test_memoria_limitada(self):
        """Se memoria_limitada=True, Heap ganha de Merge"""
        car = self.make_caracteristicas(tamanho=1000)
        req = self.make_requisitos(tamanho=1000, memoria_limitada=True)
        
        _, scores = self.motor.recomendar(car, req)
        
        # Heap Sort (O(1) espaço) > Merge Sort (O(n) espaço)
        self.assertGreater(
            scores["Heap Sort"],
            scores["Merge Sort"],
            "Heap Sort deve ganhar de Merge Sort com memória limitada"
        )
    
    #  TESTES DE LOGICA: DUPLICATAS
    def test_muitos_repetidos(self):
        """Se muitos_repetidos, Merge Sort recebe bonus"""
        car = self.make_caracteristicas(duplicatas=70)
        req = self.make_requisitos(muitos_repetidos=True)
        
        _, scores = self.motor.recomendar(car, req)
        
        # Merge Sort deve ter bonus
        self.assertGreater(
            scores["Merge Sort"],
            50,
            f"Merge Sort score com duplicatas: {scores['Merge Sort']}, esperado > 50"
        )
    
    #  TESTES DE BUSCA
    def test_operacao_buscar(self):
        """Com operacao='buscar', retorna algoritmos de busca"""
        car = self.make_caracteristicas()
        req = self.make_requisitos(operacao="buscar", tamanho=100)
        
        algoritmo, scores = self.motor.recomendar(car, req)
        
        buscas_validas = ["Busca Sequencial", "Busca Binária", "Busca Hash"]
        self.assertIn(algoritmo, buscas_validas)
        self.assertIn("Busca Sequencial", scores)
    
    def test_busca_grande_dataset(self):
        """Busca em dataset > 1000 deve preferir Binária/Hash"""
        car = self.make_caracteristicas(tamanho=100000)
        req = self.make_requisitos(operacao="buscar", tamanho=100000)
        
        _, scores = self.motor.recomendar(car, req)
        
        # Busca Sequencial deve ser penalizada
        self.assertLess(
            scores["Busca Sequencial"],
            scores["Busca Binária"],
            "Busca Binária deve ganhar de Sequencial em dataset grande"
        )
    
    #  TESTES DE DADOS PEQUENOS
    def test_dados_muito_pequenos(self):
        """Dados pequenos (< 50): algoritmos simples são aceitáveis"""
        car = self.make_caracteristicas(tamanho=20)
        req = self.make_requisitos(tamanho=20)
        
        _, scores = self.motor.recomendar(car, req)
        
        # Insertion e Bubble devem ter bonus
        self.assertGreater(scores["Insertion Sort"], 50)


class TestMotorDecisaoRegressao(unittest.TestCase):
    """Testa casos específicos para evitar regressões"""
    
    def setUp(self):
        self.motor = MotorDecisao()
    
    def make_caracteristicas(self, tamanho=100, grau_ordenacao=50, duplicatas=10):
        return {
            "tamanho": tamanho,
            "tipo": "int",
            "amplitude": 10000,
            "duplicatas": duplicatas,
            "grau_ordenacao": grau_ordenacao
        }
    
    def make_requisitos(self, tamanho=100, operacao="ordenar", **kwargs):
        return {
            "quantidade_elementos": tamanho,
            "parcialmente_ordenado": kwargs.get("parcialmente_ordenado", False),
            "muitos_repetidos": kwargs.get("muitos_repetidos", False),
            "estabilidade": kwargs.get("estabilidade", False),
            "memoria_limitada": kwargs.get("memoria_limitada", False),
            "operacao": operacao
        }
    
    def test_cenario_dados_pequenos_parcialmente_ordenados(self):
        """Insertion Sort para dados pequenos parcialmente ordenados"""
        car = self.make_caracteristicas(tamanho=30, grau_ordenacao=75)
        req = self.make_requisitos(tamanho=30, parcialmente_ordenado=True)
        
        algoritmo, _ = self.motor.recomendar(car, req)
        # Pode ser Insertion, Bubble ou Selection
        self.assertIn(
            algoritmo, 
            ["Insertion Sort", "Bubble Sort", "Selection Sort"],
            f"Pra dados pequenos parcialmente ordenados, esperava algoritmo simples, got {algoritmo}"
        )
    
    def test_cenario_dados_grandes_nao_ordenados(self):
        """Para dados grandes não-ordenados, prefere Quick/Merge"""
        car = self.make_caracteristicas(tamanho=50000, grau_ordenacao=20)
        req = self.make_requisitos(tamanho=50000)
        
        algoritmo, _ = self.motor.recomendar(car, req)
        self.assertIn(
            algoritmo,
            ["Quick Sort", "Merge Sort", "Heap Sort"],
            f"Pra dados grandes, esperava algoritmo eficiente, got {algoritmo}"
        )


if __name__ == "__main__":
    unittest.main()