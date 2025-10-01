from depth_first_search import DepthFirstSearch


def is_eulerian(graph):
    """
    Verifica se o grafo possui uma trilha ou circuito euleriano.
    :return: "circuito" ou dispara um erro em caso de não ser euleriano.
    :raises ValueError: se o grafo não for conexo ou possuir mais de 0 vértices de grau ímpar.
    """
    odd = 0
    start = None
    for v in range(graph.V()):
        if graph.degree(v) > 0 and start is None:
            start = v

        if graph.degree(v) % 2 != 0:
            odd += 1

    dfs = DepthFirstSearch(graph, start)
    for v in range(graph.V()):
        if graph.degree(v) > 0 and not dfs.marked(v):
            raise ValueError("O grafo não é conexo.")

    if odd == 0:
        return "circuito"

    raise ValueError(f"O grafo não é euleriano pois possui {odd} vertices de grau impar.")
