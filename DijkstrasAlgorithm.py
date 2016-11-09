import BinomialHeap
import BinaryHeap
import sys


class Dijkstras:
    """
    This class represents two method to find Dijkstras algorithm to find single source shortest path:
        -Dijkstras algorithms by using Binomial Heap
        -Dijkstras algorithms by using Binary Heap
    """

    def dijkstra_by_BinomialHeap(graph, source):
        ##
        # Dijkstras algorithm to find single source shortest path by using Binomial Heap
        # @param graph: Adjacency matrix of the graph as input
        # @param source: source node of the graph
        # @return distance matrix as list of every node from source node
        ##
        nodes = [x for x in range(len(graph))]
        distance_vector = [sys.maxsize for _ in range(len(nodes))]
        prev = [0 for _ in range(len(nodes))]

        ## Q is Binomial Heap maintained as key with node's number and value with distance of each node from source.
        Q = BinomialHeap.create_heap_from_list([sys.maxsize for _ in range(len(nodes))])
        u = source
        Q.decrease_key_by_data(u, 0)
        distance_vector[u] = 0
        while not Q.isEmpty():
            u = Q.delete_min().getData()
            for x in range(len(graph)):
                if graph[u][x] == 0:
                    alt = sys.maxsize
                else:
                    alt = distance_vector[u] + graph[u][x]
                if distance_vector[x] > alt:
                    distance_vector[x] = alt
                    Q.decrease_key_by_data(x, alt)
                    prev[x] = u
        return distance_vector

    def dijkstras_by_binary_heap(graph, source):
        ##
        #  Dijkstras algorithm to find single source shortest path by using Binary Heap
        # @param graph: Adjacency matrix of the graph as input
        # @param source: source node of the graph
        # @return distance matrix as list of every node from source node
        ##
        nodes = [x for x in range(len(graph))]
        distance_vector = [sys.maxsize for _ in range(len(nodes))]
        prev = [0 for _ in range(len(nodes))]

        ## Q is Binary Heap maintained as key with node's number and value with distance of each node from source.
        Q = BinaryHeap.create_heap_from_list([sys.maxsize for _ in range(len(nodes))])
        u = source
        Q.decrease_key_by_data(u, 0)
        distance_vector[u] = 0
        while not Q.isEmpty():
            u = Q.delete_min().data
            for x in range(len(graph)):
                if graph[u][x] == 0:
                    alt = sys.maxsize
                else:
                    alt = distance_vector[u] + graph[u][x]
                if distance_vector[x] > alt:
                    distance_vector[x] = alt
                    Q.decrease_key_by_data(x, alt)
                    prev[x] = u
        return distance_vector

