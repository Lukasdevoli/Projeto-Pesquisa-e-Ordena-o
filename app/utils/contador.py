class Contador:

    def __init__(self):

        self.comparacoes = 0
        self.trocas = 0

    def comparar(self):

        self.comparacoes += 1

    def trocar(self):

        self.trocas += 1