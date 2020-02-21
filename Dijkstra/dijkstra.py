from graphs import *
from queue import *
from math import inf as infinity


def dijkstra(graph, start=0):
    was_considered = list()
    distance_cost = list()
    predecessors = list()
    queue = PriorityQueue()

    for node in range(graph.nodeNumber):
        # Q.add(node)
        was_considered.append(0)
        distance_cost.append(infinity)
        predecessors.append(-1)
        queue.enqueue(QueueItem(node, infinity))

    queue.change_el_priority(QueueItem(start, distance_cost[start]), 0)
    distance_cost[start] = 0  # cost edge start to self

    for i in range(graph.nodeNumber):
        node = queue.dequeue()
        node = node.name
        # print(" i in range i ={}, node = {}".format(i, node))
        was_considered[node] = 1
        for neigh in graph.nodes_neigh(node):
            # print(" neigh in range i ={}".format(neigh))
            if was_considered[neigh] == 0:
                cost_start_node_neigh = distance_cost[node] + graph.matrix[node][neigh]
                # cost of distance from Start through Node to Neigh
                if distance_cost[neigh] > cost_start_node_neigh:
                    queue.change_el_priority(QueueItem(neigh, distance_cost[neigh]),cost_start_node_neigh)
                    distance_cost[neigh] = cost_start_node_neigh
                    predecessors[neigh] = node
    print_result(distance_cost, predecessors, graph.nodeNumber)
#    result = list()
#    result.append(distance_cost)
#    result.append(predecessors)

#    return result


def print_result(distance, predecessors, nodeNumber):
    print("Results:")
    for index in range(nodeNumber):
        print("Node: {}\tDistance from Start: {}\t Predecessor: {}".format(index, distance[index], predecessors[index]))

