class MotorDecisao:

    def recomendar(self, caracteristicas, requisitos):

        operacao = requisitos["operacao"].lower()

        # MODO BUSCA
        if operacao == "buscar":

            scores = {
                "Busca Sequencial": 50,
                "Busca Binária": 50,
                "Busca Hash": 50
            }

            tamanho = requisitos["quantidade_elementos"]

            if tamanho > 1000:
                scores["Busca Binária"] += 30
                scores["Busca Hash"] += 40
                scores["Busca Sequencial"] -= 30

            if requisitos["muitos_repetidos"]:
                scores["Busca Hash"] += 10

            melhor = max(scores, key=scores.get)

            return melhor, scores

        # MODO ORDENAÇÃO
        scores = {
            "Bubble Sort": 50,
            "Selection Sort": 50,
            "Insertion Sort": 50,
            "Merge Sort": 50,
            "Quick Sort": 50,
            "Heap Sort": 50
        }

        tamanho = requisitos["quantidade_elementos"]

        # Dataset muito grande: eliminar algoritmos O(n²)
        if tamanho > 10000:

            scores["Bubble Sort"] = -999
            scores["Selection Sort"] = -999
            scores["Insertion Sort"] = -999

            scores["Merge Sort"] += 40
            scores["Quick Sort"] += 40
            scores["Heap Sort"] += 40

        elif tamanho > 1000:

            scores["Bubble Sort"] -= 50
            scores["Selection Sort"] -= 50

            scores["Merge Sort"] += 20
            scores["Quick Sort"] += 20

        if requisitos["parcialmente_ordenado"]:

            scores["Insertion Sort"] += 35

        if requisitos["muitos_repetidos"]:

            scores["Merge Sort"] += 20

        if requisitos["estabilidade"]:

            scores["Quick Sort"] -= 30
            scores["Heap Sort"] -= 30
            scores["Selection Sort"] -= 30

            scores["Merge Sort"] += 20
            scores["Insertion Sort"] += 20

        if requisitos["memoria_limitada"]:

            scores["Heap Sort"] += 30
            scores["Merge Sort"] -= 30

        melhor = max(scores, key=scores.get)

        return melhor, scores