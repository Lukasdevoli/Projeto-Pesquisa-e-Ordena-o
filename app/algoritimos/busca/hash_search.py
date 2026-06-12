class HashTable:
    """Classe hash para registro e busca de dados"""

    def __init__(self, tamanho: int = 10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hashify(self, valor: int):
        """Metodo para encontrar posicao na tabela"""

        return valor % self.tamanho

    def inserir(self, valor: int):
        """Insere valor na tabela Hash"""

        indice = self._hashify(valor)
        self.tabela[indice].append(valor)

    def inserir_lista(self, lista: list[int]):

        for valor in lista:
            self.inserir(valor)

    def buscar(self, alvo: int):
        """Busca valor na tabela"""

        indice = self._hashify(alvo)

        if alvo in self.tabela[indice]:
            return indice

        return -1
    

"""Uso pratico da criacao e busca"""
if __name__ == "__main__":
    
    # Cria objeto HashTable
    hash_table = HashTable()

    # For loop para inserir cada elemento da lista
    hash_table.inserir_lista([12, 22, 32, 42])

    print(hash_table.tabela)

    print(hash_table.buscar(32))
    print(hash_table.buscar(99))
