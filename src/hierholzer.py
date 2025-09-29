import string
from graph import Graph
from stack import Stack
from copy import deepcopy


def print_letters(cycle: Stack):
    result = ''
    for w in cycle:
        result += string.ascii_lowercase[w]
        result += ' '

    return result


def make_graph_without_cycle(graph: Graph, stack: Stack):
    cycle = deepcopy(stack)
    adj_copy: dict[int, list[int]] = {}
    for v in range(graph.V()):
        adj_copy[v] = []
        for w in graph.adj(v):
            adj_copy[v].append(w)

    u = cycle.pop()
    count = 0
    while not cycle.is_empty():
        v = cycle.pop()
        adj_copy[u].remove(v)
        adj_copy[v].remove(u)
        u = v
        count += 1

    new_graph = Graph(graph.V())
    new_graph._E = graph.E() - count
    for v in range(graph.V()):
        for w in adj_copy[v]:
            new_graph._adj[v].add(w)

    return new_graph


class CycleFromVertex:
    def __init__(self, G, start):
        self._marked = [False] * G.V()
        self._edge_to = [None] * G.V()
        self._cycle = None
        self._start = start

        self._dfs(G, -1, start)

    def _dfs(self, G, parent, v):
        self._marked[v] = True
        for w in G.adj(v):
            if self._cycle is not None:
                return
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(G, v, w)
            elif w != parent and w == self._start:
                # ciclo detectado envolvendo o vértice inicial
                self._cycle = Stack()
                self._cycle.push(self._start)
                # x = self._edge_to[v]
                x = v
                while x != self._start:
                    self._cycle.push(x)
                    x = self._edge_to[x]
                self._cycle.push(self._start)  # fecha o ciclo explicitamente

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        if self._cycle is None:
            return Stack()
        return self._cycle


class Hierholzer:
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def make_circuit(self, v: int):
        finder = CycleFromVertex(self.graph, v)
        cycle = finder.cycle()
        k = make_graph_without_cycle(self.graph, cycle)
        h = Stack()
        while k.E():
            w = self.get_vertex_from_cycle(k, cycle)
            finder = CycleFromVertex(k, w)
            h = finder.cycle()
            cycle = self.union(cycle, h)
            k = make_graph_without_cycle(self.graph, cycle)

        return cycle
    
    def get_vertex_from_cycle(self, k: Graph, cycle: Stack):
        for v in cycle:
            # d(v) > 0
            if not k.degree(v):
                continue

            return v
        return v
    
    def union(self, c: Stack, h: Stack):        
        result = []
        first_element = h.peek()
        is_first = True
        for v in c:
            if v == first_element and is_first:
                is_first = False
                for w in h:
                    result.append(w)

            else:
                result.append(v)

        stack = Stack()
        for v in reversed(result):
            stack.push(v)

        return stack

    def has_unexplored_edges(self):
        all_values = self.adj_copy.values()
        for values in all_values:
            if values:
                return True
            
        return False


if __name__ == '__main__':
    from os.path import join, dirname, abspath

    data_file = join(dirname(abspath(__file__)), '..', 'data', 'hierholzer.txt')
    g = Graph.from_txt(data_file)

    print(g)
    print('-=' * 20)

    hierholzer = Hierholzer(g)    
    print(print_letters(hierholzer.make_circuit(2)))
