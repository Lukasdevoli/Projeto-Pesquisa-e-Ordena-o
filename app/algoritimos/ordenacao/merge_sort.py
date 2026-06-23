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
    
    def _merge_sort_helper(arr, esquerda, direita):
        """Ordena subarray in-place"""
        if esquerda < direita:
            meio = (esquerda + direita) // 2
            
            _merge_sort_helper(arr, esquerda, meio)
            _merge_sort_helper(arr, meio + 1, direita)
            
            # Faz merge
            _merge_inplace(arr, esquerda, meio, direita)
    
    def _merge_inplace(arr, esquerda, meio, direita):

        # Cria cópia apenas da subarray 
        esq_arr = arr[esquerda:meio + 1]
        dir_arr = arr[meio + 1:direita + 1]
        
        i = j = 0
        k = esquerda
        
        # faz merge das duas subarrays
        while i < len(esq_arr) and j < len(dir_arr):
            if esq_arr[i] <= dir_arr[j]:
                arr[k] = esq_arr[i]
                i += 1
            else:
                arr[k] = dir_arr[j]
                j += 1
            k += 1
        
        # add elementos restantes
        while i < len(esq_arr):
            arr[k] = esq_arr[i]
            i += 1
            k += 1
        
        while j < len(dir_arr):
            arr[k] = dir_arr[j]
            j += 1
            k += 1
    
    resultado = lista.copy()
    _merge_sort_helper(resultado, 0, len(resultado) - 1)
    return resultado