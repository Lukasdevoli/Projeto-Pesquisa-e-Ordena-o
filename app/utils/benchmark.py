import time
import tracemalloc


class Benchmark:

    @staticmethod
    def medir(funcao, dados):

        copia = dados.copy()

        tracemalloc.start()

        inicio = time.perf_counter()

        resultado = funcao(copia)

        fim = time.perf_counter()

        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        return {
            "tempo": fim - inicio,
            "memoria_atual_bytes": memoria_atual,
            "memoria_pico_bytes": memoria_pico,
            "resultado": resultado
        }