from analisador.caracteristicas import CaracteristicasDataset
from analisador.questionario import obter_requisitos
from analisador.motor_decisao import MotorDecisao

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

    print("\nGerando conjunto de dados...")

    tamanho = int(
        input(
            "Informe o tamanho do dataset: "
        )
    )

    dados = gerar_aleatorio(tamanho)

    print("\nAnalisando características...")

    analisador = CaracteristicasDataset()

    caracteristicas = analisador.analisar(dados)

    print("\nCaracterísticas encontradas:")

    print(f"Tamanho: {caracteristicas['tamanho']}")
    print(
        f"Grau de ordenação: "
        f"{caracteristicas['grau_ordenacao']:.2f}%"
    )
    print(
        f"Duplicatas: "
        f"{caracteristicas['duplicatas']:.2f}%"
    )
    print(
        f"Amplitude: "
        f"{caracteristicas['amplitude']}"
    )

    print("\nResponda ao questionário:")

    requisitos = obter_requisitos()

    motor = MotorDecisao()

    algoritmo, scores = motor.recomendar(
        caracteristicas,
        requisitos
    )

    print("\n" + "=" * 50)
    print("RESULTADO")
    print("=" * 50)

    print(
        f"\nAlgoritmo recomendado: "
        f"{algoritmo}"
    )

    print(
        f"Pontuação: "
        f"{scores[algoritmo]}"
    )

    exibir_ranking(scores)

    print("\nFim da análise.")


if __name__ == "__main__":
    main()