"""
Exemplo de uso de algoritimos de busca

OBS.: Devido a como imports funcionam em pastas python, os codigos tem que ser executados via terminal.
Isso ocorre pois em pastas separadas, python não consegue enxergar o arquivo todo.

pasta1/
    | __init__.py <--- Arquivo que exporta N funcoes
    L arquivo1.py
pasta2/
    L arquivo2.py

    
Ao importar (tambem tem no comeco desse arquivo):

from app.pasta1.pasta2.arquivoexemplo import minha_funcao

Ao rodar arquivo no terminal: 
python -m app.algoritimos.exemplos.exemplo_de_uso_busca
OU
python3 -m app.algoritimos.exemplos.exemplo_de_uso_busca

"""

from app.algoritimos.busca import sequential_search
from app.algoritimos.busca import binary_search

teste = [1, 2, 3, 4]

print(sequential_search(teste, 3))
print(binary_search(teste, 2))
