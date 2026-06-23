def quick_sort(lista: list[int]) -> list[int]:
    """
    Ordena lista usando Quick Sort in-place.

    Args:
        lista (list[int]):
            Lista de numeros inteiros a ser ordenada.

    Returns:
        list[int]:
            Lista ordenada em ordem crescente.
    """
    
    def _quick_sort_helper(arr, esquerda, direita):
        if esquerda < direita:
            # Particiona e retorna índice do pivô
            pivo_idx = _particionar(arr, esquerda, direita)
            
            # Ordena partes esquerda e direita
            _quick_sort_helper(arr, esquerda, pivo_idx - 1)
            _quick_sort_helper(arr, pivo_idx + 1, direita)
    
    def _particionar(arr, esquerda, direita):
        """Particiona array e retorna índice do pivô"""
        pivo = arr[direita]
        i = esquerda - 1
        
        for j in range(esquerda, direita):
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[direita] = arr[direita], arr[i + 1]
        return i + 1
    
    resultado = lista.copy()
    _quick_sort_helper(resultado, 0, len(resultado) - 1)
    return resultado