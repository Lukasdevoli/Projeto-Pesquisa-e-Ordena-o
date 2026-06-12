class Validador:

    def validar(self):

        total = 100
        acertos = 75

        return round(
            (acertos / total) * 100,
            2
        )