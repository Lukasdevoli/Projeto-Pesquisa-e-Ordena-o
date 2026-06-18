from typing import Tuple, Dict

class MotorDecisao:

    def recomendar(self, caracteristicas: dict, requisitos: dict) -> Tuple[str, Dict[str, int]]:

        operacao = requisitos["operacao"].lower()

        # MODO BUSCA
        if operacao == "buscar":

            scores: Dict[str, int] = {
                "Busca Sequencial": 50,
                "Busca Binária": 50,
                "Busca Hash": 50
            }

            tamanho = requisitos.get("quantidade_elementos", 100)

            if tamanho > 1000:
                scores["Busca Binária"] += 30
                scores["Busca Hash"] += 40
                scores["Busca Sequencial"] -= 30

            if requisitos.get("muitos_repetidos", False):
                scores["Busca Hash"] += 10

            melhor: str = max(scores, key=scores.get)
            return melhor, scores

        # MODO ORDENACAO
        scores: Dict[str, int] = {
            "Bubble Sort": 50,
            "Selection Sort": 50,
            "Insertion Sort": 50,
            "Merge Sort": 50,
            "Quick Sort": 50,
            "Heap Sort": 50
        }

        tamanho = requisitos.get("quantidade_elementos", 100)

        
        if tamanho > 10000:
            # dataset muito grande
            scores["Bubble Sort"] = -999
            scores["Selection Sort"] = -999
            scores["Insertion Sort"] = -999
            
            # algoritmos O(n log n) 
            scores["Quick Sort"] += 50      
            scores["Heap Sort"] += 50       
            scores["Merge Sort"] += 20     

        elif tamanho > 1000:
            # dataset medio-grande prefere O(n log n)
            scores["Bubble Sort"] -= 50
            scores["Selection Sort"] -= 50
            
            scores["Quick Sort"] += 30      # Melhor pra medio grande
            scores["Heap Sort"] += 25
            scores["Merge Sort"] += 20

        elif tamanho > 100:
            # dataset pequeno medio qualquer um funciona
            scores["Quick Sort"] += 10
            scores["Heap Sort"] += 5
            scores["Merge Sort"] += 5

        else:
            # dataset muito pequeno (< 100) insertion sort aceitável
            scores["Insertion Sort"] += 15
            scores["Quick Sort"] += 10
        

        if requisitos.get("parcialmente_ordenado", False):

            scores["Insertion Sort"] += 50
            scores["Bubble Sort"] += 10

        # muitos repetidos
        if requisitos.get("muitos_repetidos", False):
            scores["Merge Sort"] += 20

        # estabilidade importante
        if requisitos.get("estabilidade", False):
            scores["Merge Sort"] += 30
            scores["Insertion Sort"] += 20
            
            scores["Quick Sort"] -= 25
            scores["Heap Sort"] -= 25

        # memoria limitada
        if requisitos.get("memoria_limitada", False):
            scores["Heap Sort"] += 30
            scores["Merge Sort"] -= 30

        melhor: str = max(scores, key=scores.get)
        return melhor, scores