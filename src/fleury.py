class Fleury:
    def __init__(self, graph, start=0):
        """
        Inicializa o algoritmo de Fleury com um grafo.
        
        :param graph: uma instância da classe Graph
        :param start: vértice inicial para a trilha ou circuito (opcional)
        """
        self.graph = graph
        self.start = start
        self.V = graph.V()

    def is_eulerian(self):
        """
        Verifica se o grafo possui uma trilha ou circuito euleriano.
        :return: "circuito", "trilha" ou None
        """
        odd = 0
        for v in range(self.V):
            if self.graph.degree(v) % 2 != 0:
                odd += 1
        if odd == 0:
            return "circuito"
        elif odd == 2:
            return "trilha(caminho)"
        else:
            return None

    def find(self):
        """
        Executa o algoritmo de Fleury para encontrar a trilha ou circuito euleriano.
        :return: lista de vértices na ordem da trilha, ou None se não for euleriano.
        """
        if self.is_eulerian() is None:
            return None

        # Cria cópia das adjacências para manipular
        adj = [list(self.graph.adj(v)) for v in range(self.V)]
        path = []

        def remove_edge(u, v):
            adj[u].remove(v)
            adj[v].remove(u)

        def dfs_count(u, visited):
            visited[u] = True
            count = 1
            for v in adj[u]:
                if not visited[v]:
                    count += dfs_count(v, visited)
            return count

        def is_valid_next_edge(u, v):
            if len(adj[u]) == 1:
                return True
            visited = [False] * self.V
            count1 = dfs_count(u, visited)
            remove_edge(u, v)
            visited = [False] * self.V
            count2 = dfs_count(u, visited)
            adj[u].append(v)
            adj[v].append(u)
            return count1 == count2

        if self.is_eulerian() == "trilha":
            for v in range(self.V):
                if self.graph.degree(v) % 2 != 0:
                    self.start = v
                    break

        u = self.start
        while any(adj[v] for v in range(self.V)):
            for v in adj[u]:
                if is_valid_next_edge(u, v):
                    path.append(u)
                    remove_edge(u, v)
                    u = v
                    break
        path.append(u)
        return path

   