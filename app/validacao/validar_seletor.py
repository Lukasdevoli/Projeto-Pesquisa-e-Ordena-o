# app/validacao/validar_seletor.py
import random
from app.analizador.caracteristicas import AnalisadorCaracteristicas
from app.analizador.motor_decisao import MotorDecisao
from app.utils.gerador import gerar_aleatorio
from app.utils.benchmark import Benchmark
from app.algoritimos.ordenacao import (
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

    def gerar_requisitos(self, tamanho, caracteristicas):
        """
        Gera requisitos baseado nas caracteristicas dos dados
        """
        return {
            "quantidade_elementos": tamanho,
            "parcialmente_ordenado": caracteristicas["grau_ordenacao"] > 70,
            "muitos_repetidos": caracteristicas["duplicatas"] > 30,

            "estabilidade": False,
            "memoria_limitada": False,
            "operacao": "ordenar",
            "grau_ordenacao": caracteristicas["grau_ordenacao"],
            "percentual_duplicatas": caracteristicas["duplicatas"],
            "amplitude": caracteristicas["amplitude"]
        }

    def validar(self, seed=None):
        """
        Valida o seletor de algoritmos.
        
        Args:
            seed: Seed para random (para testes reproduzíveis)
        """
        if seed is not None:
            random.seed(seed)
        
        cenarios = [
            100,    # Pequeno
            500,    # Pequeno-médio
            1000,   # Medio
            5000,   # Medio-grande
            10000,  # Grande
        ]

        total = 0
        acertos = 0
        motor = MotorDecisao()
        
        print("\n" + "=" * 70)
        print("VALIDANDO MOTOR DE DECISAO")
        print("=" * 70)

        for tamanho in cenarios:
            # GERA DADOS ALEATORIOS
            dados = gerar_aleatorio(tamanho)

            # ANALISA CARACTERISTICAS REAIS
            analisador = AnalisadorCaracteristicas(dados)
            caracteristicas = analisador.analisar()

            # GERA REQUISITOS BASEADO EM DADOS REAIS
            requisitos = self.gerar_requisitos(tamanho, caracteristicas)

            # OBTEM RECOMENDAÇÃO DO MOTOR
            recomendado, scores = motor.recomendar(
                caracteristicas,
                requisitos
            )

            # MEDE DESEMPENHO DE CADA ALGORITMO
            tempos = {}
            for nome, algoritmo in self.ALGORITMOS.items():
                resultado = Benchmark.medir(algoritmo, dados)
                tempos[nome] = resultado["tempo"]
                ordenado = resultado["resultado"]

                if ordenado != sorted(dados):
                    print(f"ERRO: {nome} não ordenou corretamente!")

            # EXTRAI TOP 2 REAIS
            ranking_real = sorted(
                tempos.items(),
                key=lambda item: item[1]
            )
            top2 = [ranking_real[0][0], ranking_real[1][0]]

            # VERIFICA ACERTO
            acertou = recomendado in top2
            total += 1
            if acertou:
                acertos += 1

            # IMPRIME RESULTADO DETALHADO
            print("\n" + "-" * 70)
            print(f"CENÁRIO: {tamanho} elementos")
            print("-" * 70)
            
            print(f"Características reais:")
            print(f"  • Grau de ordenação: {caracteristicas['grau_ordenacao']:.1f}%")
            print(f"  • Duplicatas: {caracteristicas['duplicatas']:.1f}%")
            print(f"  • Amplitude: {caracteristicas['amplitude']}")
            
            print(f"\nRequisitos usados:")
            print(f"  • Parcialmente ordenado: {requisitos['parcialmente_ordenado']}")
            print(f"  • Muitos repetidos: {requisitos['muitos_repetidos']}")
            
            print(f"\nRecomendação do motor:")
            print(f"  • Algoritmo: {recomendado}")
            print(f"  • Score: {scores[recomendado]:.1f}")
            
            print(f"\nDesempenho real (TOP 3):")
            for i, (nome, tempo) in enumerate(ranking_real[:3], 1):
                marker = "ACERTOU" if nome == recomendado else ""
                print(f"  {i}. {nome}: {tempo:.4f}s {marker}")
            
            print(f"\nRanking completo:")
            for nome, tempo in sorted(tempos.items(), key=lambda x: x[1])[:6]:
                print(f"  • {nome}: {tempo:.6f}s")
            
            print(f"\n{'ACERTOU' if acertou else 'ERROU'}")

        # RESULTADO FINAL
        percentual = round((acertos / total) * 100, 2)
        
        print("\n" + "=" * 70)
        print(f"RESULTADO FINAL: {acertos}/{total} acertos ({percentual}%)")
        print("=" * 70 + "\n")

        return percentual