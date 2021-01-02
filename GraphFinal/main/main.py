from Graph import Graph, Vertex, Edge


def main():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_edge("A", "B", 2.0)
    g.add_edge("A", "F", 9.0)
    g.add_edge("B", "F", 6.0)
    g.add_edge("B", "D", 15.0)
    g.add_edge("B", "C", 8.0)
    g.add_edge("C", "D", 1.0)
    g.add_edge("E", "C", 3.0)
    g.add_edge("E", "D", 7.0)
    g.add_edge("F", "B", 6.0)
    g.add_edge("F", "E", 3.0)
    print(g)
    print("starting DFS with vertex A")
    for vertex in g.dfs("A"):
        print("\t", vertex)


if (__name__ == "__main__"):
    main()
