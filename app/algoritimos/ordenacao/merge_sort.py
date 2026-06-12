def merge_sort(lista: list[int]) -> list[int]:
    """
    Ordena lista utilizando o algoritmo Merge Sort.

    Args:
        lista (list[int]):
            Lista de numeros inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """

    # Caso base da recursão.
    if len(lista) <= 1:
        return lista

    # Divide a lista em duas metades.
    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    # Junta as duas metades ordenadas.
    return merge(esquerda, direita)


def merge(esquerda: list[int], direita: list[int]) -> list[int]:
    """
    Combina duas listas já ordenadas.

    Args:
        esquerda (list[int]):
            Primeira metade ordenada.

        direita (list[int]):
            Segunda metade ordenada.

    Returns:
        list[int]:
            Lista resultante ordenada.
    """

    resultado = []

    i = 0
    j = 0

    # Compara os menores elementos de cada lista.
    while i < len(esquerda) and j < len(direita):

        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes.
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado