import time


class Benchmark:

    @staticmethod
    def medir(funcao, dados):

        copia = dados.copy()

        inicio = time.perf_counter()

        resultado = funcao(copia)

        fim = time.perf_counter()

        return {
            "tempo": fim - inicio,
            "resultado": resultado
        }