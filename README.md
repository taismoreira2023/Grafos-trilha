# 🧮 Circuitos Eulerianos — Algoritmos de Hierholzer e Fleury

Este projeto foi desenvolvido como parte de uma atividade acadêmica para a disciplina de Resolução probremas com grafos. O objetivo é implementar e comparar dois algoritmos clássicos para encontrar **circuitos eulerianos** em grafos: **Hierholzer** e **Fleury**.

## 📚 Conceitos

Um **circuito euleriano** é um caminho fechado em um grafo que percorre cada aresta exatamente uma vez. Para que um grafo não direcionado possua um circuito euleriano, ele deve ser **conexo** e todos os seus vértices devem ter **grau par**.

## 🧠 Algoritmos Implementados

### 🔁 Hierholzer
- Inicia em qualquer vértice com grau não zero.
- Constrói um circuito parcial.
- Insere subcircuitos conforme encontra vértices com arestas não exploradas.
- É eficiente e ideal para grafos grandes.

### 🧭 Fleury
- Escolhe arestas cuidadosamente para evitar pontes (arestas cuja remoção desconecta o grafo).
- Mais intuitivo, porém menos eficiente.
- Requer verificação constante de conectividade.

## 🏃 Como exucutar
### Hierholzer
Para executar o algoritmo Hierholzer

```sh
python src/main.py hierholzer
# ou caso queira passar um arquivo especifico
cat data/c4_isolado9.txt | python src/main.py hierholzer
```

### Fleury
Para executar o algoritmo Fleury

```sh
python src/main.py fleury
# ou caso queira passar um arquivo especifico
cat data/c4_isolado9.txt | python src/main.py fleury
```


## 🛠️ Tecnologias e Base

Este projeto utiliza como base o repositório [`itu-algs4`](https://github.com/itu-algs4/itu-algs4), que fornece implementações fundamentais de estruturas de dados e grafos inspiradas na biblioteca algs4 de Princeton.

### Principais classes utilizadas do `itu-algs4`:
- `Graph`: representação de grafos não direcionados.
- `Stack`, `Bag`, `DepthFirstSearch`: estruturas auxiliares para os algoritmos.

### Classes dos algortimos
- `Fleury`: Algoritmo de Fleury, arquivo: `src/fleury.py`
- `Hierholzer`: Algoritmo de Hierholzer, arquivo: `src/hierholzer.py`

## 📁 Estrutura do Projeto

```
├── src/
│ ├── bag.py
│ ├── graph.py
│ ├── stack.py
│ ├── depth_first_search.py
│ ├── main.py # arquivo principal
│ ├── fleury.py # Algortimo fleury
│ ├── utils.py # verificar se o grafo é euleriano
│ └── hierholzer.py # Algoritmo Hierholzer
├── data/ # grafos de teste
│ ├── c4.txt # Existe circuito (ciclo 0–1–2–3–0).
│ ├── c4_isolado9.txt # Existe circuito (C₄ + vértice isolado; conectividade ignora isolados).
│ ├── caminho_triangulo.txt # Não euleriano (graus ímpares).
│ ├── konigsberg.txt # Não euleriano (proxy de K₄).
│ ├── desconexo.txt # Desconexo (dois componentes com arestas).
│ └── hierholzer.txt # dados para exemplo de hierholzer
└── README.md
```
