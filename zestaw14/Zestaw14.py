from graph import *

#ZAD 1 zestaw 14
def list_nodes(graph):
    """ Moj klasa grafu posiada listę przechowującą indexy wierzchołków stąd:"""
    return graph.nodes
    """W przypadku braku takiej listy:"""
    """nodes = list()
    for node in range(graph.nodeNumber):
        nodes.append(node)
    return nodes"""

def list_edges(graph):
    edges = list()
    neighbours = list()
    for node in list_nodes(graph):
        neighbours = graph.nodes_neigh(node)
        for neigh in neighbours:
            edges.append((node, neigh))
    return edges


def count_nodes(graph):
    return graph.nodeNumber

def count_edges(graph):
    return len(list_edges(graph))

""" zad 6 zestaw 14
    Dla grafów nieskierowanych w Pythonie napisać funkcję tworzącą słownik,
    w którym kluczami będą wierzchołki, a wartościami liczby krawędzi
    wychodzących z wierzchołka (stopnie wierzchołków). """
def nodes_grades(graph):
    nodes_grade = dict()
    nodes = list_nodes(graph)
    for node in nodes:
        nodes_grade[node] = len(graph.nodes_neigh(node))
    return nodes_grade


graf = Graph(5, 1)
graf.add_edge(0, 1)
graf.add_edge(0, 2)
graf.add_edge(1, 4)
graf.add_edge(1, 3)
graf.add_edge(2, 0)
graf.add_edge(2, 4)
graf.add_edge(2, 3)
graf.add_edge(3, 2)
graf.add_edge(4, 0)
graf.add_edge(4, 3)
print()
graf.print_graph()

print("List of nodes:")
print(list_nodes(graf))

print("List of edges:")
print(list_edges(graf))

print("Number of nodes:")
print(count_nodes(graf))

print("Number of edges:")
print(count_edges(graf))

print("Nodes grades:")
print(nodes_grades(graf))


