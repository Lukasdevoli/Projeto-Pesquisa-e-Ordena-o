# 🚀 Projeto: Pesquisa e Ordenação de Dados

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Algorithms](https://img.shields.io/badge/Algorithms-Busca%20e%20Ordenação-orange)
![License](https://img.shields.io/badge/Academic-Project-lightgrey)

> Sistema interativo de recomendação de algoritmos para busca e ordenação, com foco em análise de desempenho, complexidade computacional e validação prática.

## 📌 Resumo rápido

| Aspecto | Detalhe |
|---|---|
| Área | Pesquisa e Ordenação de Dados |
| Objetivo | Recomendar algoritmos com base em características do dataset e requisitos do usuário |
| Abordagem | Heurística + benchmark + validação empírica |
| Público | Estudantes, acadêmicos e interessados em algoritmos |

### ✨ Destaques
- Interface simples e didática para testes e demonstrações.
- Comparação entre algoritmos de busca e ordenação.
- Análise de complexidade temporal e espacial.
- Validação prática do desempenho recomendado.

## 1. 🎯 Introdução

Este projeto foi desenvolvido no contexto da disciplina de Pesquisa e Ordenação de Dados, com o objetivo de estudar e aplicar algoritmos de ordenação e busca em estruturas de dados, além de analisar critérios de escolha de algoritmos com base em características do conjunto de dados e requisitos do usuário.

A proposta central do sistema é fornecer um seletor adaptativo que recomenda, dentre os algoritmos disponíveis, aquele que apresenta maior adequação para uma determinada situação de uso. Para isso, o projeto combina:

- análise de características do dataset;
- coleta de requisitos pelo usuário;
- lógica de decisão para recomendação;
- benchmark e validação empírica de desempenho.

## 2. 🎯 Objetivo do Projeto

O projeto tem como objetivos principais:

1. compreender o comportamento de algoritmos de busca e ordenação;
2. comparar desempenho teórico e prático entre diferentes abordagens;
3. desenvolver um sistema de recomendação baseado em heurísticas;
4. demonstrar, de forma prática, a relação entre complexidade computacional e desempenho real.

## 3. 📚 Contexto Acadêmico

Este trabalho está inserido na área de algoritmos e estruturas de dados, com foco em:

- complexidade temporal e espacial;
- estabilidade e eficiência de algoritmos;
- análise de cenários com dados grandes, parcialmente ordenados e com valores repetidos;
- uso de métricas experimentais para validação.

A implementação busca unir fundamentos teóricos de pesquisa operacional sobre algoritmos com uma aplicação interativa que facilita a compreensão dos conceitos estudados.

## 4. ⚙️ Funcionalidades

O sistema oferece as seguintes funcionalidades:

### 4.1 Geração de dados
O projeto é capaz de gerar conjuntos de dados aleatórios para testes e simulações.

### 4.2 Análise de características
O analisador verifica propriedades como:
- tamanho do conjunto;
- grau de ordenação;
- percentual de duplicatas;
- amplitude dos valores;
- tipo dos dados.

### 4.3 Questionário de requisitos
O usuário responde perguntas sobre:
- quantidade de elementos;
- grau de ordenação dos dados;
- presença de valores repetidos;
- necessidade de estabilidade;
- restrição de memória;
- tipo de operação desejada (buscar ou ordenar).

### 4.4 Recomendação adaptativa
Com base nas respostas e nas características do dataset, o motor de decisão sugere o algoritmo mais adequado.

### 4.5 Benchmark e validação
O projeto inclui recursos para medir desempenho, como:
- tempo de execução;
- uso de memória;
- comparação entre algoritmos;
- validação empírica da recomendação.

### 4.6 Instrumentação e Métricas

O sistema possui mecanismos de instrumentação para coleta de métricas experimentais durante a execução dos algoritmos.

Atualmente são monitorados:

- tempo real de execução;
- uso aproximado de memória;
- ranking de desempenho entre algoritmos;
- comparação entre desempenho teórico e desempenho observado.

Essas métricas permitem confrontar a análise assintótica tradicional com resultados obtidos em cenários reais de execução.

### 4.7 Modos de Operação

O sistema pode operar em dois modos distintos:

#### Modo Questionário

O usuário informa características do problema através de perguntas guiadas.

Exemplos:

- quantidade de elementos;
- necessidade de estabilidade;
- existência de restrição de memória;
- presença de valores repetidos;
- tipo de operação (busca ou ordenação).

#### Modo Direto

O usuário fornece diretamente um array de entrada.

O sistema realiza automaticamente:

- análise de tamanho;
- cálculo do grau de ordenação;
- identificação de duplicatas;
- análise de amplitude;
- geração automática de recomendações.

## 5. 📁 Estrutura do Projeto

A organização do repositório está organizada da seguinte forma:

```text
Projeto-Pesquisa-e-Ordena-o/
├── README.md
├── requirements.txt
├── .gitgnore
└── app/
    ├── main.py
    ├── algoritimos/
    │   ├── busca/
    │   │   ├── __init__.py
    │   │   ├── binary_search.py
    │   │   ├── hash_search.py
    │   │   └── sequential_search.py
    │   └── ordenacao/
    │       ├── __init__.py
    │       ├── bubble_sort.py
    │       ├── heap_sort.py
    │       ├── insertion_sort.py
    │       ├── merge_sort.py
    │       ├── quick_sort.py
    │       └── selection_sort.py
    ├── analizador/
    │   ├── __init__.py
    │   ├── caracteristicas.py
    │   ├── motor_decisao.py
    │   └── questionario.py
    ├── testes/
    │   ├── __init__.py
    │   └── test_seletor.py
    ├── utils/
    │   ├── __init__.py
    │   ├── benchmark.py
    │   ├── complexidade.py
    │   ├── contador.py
    │   └── gerador.py
    └── validacao/
        ├── __init__.py
        └── validar_seletor.py
```

## 6. 🧩 Descrição dos Módulos

### 6.1 Arquivo principal da raiz
- main1.py: ponto de entrada alternativo da aplicação.

### 6.2 app/main.py
Arquivo principal da aplicação, responsável por:
- gerar dados;
- analisar características;
- coletar requisitos;
- recomendar o algoritmo mais adequado;
- exibir o ranking e o relatório final.

### 6.3 app/analizador
Contém a lógica de análise e tomada de decisão:
- caracteristicas.py: calcula métricas do dataset;
- questionario.py: coleta informações do usuário;
- motor_decisao.py: aplica as regras para recomendar algoritmos.

### 6.4 app/algoritimos
Implementações dos algoritmos utilizados no projeto:

#### Busca
- Busca Sequencial
- Busca Binária
- Busca Hash

#### Ordenação
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

### 6.5 app/utils
Funções auxiliares do sistema:
- benchmark.py: mede tempo e memória;
- complexidade.py: armazena informações teóricas de complexidade;
- gerador.py: gera entradas aleatórias;
- contador.py: suporte para contagem e análise.

### 6.6 app/validacao
Contém a validação empírica do seletor, verificando se o algoritmo recomendado está entre os melhores em cenários testados.

### 6.7 app/testes
Implementa testes automatizados para validar o comportamento esperado do sistema.

## 7. ▶️ Como Executar

### Requisitos
- Python 3.8 ou superior
- Bibliotecas padrão da linguagem

### Instalação
No diretório do projeto, execute:

```bash
pip install -r requirements.txt
```

### Execução da aplicação principal

```bash
python app/main.py
```

### Execução dos testes

```bash
# Testes de Corretude de Algoritmos
python -m unittest app.testes.test_algoritmos_ordenacao -v

# Testes do Motor de Decisão
python -m unittest app.testes.test_motor_decisao -v

# Testes do Analisador de Características
python -m unittest app.testes.test_caracteristicas -v

# Testes do Validador/Seletor
python -m unittest app.testes.test_seletor -v

# Descubra todos os testes na pasta
python -m unittest discover -s app/testes -p "test_*.py" -v
```

## 8. 🔄 Fluxo de Funcionamento

1. O sistema gera ou recebe um conjunto de dados.
2. O analisador calcula suas características principais.
3. O usuário responde a um questionário sobre requisitos.
4. O motor de decisão atribui pontuações aos algoritmos.
5. O programa recomenda o algoritmo mais adequado.
6. O sistema exibe um ranking e, quando aplicável, métricas de benchmark.

## 9. 📊 Análise de Complexidade

O projeto mantém uma base de conhecimento contendo informações teóricas sobre cada algoritmo implementado.

Para cada algoritmo são armazenadas:

- complexidade de melhor caso;
- complexidade de caso médio;
- complexidade de pior caso;
- uso de memória;
- estabilidade;
- comportamento prático.

Essas informações são apresentadas no relatório final para justificar a recomendação realizada pelo sistema.

### Exemplo

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso |
|------------|------------|------------|------------|
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |


## 10. 🧪 Validação Empírica

Além da análise teórica, o projeto realiza validação experimental das recomendações produzidas pelo seletor adaptativo.

O processo consiste em:

1. gerar diferentes cenários de teste;
2. executar todos os algoritmos aplicáveis;
3. medir o tempo real de execução;
4. construir um ranking experimental;
5. comparar esse ranking com a recomendação realizada pelo motor de decisão.

O objetivo é verificar se o algoritmo recomendado encontra-se entre os algoritmos mais eficientes observados experimentalmente.

Essa abordagem permite avaliar a qualidade das heurísticas utilizadas pelo sistema.

## 11. ⏱️ Benchmark Experimental

O módulo de benchmark é responsável pela medição de desempenho dos algoritmos.

As métricas coletadas incluem:

- tempo de execução;
- uso aproximado de memória;
- desempenho relativo entre algoritmos.

Os resultados podem ser utilizados para:

- comparação entre algoritmos;
- geração de gráficos;
- análise acadêmica;
- validação das recomendações do seletor.

## 12. ✅ Conclusão

Além da recomendação baseada em heurísticas, o sistema também incorpora benchmark experimental, instrumentação de desempenho e validação empírica, aproximando o comportamento observado da teoria clássica de análise de algoritmos.

## 13. 🌱 Referência para Desenvolvimento Futuro

Possíveis melhorias para o projeto incluem:

- integração com interface gráfica;
- persistência de históricos de execução;
- comparação visual de desempenho;
- suporte a outros tipos de dados;
- expansão da base de regras do motor de decisão.
