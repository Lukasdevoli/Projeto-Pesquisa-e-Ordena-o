def insertion_sort(lista: list[int]) -> list[int]:
    """
    Ordena lista utilizando o algoritmo Insertion Sort.

    Args:
        lista (list[int]):
            Lista de numeros inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """

    # Começa do segundo elemento.
    # O primeiro é considerado ordenado.
    for i in range(1, len(lista)):

        # Valor que será inserido na posição correta.
        atual = lista[i]

        # Índice do elemento anterior.
        j = i - 1

        # Move os elementos maiores para a direita.
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere o elemento na posição correta.
        lista[j + 1] = atual

    return lista