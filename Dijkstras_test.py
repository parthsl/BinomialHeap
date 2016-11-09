import BinomialHeap
import BinaryHeap
import Dataset
import sys
import timeit

def dijkstra(graph, source):
    nodes = [x for x in range(len(graph))]
    distance_vector = [sys.maxsize for _ in range(len(nodes))]
    prev = [0 for _ in range(len(nodes))]
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
    nodes = [x for x in range(len(graph))]
    distance_vector = [sys.maxsize for _ in range(len(nodes))]
    prev = [0 for _ in range(len(nodes))]
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


if __name__ == '__main__':
    # Dataset.display_matrix(matrix)
    precision = 1000
    print('|V|--------------Binomial Heap--------------------Binary Heap-----------------------')
    for i in range(1,10):
        matrix = Dataset.get_matrix('random.txt', i*100)
        print(len(matrix),end='            ')

        start = timeit.default_timer()
        dist = dijkstra(matrix, 0)
        stop = timeit.default_timer()
        print((stop-start)*precision,end='                 ')

        start = timeit.default_timer()
        dist = dijkstras_by_binary_heap(matrix,0)
        stop = timeit.default_timer()
        print((stop-start)*precision)
