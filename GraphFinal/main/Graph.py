import math

class Graph(object):
    """Class definition of Graph"""

    def __init__(self, vertices = []):
        self.vertices = vertices

    def add_vertex(self, label):
        if (type(label) != str):
            raise ValueError("The label provided was not a String")
        self.vertices.append(Vertex(label))

    def add_edge(self, src, dest, weight):
        conditionS = False
        conditionD = False
        for vertex in self.vertices:
            if (src == vertex.name):
                conditionS = True
            if (dest == vertex.name):
                conditionD = True
        if (conditionS == False or conditionD == False):
           raise ValueError("That was an incorrect directive")
        

        for vertex in self.vertices:
            if (vertex.name == src):
                vertex.adjacency.append(Edge(dest, weight))
                if(len(vertex.edges) == 0):
                    vertex.edges.append(Edge(dest, weight))
                    break
                elif (vertex.edges[len(vertex.edges) - 1].weight < weight):
                    vertex.edges.append(Edge(dest, weight))
                    break
                elif(len(vertex.edges) == 1 and weight < vertex.edges[0].weight):
                    vertex.edges.insert(0, Edge(dest, weight))
                    break
                else:
                    for e in range(len(vertex.edges)):
                        if (weight >= vertex.edges[e].weight and weight <= vertex.edges[e + 1].weight):
                            vertex.edges.insert(e, Edge(dest, weight))
                            break
                

    def get_weight(self, src, dest):
         conditionS = False
         conditionD = False
         for vertex in self.vertices:
             if (src == vertex.name):
                 conditionS = True
             if (dest == vertex.name):
                 conditionD = True
         if (conditionS == False or conditionD == False):
            raise ValueError("That was an incorrect directive")
         

         for vertex in self.vertices:
            if (vertex.name == src):
                for e in vertex.edges:
                    if (e.destination == dest):
                        return e.weight
                return math.inf

    def dfs(self, start):
        for vertex in self.vertices:
            vertex.visited = False
        
        startCondition = False
        for vertex in self.vertices:
            if (start == vertex.name):
                startCondition = True
        if (startCondition == False):
            raise ValueError("The provided vertex is not contained in the graph")

        startVertex = None
        for vertex in self.vertices:
            if (vertex.name == start):
                startVertex = vertex
        for e in startVertex.edges:
            yield from Graph.dfs_recursive_helper(self.vertices, startVertex)

    def dfs_recursive_helper(lyst, vert):
        if(vert.visited == False):
            yield vert.name
        vert.visited = True
        for e in vert.edges:
            for vertex in lyst:
                if (e.destination == vertex.name):
                    if (vertex.visited == False):
                        yield from Graph.dfs_recursive_helper(lyst, vertex)



    def bfs(self, start):
        startVertex = None
        for vertex in self.vertices:
            if (vertex.name == start):
                startCondition = True
        if (startCondition == False):
            raise ValueError("The provided vertex is not contained in the graph")

        for vertex in self.vertices:
            vertex.visited = False
            if (vertex.name == start):
                startVertex = vertex

        yield startVertex.name
        startVertex.marked = True
        for count in range(len(self.vertices)):
            for e in startVertex.adjacency:
                if (startVertex.visited == False):
                    startVertex.visited = True
                for vertex in self.vertices:
                    if (vertex.name == e.destination):
                        if (vertex.marked == False):
                            yield vertex.name
                            vertex.marked = True

            for e in startVertex.adjacency:
                for vertex in self.vertices:
                    if (vertex.name == e.destination and vertex.visited == False):
                       startVertex = vertex
                       break
                break
                        
   # def dijkstra_shortest_path(src, dest):

   # def dijkstra_shortest_path(src):

    def __str__(self):
        graph = "numVertices: " + str(len(self.vertices)) + "\n"
        graph = graph  + "Vertex\tAdjacency List\n"
        for vertex in self.vertices:
            graph = graph + str(vertex)

        return str(graph)



class Vertex(object):

    def __init__(self, label = None):
        self.name = label
        self.edges = []
        self.adjacency = []
        self.visited = False
        self.marked = False

    def __str__(self):
        e = "["
        for ed in range(len(self.edges)):
            if (ed == (len(self.edges) - 1)):
                e = e + str(self.adjacency[ed])
            else:
                e = e + str(self.adjacency[ed]) + ", "

        e = e + "]"
        return "{}\t{}\n".format(self.name, e)


class Edge(object):

    def __init__(self, destination = None, weight = 0.0):
        self.destination = destination
        self.weight =  weight

    def __str__(self):
        return "('{}', {})".format(self.destination, self.weight)

 