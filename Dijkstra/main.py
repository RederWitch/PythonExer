from graphs import *
from  dijkstra import *

AlreadyExistError = "AlreadyExistError"

graph = None

def set_up():
    global graph
    print("Hello")
    print("Welcome to my Dijkstra project")
    print("Please enter the date following the instructions")
    while True:
        print("Please insert the number of nodes in your Graph")
        print("You can use a default Graph by inserting \"def\"")
        nodeNumber = input("Number of nodes: ")
        try:
            nodeNumber = int(nodeNumber)
        except ValueError:
            if nodeNumber == "def":
                make_def_graph()
                break
            else:
                print("This is not a number, try again")
                continue
        else:
            graph = Graph(nodeNumber)
            insert_edges()
            break


def insert_edges():
    global graph
    print("Insert edges of your graph by inserting 3 numbers\n"
          "index of Start End and Cost of the edge\n"
          "separated by white space. START END COST")
    print("To end adding of edges insert \"end\"")
    print("But please be careful I have not provided any way to correct"
          "inserted edges yet")
    while True:
        edge = input("Edge: ")
        edge = edge.split()
        if len(edge) == 1:
            if edge[0] == "end":
                break
            else:
                print("Unknown comand")
                continue
        elif len(edge) == 3:
            try:
                start = int(edge[0])
                end = int(edge[1])
                cost = int(edge[2])
            except ValueError:
                print("This is not a number, try again")
                continue
            else:
                try:
                    graph.add_edge(start, end, cost)
                except IndexError:
                    print("Edge with these nodes was has been crated alredy")
                    continue
        else:
            print("Something went wrong try again")
            continue

def insert_start_node():
    print("Now insert the number of node\n"
          "You want start Dijkstra algorithm")
    while True:
        node = input("Insert index of start node: ")
        try:
            node = int(node)
        except ValueError:
            print("This is not a number")
            continue
        else:
            if node < 0:
                print("Index can not be negative")
                continue
            elif node > graph.nodeNumber:
                print("Index can not be higher than number of nodes")
                continue
            else:
                return node


def make_def_graph():
    global graph
    graph = Graph(6)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 4, 1)
    graph.add_edge(0, 5, 7)

    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 4)
    graph.add_edge(1, 5, 12)

    graph.add_edge(2, 5, 4)

    graph.add_edge(3, 5, 6)

    graph.add_edge(4, 5, 2)



set_up()
node_start = insert_start_node()
print("\n\n")
print("Look matrix of your graph:")
graph.print_graph()
print("\n\n")
dijkstra(graph, node_start)