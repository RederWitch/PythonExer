
class Graph:

    def __init__(self, nodeNumber,  directed = False):
        self.nodeNumber = nodeNumber
        self.directed = directed

        self.nodes = []
        self.matrix = []
        for i in range(self.nodeNumber):
            self.matrix.append([])
            self.nodes.append(i)
        for i in range(self.nodeNumber):
            for j in range(self.nodeNumber):
                self.matrix[i].append(0)

    def add_node(self, node):           # dodaje wierzchołek
        pass

    def has_node(self, node):
        pass  # bool

    def __change_edge(self, source, destination, weight):
        if weight<0:
            raise IndexError
        self.matrix[source][destination] = weight
        if not self.directed:
            self.matrix[destination][source] = weight

    def add_edge(self, source, destination, weight=1):    # wstawienie krawędzi
        if not self.has_edge(source, destination):
            self.__change_edge(source, destination, weight)
        else:
            raise IndexError

    def has_edge(self, source, destination): # bool
        if self.matrix[source][destination] != 0:
            return True
        else:
            return False

    def del_edge(self, source, destination):   # usunięcie krawędzi
        if self.has_edge(source, destination):
            self.add_edge(source, destination, 0)
        else:
            raise IndexError

    def weight(self, source, destination): # zwraca wagę krawędzi
        if self.has_edge(source, destination):
            return self.matrix[source][destination]
        else:
            raise IndexError

    def change_edge(self, source, destination, weight):
        if self.has_edge(source, destination):
            self.__change_edge(source, destination, weight)

    def print_graph(self):
        for i in range(self.nodeNumber):
            print(self.matrix[i])

    def nodes_neigh(self, node):
        neigh = []

        for index in range(self.nodeNumber):
            if self.matrix[node][index] != 0:
                neigh.append(index)

        return neigh

