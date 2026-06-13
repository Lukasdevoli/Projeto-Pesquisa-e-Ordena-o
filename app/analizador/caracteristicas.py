import random

class AnalisadorCaracteristicas:

    def __init__(self, dados):
        self.dados = dados

    def analisar_tamanho(self):

        return len(self.dados)

    def analisar_tipo(self):

        if not self.dados:
            return "vazio"

        return type(self.dados[0]).__name__

    def analisar_amplitude(self):

        if not self.dados:
            return 0

        return max(self.dados) - min(self.dados)

    def analisar_duplicatas(self):

        if not self.dados:
            return 0

        total = len(self.dados)
        unicos = len(set(self.dados))

        return round(
            (1 - unicos / total) * 100,
            2
        )

    def analisar_grau_ordenacao(self):

        n = len(self.dados)

        if n < 2:
            return 100.0

        # Arrays pequenos: conta todas as inversões
        if n <= 1000:

            inversoes = 0
            max_inversoes = n * (n - 1) / 2

            for i in range(n):
                for j in range(i + 1, n):

                    if self.dados[i] > self.dados[j]:
                        inversoes += 1

            percentual = (
                1 - (inversoes / max_inversoes)
            ) * 100

            return round(percentual, 2)

        # Arrays grandes: usa amostragem aleatória
        amostras = min(10000, n * 2)

        inversoes = 0

        for _ in range(amostras):

            i = random.randint(0, n - 2)
            j = random.randint(i + 1, n - 1)

            if self.dados[i] > self.dados[j]:
                inversoes += 1

        percentual = (
            1 - (inversoes / amostras)
        ) * 100

        return round(percentual, 2)

    def analisar(self):

        return {
            "tamanho": self.analisar_tamanho(),
            "tipo": self.analisar_tipo(),
            "amplitude": self.analisar_amplitude(),
            "duplicatas": self.analisar_duplicatas(),
            "grau_ordenacao": self.analisar_grau_ordenacao()
        }