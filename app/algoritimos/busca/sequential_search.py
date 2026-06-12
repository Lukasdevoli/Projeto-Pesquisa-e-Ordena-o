def sequential_search(array: list[int], alvo: int) -> int: 
    """Algoritimo de busca sequencial básico para lista de numeros

    Args:
        array (list[int]): Lista ou array com dados
        alvo (int): Numero alvo a ser procurado no array

    Returns: 
        Indice onde numero alvo se encontra, caso nao encontrado retorna -1
    """

    for indice, valor in enumerate(array):
        if valor == alvo:
            return indice

    return -1