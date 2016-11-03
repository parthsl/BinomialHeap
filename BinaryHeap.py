def create_heap_from_list(array_list):
    bh = BinaryHeap()
    for x in range(len(array_list)):
        bh.insert(array_list[x], x)
    return bh


class BinaryHeap:
    heap = []

    class Node:
        def __init__(self, value, data=0):
            self.value = value
            self.data = data

    def insert(self, value, data):
        self.heap.append(BinaryHeap.Node(value, data))
        inserted = len(self.heap) - 1
        parent = int(((inserted + 1) / 2) - 1)
        while parent >= 0:
            if self.heap[parent].value > self.heap[inserted].value:
                aux = self.heap[parent]
                self.heap[parent] = self.heap[inserted]
                self.heap[inserted] = aux
                inserted = parent
                parent = int(((inserted + 1) / 2) - 1)
                continue
            else:
                break;

    def min_heapify(self, node):
        left_child = 2 * (node + 1) - 1
        right_child = left_child + 1
        largest = node
        if left_child < len(self.heap) and self.heap[left_child].value<self.heap[largest].value:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child].value < self.heap[largest].value:
            largest = right_child
        if largest is not node:
            aux = self.heap[largest]
            self.heap[largest] = self.heap[node]
            self.heap[node] = aux
            self.min_heapify(largest)

    def delete_min(self):
        if len(self.heap) is not 0:
            minimum = self.heap[0]
            last = self.heap[len(self.heap)-1]
            self.heap.remove(last)
            if len(self.heap) is not 0:
                self.heap[0] = last
            self.min_heapify(0)
            return minimum
        else:
            return -1

    def traverse(self):
        for x in self.heap:
            print(x.value, '|', x.data)

    def search_by_data(self,data):
        for x in range(len(self.heap)):
            if self.heap[x].data == data:
                return x
        return -1

    def decrease_key_by_data(self,data,newValue):
        node_pos = self.search_by_data(data)
        self.heap[node_pos].value = newValue

        parent = int(((node_pos + 1) / 2) - 1)
        while parent >= 0:
            if self.heap[parent].value > self.heap[node_pos].value:
                aux = self.heap[parent]
                self.heap[parent] = self.heap[node_pos]
                self.heap[node_pos] = aux
                node_pos = parent
                parent = int(((node_pos + 1) / 2) - 1)
                continue
            else:
                break;

    def isEmpty(self):
        if len(self.heap) < 1:
            return True
        return False