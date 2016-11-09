## @mainpage
# This Project is made to check the efficiency of BinomialHeap and BinaryHeap,
# implementing it in Dijkstras Algorithm to find single source shortest path.\n
# This project contains three main files representing class of Binomial Heap, Binary Heap and Dijkstra Algorithm.\n
# Since in Dijkstra algorithm, queue is build once and then extract minimum is done till queue is empty,
# we can take advantage of Heaps which has lower time complexity of extract minimum node.\n
# This is demonstrated in this project.
# This project is available at below link: \n
# <a href="https://github.com/parthsl/BinomialHeap">GitHub link</a>
# @author PARTH SHAH
# @author SHIVAM PRAJAPATI
##

def create_heap_from_list(array_list):
    ##
    # Creates Binary Heap from list of values
    # @returns Address of Binary Heap
    ##
    bh = BinaryHeap()
    for x in range(len(array_list)):
        bh.insert(array_list[x], x)
    return bh


class BinaryHeap:
    ##
    # This class creates Binary Heap following min-Heap property
    ##

    ## Binary Heap is maintained in dynamic list. Each node object is represented as one element of the list.
    heap = []

    class Node:
        ##
        # Each node conatins key-value pair. This class represents node's structure present in Binary Heap
        ##
        def __init__(self, value, data=0):
            ##
            # Constructor with default values and data
            ##

            ## Value from key-value pair in Binary Heap Nodes
            self.value = value
            ## Data Represents Key from key-value pair in BinaryHeap Nodes
            self.data = data

    def insert(self, value, data):
        ##
        # Insert operation on BinaryHeap
        # @param value: value field of the new node to be inserted
        # @param data: data field of new node
        ##
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
        ##
        # Min heapify operation to maintain min-heap property by Binary Heap
        # @param node: Address of node from where to check validation of heap
        ##
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
        ##
        # Delete or Extract minimum operation on BinaryHeap
        # @return Address of minimum node extracted based on value
        ##
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
        ##
        # To display data available in BinaryHeap
        # Displayed Data will be in Value|Data manner
        for x in self.heap:
            print(x.value, '|', x.data)

    def search_by_data(self,data):
        ##
        # Searches the node with given data
        # @param data: data field of node to be searched for.
        # @return Address of the node or if not found then returns -1.
        ##

        for x in range(len(self.heap)):
            if self.heap[x].data == data:
                return x
        return -1

    def decrease_key_by_data(self,data,newValue):
        ##
        # Decrease key operation on BinaryHeap
        # It decrease node's value searched using data field
        # @param data: data field to be searched for
        # @param newValue: Update the searched node to this new value
        ##
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
        ##
        # Checks if Binaryheap is empty or not
        # @return TRUE if BinaryHeap is empty and has no nodes else returns FALSE
        ##
        if len(self.heap) < 1:
            return True
        return False