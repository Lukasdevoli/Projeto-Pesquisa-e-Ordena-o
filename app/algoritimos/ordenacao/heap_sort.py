def heapify(lista: list[int], n: int, i: int) -> None:
    """
    Ajusta subarvore pra manter a propriedade de Max Heap.

    Args:
        lista (list[int]):
            Lista que representa a heap.

        n (int):
            Tamanho considerado da heap.

        i (int):
            Índice do nó raiz da subárvore.

    Returns:
        None
    """

    maior = i

    esquerda = (2 * i) + 1
    direita = (2 * i) + 2

    # Verifica filho esquerdo.
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    # Verifica filho direito.
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Se encontrou um elemento maior, realiza a troca.
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]

        # Continua ajustando a heap.
        heapify(lista, n, maior)


def heap_sort(lista: list[int]) -> list[int]:
    """
    Ordena uma lista utilizando o algoritmo Heap Sort.

    Args:
        lista (list[int]):
            Lista de números inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """

    n = len(lista)

    # Constrói a Max Heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Remove o maior elemento repetidamente.
    for i in range(n - 1, 0, -1):

        # Move a raiz para o final.
        lista[0], lista[i] = lista[i], lista[0]

        # Reconstrói a heap.
        heapify(lista, i, 0)

    return lista