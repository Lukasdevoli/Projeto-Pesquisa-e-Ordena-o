from analizador.caracteristicas import AnalisadorCaracteristicas
from analizador.questionario import obter_requisitos, obter_requisitos_direto
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

def obter_justificativas(algoritmo, requisitos):

    justificativas = []

    if requisitos["parcialmente_ordenado"]:
        justificativas.append(
            "O conjunto de dados foi informado como parcialmente ordenado."
        )

    if requisitos["estabilidade"]:
        justificativas.append(
            "Foi indicada necessidade de estabilidade na ordenação."
        )

    if requisitos["memoria_limitada"]:
        justificativas.append(
            "Existe restrição de memória disponível."
        )

    if requisitos["muitos_repetidos"]:
        justificativas.append(
            "O conjunto possui muitos valores repetidos."
        )

    justificativas.append(
        f"O algoritmo {algoritmo} recebeu a maior pontuação segundo as regras do motor de decisão."
    )

    return justificativas


def obter_avisos(algoritmo, requisitos):

    avisos = []

    if algoritmo == "Merge Sort":
        avisos.append(
            "Merge Sort necessita memória auxiliar proporcional ao tamanho do dataset."
        )

    if algoritmo == "Quick Sort":
        avisos.append(
            "Quick Sort pode apresentar pior caso O(n²) dependendo da escolha do pivô."
        )

    if algoritmo == "Busca Binária":
        avisos.append(
            "Busca Binária exige que os dados estejam previamente ordenados."
        )

    if algoritmo == "Busca Hash":
        avisos.append(
            "Busca Hash exige estrutura de armazenamento adicional."
        )
    
    if requisitos["quantidade_elementos"] > 10000:
        avisos.append(
            "Bubble Sort, Selection Sort e Insertion Sort foram eliminados por possuírem complexidade O(n²)."
        )

    return avisos

def ler_array_usuario():

    entrada = input(
        "\nDigite os números separados por vírgula:\n"
    )

    dados = [
        int(valor.strip())
        for valor in entrada.split(",")
    ]

    return dados

def main():

    print("\nModo de operação:")
    print("1 - Questionário")
    print("2 - Modo Direto")

    modo = input(
        "\nEscolha uma opção: "
    ).strip()

    if modo == "2":

        dados = ler_array_usuario()

        analisador = AnalisadorCaracteristicas(
            dados
        )

        caracteristicas = analisador.analisar()

        requisitos = {
            "quantidade_elementos":
                caracteristicas["tamanho"],

            "parcialmente_ordenado":
                caracteristicas["grau_ordenacao"] >= 70,

            "muitos_repetidos":
                caracteristicas["duplicatas"] >= 20
        }

        requisitos.update(
            obter_requisitos_direto()
        )

    else:

        requisitos = obter_requisitos()

        dados = gerar_aleatorio(
            requisitos["quantidade_elementos"]
        )

        analisador = AnalisadorCaracteristicas(
            dados
        )

        caracteristicas = analisador.analisar()

    # print("=" * 50)
    # print("SELETOR ADAPTATIVO DE ALGORITMOS")
    # print("=" * 50)

    # requisitos = obter_requisitos()

    # dados = gerar_aleatorio(
    #     requisitos["quantidade_elementos"]
    # )

    # analisador = AnalisadorCaracteristicas(dados)

    # caracteristicas = analisador.analisar()

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

    pontuacao_final = max(
        0,
        min(100, scores[algoritmo])
    )

    ranking = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    alternativas = [
        nome
        for nome, _ in ranking[1:4]
    ]

    complexidade = COMPLEXIDADES.get(
        algoritmo,
        {
        "tempo": "Desconhecida",
        "espaco": "Desconhecida"
        }
    )

    print("\n" + "=" * 50)
    print("RELATÓRIO FINAL")
    print("=" * 50)

    print(
        f"\nAlgoritmo recomendado: {algoritmo}"
    )

    print(
        f"Pontuação obtida: {scores[algoritmo]}"
    )

    print(
        f"Pontuação normalizada: {pontuacao_final}/100"
    )

    print(
        f"Pontuação final: {pontuacao_final}/100"
    )

    print(
        f"Complexidade de Tempo: "
        f"{complexidade['tempo']}"
    )

    print(
        f"Complexidade de Espaço: "
        f"{complexidade['espaco']}"
    )

    print("\nAlternativas possíveis:")

    for alternativa in alternativas:
        print(f"- {alternativa}")

    print("\nJustificativas:")

    for justificativa in obter_justificativas(
        algoritmo,
        requisitos
    ):
        print(f"• {justificativa}")

    print("\nAvisos importantes:")

    avisos = obter_avisos(
        algoritmo,
        requisitos
    )

    if avisos:

        for aviso in avisos:
            print(f"⚠ {aviso}")

    else:
        print("Nenhum aviso relevante.")

    print("\n")
    exibir_ranking(scores) 


if __name__ == "__main__":
    main()