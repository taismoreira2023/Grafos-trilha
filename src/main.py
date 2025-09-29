from os.path import join, dirname, abspath
from graph import Graph
from fleury import Fleury

def main():
    filepath = join(dirname(abspath(__file__)), '..', 'graph_input.txt')
    g = Graph.from_txt(filepath)
    print(g)
    fleury = Fleury(g)
    path = fleury.find()

    tipo = fleury.is_eulerian()
    if tipo is None:
        print("O grafo não possui trilha nem circuito euleriano.")
    else:
        print(f"O grafo possui um(a) {tipo} euleriano(a).")
        print("Caminho encontrado:", " - ".join(map(str, path)))

if __name__ == "__main__":
    main()