import sys
from os.path import abspath, dirname, join
from graph import Graph
from fleury import Fleury
from hierholzer import Hierholzer
from utils import is_eulerian


def get_graph_from_stdin():
    lines = sys.stdin.read().strip().split('\n')
    V = int(lines[0])
    E = int(lines[1])
    g = Graph(V)
    for line in lines[2:2+E]:
        v, w = map(int, line.split())
        g.add_edge(v, w)

    return g


def hierholzer_algorithm(g):
    hierholzer = Hierholzer(g) 
    path = hierholzer.make_circuit()
    print("Caminho encontrado:", " - ".join(map(str, path)))


def fleury_algorithm(g):
    fleury = Fleury(g)
    path = fleury.find()

    tipo = fleury.is_eulerian()
    if tipo is None:
        print("O grafo não possui trilha nem circuito euleriano.")
    else:
        print("Caminho encontrado:", " - ".join(map(str, path)))


def select_algorithm():
    has_args = len(sys.argv) > 1
    return "Hierholzer" if has_args and sys.argv[1] == "hierholzer" else "Fleury"


def main():
    filepath = join(dirname(abspath(__file__)), '..', 'graph_input.txt')
    has_stdin = not sys.stdin.isatty()
    g = get_graph_from_stdin() if has_stdin else Graph.from_txt(filepath)
    try:        
        print("Grafo: ")
        print(g)
        print('-=' * 20)

        kind = is_eulerian(g)
        print(f"O grafo possui um(a) {kind} euleriano(a).")

        algorithm = select_algorithm()
        print(f"Usando o algoritmo de {algorithm}.")
        if algorithm == "Fleury":
            fleury_algorithm(g)
        else:
            hierholzer_algorithm(g)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
