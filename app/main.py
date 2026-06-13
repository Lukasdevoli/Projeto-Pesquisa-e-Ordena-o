from analizador.caracteristicas import AnalisadorCaracteristicas
from analizador.questionario import obter_requisitos
from analizador.motor_decisao import MotorDecisao

from utils.gerador import gerar_aleatorio


def exibir_ranking(scores):

    print("\n===== RANKING DOS ALGORITMOS =====")

    ranking = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for nome, score in ranking:
        print(f"{nome}: {score} pontos")


def main():

    print("=" * 50)
    print("SELETOR ADAPTATIVO DE ALGORITMOS")
    print("=" * 50)

    requisitos = obter_requisitos()

    dados = gerar_aleatorio(
        requisitos["quantidade_elementos"]
    )

    analisador = AnalisadorCaracteristicas(dados)

    caracteristicas = analisador.analisar()

    print("\nCaracterísticas encontradas:")

    print(
        f"Tamanho: "
        f"{caracteristicas['tamanho']}"
    )

    print(
        f"Tipo: "
        f"{caracteristicas['tipo']}"
    )

    print(
        f"Grau de ordenação: "
        f"{caracteristicas['grau_ordenacao']}%"
    )

    print(
        f"Duplicatas: "
        f"{caracteristicas['duplicatas']}%"
    )

    print(
        f"Amplitude: "
        f"{caracteristicas['amplitude']}"
    )

    COMPLEXIDADES = {

        "Bubble Sort": {
            "tempo": "O(n²)",
            "espaco": "O(1)"
        },

        "Selection Sort": {
            "tempo": "O(n²)",
            "espaco": "O(1)"
        },

        "Insertion Sort": {
            "tempo": "O(n²)",
            "espaco": "O(1)"
        },

        "Merge Sort": {
            "tempo": "O(n log n)",
            "espaco": "O(n)"
        },

        "Quick Sort": {
            "tempo": "O(n log n)",
            "espaco": "O(log n)"
        },

        "Heap Sort": {
            "tempo": "O(n log n)",
            "espaco": "O(1)"
        },

        "Busca Sequencial": {
            "tempo": "O(n)",
            "espaco": "O(1)"
        },

        "Busca Binária": {
            "tempo": "O(log n)",
            "espaco": "O(1)"
        },

        "Busca Hash": {
            "tempo": "O(1)",
            "espaco": "O(n)"
        }
    }

    motor = MotorDecisao()

    algoritmo, scores = motor.recomendar(
        caracteristicas,
        requisitos
    )

    complexidade = COMPLEXIDADES.get(
        algoritmo,
        {
        "tempo": "Desconhecida",
        "espaco": "Desconhecida"
        }
    )

    print("\n" + "=" * 50)
    print("RESULTADO")
    print("=" * 50)

    print(
        f"\nAlgoritmo recomendado: {algoritmo}"
    )

    print(
        f"Pontuação: {scores[algoritmo]}"
    )

    print(
        f"Complexidade de Tempo: "
        f"{complexidade['tempo']}"
    )

    print(
        f"Complexidade de Espaço: "
        f"{complexidade['espaco']}"
    )

    exibir_ranking(scores)


if __name__ == "__main__":
    main()