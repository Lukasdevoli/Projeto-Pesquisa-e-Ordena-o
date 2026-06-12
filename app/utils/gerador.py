import random


def gerar_aleatorio(n):

    return [
        random.randint(1, 100000)
        for _ in range(n)
    ]