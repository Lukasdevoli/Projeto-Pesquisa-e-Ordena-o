def bubble_sort(lista: list[int]) -> list[int]:
    """
    Ordena uma lista utilizando o algoritmo Bubble Sort.

    Args:
        lista (list[int]):
            Lista de numeros inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """

    n = len(lista)

    # Cada passagem posiciona o maior elemento restante.
    for i in range(n):

        # Compara elementos vizinhos.
        for j in range(0, n - i - 1):

            # Se estiverem fora de ordem, realiza a troca.
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista