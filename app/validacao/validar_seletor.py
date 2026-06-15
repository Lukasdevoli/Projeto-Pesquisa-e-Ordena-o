from analizador.caracteristicas import AnalisadorCaracteristicas
from analizador.motor_decisao import MotorDecisao

from utils.gerador import gerar_aleatorio
from utils.benchmark import Benchmark

from algoritimos.ordenacao import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort
)


class Validador:

    ALGORITMOS = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort
    }

    def gerar_requisitos(self, tamanho):

        return {
            "quantidade_elementos": tamanho,
            "parcialmente_ordenado": False,
            "muitos_repetidos": False,
            "estabilidade": False,
            "memoria_limitada": False,
            "operacao": "ordenar"
        }

    def validar(self):

        cenarios = [
            100,
            500,
            1000,
            5000,
            10000
        ]

        total = 0
        acertos = 0

        motor = MotorDecisao()

        for tamanho in cenarios:

            dados = gerar_aleatorio(tamanho)

            analisador = AnalisadorCaracteristicas(
                dados
            )

            caracteristicas = analisador.analisar()

            requisitos = self.gerar_requisitos(
                tamanho
            )

            recomendado, _ = motor.recomendar(
                caracteristicas,
                requisitos
            )

            tempos = {}

            for nome, algoritmo in self.ALGORITMOS.items():

                resultado = Benchmark.medir(
                    algoritmo,
                    dados
                )

                tempos[nome] = resultado["tempo"]

                ordenado = resultado["resultado"]

                if ordenado != sorted(dados):

                    print(
                        f"ERRO: {nome} não ordenou corretamente."
                    )

            ranking_real = sorted(
                tempos.items(),
                key=lambda item: item[1]
            )

            top2 = [
                ranking_real[0][0],
                ranking_real[1][0]
            ]

            total += 1

            if recomendado in top2:
                acertos += 1

            print("\n" + "=" * 50)
            print(f"CENÁRIO: {tamanho} elementos")
            print("=" * 50)

            print(
                f"Recomendado: {recomendado}"
            )

            print(
                f"Top 2 reais: {top2}"
            )

            print(
                f"Acertou: {recomendado in top2}"
            )

        percentual = round(
            (acertos / total) * 100,
            2
        )

        return percentual