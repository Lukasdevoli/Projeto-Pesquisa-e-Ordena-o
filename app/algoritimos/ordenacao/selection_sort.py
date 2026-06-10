def selection_sort(lista: list[int]) -> list[int]:
    """
    Ordena lista usando algoritmo Selection Sort.

    Args:
        lista (list[int]):
            Lista de numeros inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """

    n = len(lista)

    # Percorre todas as posições da lista.
    for i in range(n):

        # Assume que o menor elemento está na posição atual.
        menor = i

        # Procura um elemento menor no restante da lista.
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        # Troca o menor encontrado pela posição atual.
        lista[i], lista[menor] = lista[menor], lista[i]

    return lista