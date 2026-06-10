def binary_search(array: list[int], alvo: int) -> int:
    """Algoritimo de busca binaria básico para lista de numeros

    Args:
        array (list[int]): Lista ou array com dados
        alvo (int): Numero alvo a ser procurado no array

    Returns: 
        Indice onde numero alvo se encontra, caso nao encontrado retorna -1
    """
    
    esquerda = 0
    direita = len(array) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if array[meio] == alvo:
            return meio

        elif array[meio] < alvo:
            esquerda = meio + 1

        else:
            direita = meio - 1

    return -1