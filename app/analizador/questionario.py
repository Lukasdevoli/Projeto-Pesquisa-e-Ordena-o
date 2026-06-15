# Requisitos: Modo Questionario
def obter_requisitos():

    print("\n-+-+-+-+-+-+-+-+-+-+- QUESTIONÁRIO -+-+-+-+-+-+-+-+-+-+-")

    quantidade = int(
        input(
            "\nQuantos elementos existem no conjunto de dados? "
        )
    )

    parcialmente_ordenado = input(
        "Os dados já estão parcialmente ordenados? (s/n): "
    ).lower()

    muitos_repetidos = input(
        "Há muitos valores repetidos? (s/n): "
    ).lower()

    estabilidade = input(
        "A estabilidade é necessária? (s/n): "
    ).lower()

    memoria = input(
        "Existe restrição de memória? (s/n): "
    ).lower()

    operacao = input(
        "A operação desejada é BUSCAR ou ORDENAR? "
    ).lower()

    return {
        "quantidade_elementos": quantidade,
        "parcialmente_ordenado": parcialmente_ordenado == "s",
        "muitos_repetidos": muitos_repetidos == "s",
        "estabilidade": estabilidade == "s",
        "memoria_limitada": memoria == "s",
        "operacao": operacao
    }

# Requisitos: Modo Direto
def obter_requisitos_direto():

    print("\n-+-+-+-+-+-+-+-+-+-+- QUESTIONÁRIO -+-+-+-+-+-+-+-+-+-+-")

    estabilidade = input(
        "\nPrecisa de estabilidade? (s/n): "
    ).lower()

    memoria = input(
        "Existe restrição de memória? (s/n): "
    ).lower()

    operacao = input(
        "Operação (buscar/ordenar): "
    ).lower()

    return {
        "estabilidade": estabilidade == "s",
        "memoria_limitada": memoria == "s",
        "operacao": operacao
    }