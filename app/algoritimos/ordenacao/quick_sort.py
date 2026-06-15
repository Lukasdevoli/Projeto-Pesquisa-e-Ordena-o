def quick_sort(lista: list[int]) -> list[int]:
    """
    Ordena lista usando o algoritmo Quick Sort.

    Args:
        lista (list[int]):
            Lista de numeros inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """

    # Caso base.
    if len(lista) <= 1:
        return lista

    # Escolhe o primeiro elemento como pivô.
    pivo = lista[0]

    # Elementos menores ou iguais ao pivô.
    menores = [
        valor
        for valor in lista[1:]
        if valor <= pivo
    ]

    # Elementos maiores que o pivô.
    maiores = [
        valor
        for valor in lista[1:]
        if valor > pivo
    ]

    # Ordena recursivamente cada lado.
    return (
        quick_sort(menores)
        + [pivo]
        + quick_sort(maiores)
    )