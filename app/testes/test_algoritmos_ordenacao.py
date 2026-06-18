import unittest
from app.algoritimos.ordenacao import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort, heap_sort
)
from app.algoritimos.busca.binary_search import binary_search

from typing import Callable, Dict

class TestAlgoritmosOrdenacao(unittest.TestCase):
    """Verifica se cada algoritmo ordena corretamente"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.algoritmos: Dict[str, Callable] = {
            "Bubble": bubble_sort,
            "Selection": selection_sort,
            "Insertion": insertion_sort,
            "Merge": merge_sort,
            "Quick": quick_sort,
            "Heap": heap_sort
        }
    
    #  TESTES BASICOS
    def test_lista_vazia(self):
        """Cada algoritmo deve lidar com lista vazia"""
        for nome, alg in self.algoritmos.items():
            resultado = alg([])
            self.assertEqual(resultado, [], f"{nome} falhou com lista vazia")
    
    def test_um_elemento(self):
        """Cada algoritmo deve retornar [x] para entrada [x]"""
        for nome, alg in self.algoritmos.items():
            resultado = alg([42])
            self.assertEqual(resultado, [42], f"{nome} falhou com 1 elemento")
    
    def test_dois_elementos(self):
        """Testa com dois elementos, ambas ordens"""
        for nome, alg in self.algoritmos.items():
            self.assertEqual(alg([2, 1]), [1, 2], f"{nome} falhou: [2,1]")
            self.assertEqual(alg([1, 2]), [1, 2], f"{nome} falhou: [1,2]")
    
    # TESTES' DADOS COMUNS
    def test_lista_ja_ordenada(self):
        """Algoritmo deve preservar ordem já existente"""
        entrada = [1, 2, 3, 4, 5]
        for nome, alg in self.algoritmos.items():
            resultado = alg(entrada.copy())
            self.assertEqual(resultado, [1, 2, 3, 4, 5], f"{nome} falhou com ordenado")
    
    def test_lista_invertida(self):
        """Algoritmo deve ordenar lista ao contrário"""
        entrada = [5, 4, 3, 2, 1]
        esperado = [1, 2, 3, 4, 5]
        for nome, alg in self.algoritmos.items():
            resultado = alg(entrada.copy())
            self.assertEqual(resultado, esperado, f"{nome} falhou com invertido")
    
    def test_com_duplicatas(self):
        """Algoritmo deve lidar com valores repetidos"""
        entrada = [3, 1, 2, 1, 3, 2, 1]
        esperado = [1, 1, 1, 2, 2, 3, 3]
        for nome, alg in self.algoritmos.items():
            resultado = alg(entrada.copy())
            self.assertEqual(resultado, esperado, f"{nome} falhou com duplicatas")
    
    def test_com_negativos(self):
        """Algoritmo deve lidar com números negativos"""
        entrada = [3, -1, 2, -5, 0]
        esperado = [-5, -1, 0, 2, 3]
        for nome, alg in self.algoritmos.items():
            resultado = alg(entrada.copy())
            self.assertEqual(resultado, esperado, f"{nome} falhou com negativos")
    
    #  TESTES ESTABILIDADE
    def test_estabilidade(self):
        """Verifica se algoritmos estáveis mantêm ordem relativa de iguais"""
        
        # Entrada: (valor, indice_original)
        entrada = [
            (5, 0), 
            (3, 1), 
            (5, 2), 
            (3, 3), 
            (7, 4)
        ]
        
        # Bubble, Insertion, Merge sao estaveis
        algoritmos_estaveis: Dict[str, Callable] = {
            "Insertion": insertion_sort,
            "Merge": merge_sort,
            "Bubble": bubble_sort
        }
        
        for nome, alg in algoritmos_estaveis.items():
            resultado = alg(entrada.copy())
            
            # Extrai índices originais dos elementos com valor 5
            indices_do_5 = [idx for val, idx in resultado if val == 5]
            
            # Se for estavel, os 5s devem manter ordem
            self.assertEqual(
                indices_do_5, 
                [0, 2], 
                f"{nome} nao estável indices: {indices_do_5} esperado: [0, 2]"
            )
            
            # Verifica tambem os 3s
            indices_do_3 = [idx for val, idx in resultado if val == 3]
            self.assertEqual(
                indices_do_3,
                [1, 3],
                f"{nome} nao estável indices: {indices_do_3} esperado: [1, 3]"
            )


class TestAlgoritmosBusca(unittest.TestCase):
    """Testa algoritmos de busca"""
    
    def test_binary_search_encontrado(self):
        """Busca binaria deve encontrar elemento em lista ordenada"""
        lista = [1, 3, 5, 7, 9, 11]
        
        self.assertEqual(binary_search(lista, 5), 2)
        self.assertEqual(binary_search(lista, 1), 0)
        self.assertEqual(binary_search(lista, 11), 5)
    
    def test_binary_search_nao_encontrado(self):
        """Busca binaria retorna -1 se não encontrar"""
        lista = [1, 3, 5, 7, 9]
        
        self.assertEqual(binary_search(lista, 4), -1)
        self.assertEqual(binary_search(lista, 0), -1)
        self.assertEqual(binary_search(lista, 10), -1)
    
    def test_binary_search_lista_vazia(self):
        """Busca binaria em lista vazia retorna -1"""
        self.assertEqual(binary_search([], 5), -1)
    
    def test_binary_search_um_elemento_encontrado(self):
        """Busca binaria com apenas um elemento"""
        self.assertEqual(binary_search([42], 42), 0)
        self.assertEqual(binary_search([42], 10), -1)


if __name__ == "__main__":
    unittest.main()