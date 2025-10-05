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

#### 📈 Complexidade — implementação atual (`Hierholzer.make_circuit`)
- Notação: n = |V| (vértices) e m = |E| (arestas).
- A versão clássica do algoritmo de Hierholzer roda em tempo O(m) e espaço O(n + m).
- Nesta implementação específica (arquivo `src/hierholzer.py`, método `make_circuit`), o pior caso é maior por decisões de seguir mais o algoritmo no Livro de GOLDBARG:
  - A cada iteração é reconstruído um grafo auxiliar sem as arestas já usadas (`make_graph_without_cycle`). Essa rotina:
    - Copia toda a lista de adjacência: O(n + m).
    - Remove, de listas Python, as arestas do ciclo atual: cada remoção é O(grau) no pior caso; removendo L arestas resulta em O(L · Δ), onde Δ é o grau máximo.
  - Um novo ciclo é encontrado via DFS a partir de um vértice do ciclo atual (`CycleFromVertex`): O(n + m) no pior caso sobre o grafo remanescente.
  - A operação de união dos ciclos (`union`) percorre todo o circuito acumulado e o subciclo inserido: custo proporcional ao tamanho atual do circuito.
- Consequência:
  - Tempo (pior caso): O(m^2 + m·n). Intuitivamente, porque:
    - A união repetido soma prefixos do circuito e pode acumular O(m^2).
    - A reconstrução do grafo auxiliar em cada passo adiciona O(m·n + m^2) considerando as remoções em listas e até m/3 iterações (ciclos pequenos).
  - Espaço: O(n + m), dominado pelas estruturas do grafo e pilhas de ciclos (o grafo auxiliar é do mesmo tamanho assintótico do original).

### 🧭 Fleury
- Escolhe arestas cuidadosamente para evitar pontes (arestas cuja remoção desconecta o grafo).
- Mais intuitivo, porém menos eficiente.
- Requer verificação constante de conectividade.

#### 📈 Complexidade — implementação atual (`Fleury.find`)
- Notação: n = |V| (vértices) e m = |E| (arestas).
- Tempo (pior caso): O(m²). Intuição e detalhamento para esta implementação (arquivo `src/fleury.py`, método `find`):
  - O algoritmo remove exatamente uma aresta por iteração, totalizando m iterações.
  - Para evitar escolher uma ponte, a função `is_valid_next_edge(u, v)` executa duas buscas em profundidade (DFS):
    - Uma antes de remover a aresta (para contar os vértices alcançáveis a partir de `u`).
    - Outra após remover temporariamente a aresta (para verificar se a conectividade mudou).
    - Cada DFS custa O(n + m_remanescente) no grafo residual.
  - Há ainda uma verificação global `any(adj[v] for v in range(self.V))` que custa O(n) por iteração, e remoções/inserções em listas de adjacência com custo O(Δ) por aresta (Δ = grau máximo).
  - Somando os custos ao longo das m iterações, obtemos O(m · (n + m)) no pior caso, que é convencionalmente reportado como O(m²) quando m ≥ n (caso típico em grafos conexos com arestas suficientes).
- Espaço: O(n + m), dominado pela cópia das listas de adjacência (`adj`) e pelos vetores auxiliares de visitação (`visited`).

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
