COMPLEXIDADES = {

    "Bubble Sort": {
        "melhor": "O(n)",
        "medio": "O(n²)",
        "pior": "O(n²)",
        "espaco": "O(1)",
        "estavel": "Sim",
        "comportamento":
            "Adequado apenas para conjuntos pequenos ou quase ordenados."
    },

    "Selection Sort": {
        "melhor": "O(n²)",
        "medio": "O(n²)",
        "pior": "O(n²)",
        "espaco": "O(1)",
        "estavel": "Não",
        "comportamento":
            "Realiza poucas trocas, mas muitas comparações."
    },

    "Insertion Sort": {
        "melhor": "O(n)",
        "medio": "O(n²)",
        "pior": "O(n²)",
        "espaco": "O(1)",
        "estavel": "Sim",
        "comportamento":
            "Excelente para listas pequenas ou parcialmente ordenadas."
    },

    "Merge Sort": {
        "melhor": "O(n log n)",
        "medio": "O(n log n)",
        "pior": "O(n log n)",
        "espaco": "O(n)",
        "estavel": "Sim",
        "comportamento":
            "Desempenho previsível e estável, indicado para grandes volumes."
    },

    "Quick Sort": {
        "melhor": "O(n log n)",
        "medio": "O(n log n)",
        "pior": "O(n²)",
        "espaco": "O(log n)",
        "estavel": "Não",
        "comportamento":
            "Normalmente é o algoritmo de ordenação mais rápido na prática."
    },

    "Heap Sort": {
        "melhor": "O(n log n)",
        "medio": "O(n log n)",
        "pior": "O(n log n)",
        "espaco": "O(1)",
        "estavel": "Não",
        "comportamento":
            "Baixo consumo de memória e desempenho consistente."
    },

    "Busca Sequencial": {
        "melhor": "O(1)",
        "medio": "O(n)",
        "pior": "O(n)",
        "espaco": "O(1)",
        "estavel": "-",
        "comportamento":
            "Não exige ordenação prévia dos dados."
    },

    "Busca Binária": {
        "melhor": "O(1)",
        "medio": "O(log n)",
        "pior": "O(log n)",
        "espaco": "O(1)",
        "estavel": "-",
        "comportamento":
            "Exige que os dados estejam previamente ordenados."
    },

    "Busca Hash": {
        "melhor": "O(1)",
        "medio": "O(1)",
        "pior": "O(n)",
        "espaco": "O(n)",
        "estavel": "-",
        "comportamento":
            "Excelente desempenho para consultas frequentes."
    }
}