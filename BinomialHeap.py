import BinomialTree


class BinomialHeap:
    ##
    # This class uses Binomial Tree into this module.
    # This class uses one or more Binomial Tree following min-Heap property and stores them in roots list.
    # There will be pointer to a node with minimum value which can be used to extract min from heap in O(1) time.
    ##

    def __init__(self, n=0):
        ##
        # Constructor for calling BinomialHeap class and create default heap with n number of nodes
        # @param n: intial number of nodes. By default it takes 0.
        ##

        ## contains list of roots of every Binomial Tree in Binomial Heap.
        self.head = []
        ## Has Address of root with minumum value
        self.minimum = None
        ## Number of nodes present in Binomial Heap.
        self.number_of_nodes = n

    def insert_tree(self, bt: BinomialTree):
        ##
        # Insert a Binomial Tree with one or more nodes.
        # @param bt: Address of Binomial Tree.
        ##
        self.head.append(bt)
        if self.minimum is None:
            self.minimum = bt
        else:
            if self.minimum.getValue() > bt.getValue():
                self.minimum = bt
        self.number_of_nodes += pow(2, bt.getDegree())
        self.merge()

    def merge(self):
        ##
        # Merge operation in Binomial Heap
        # @return Merged Binomial Heap
        ##
        array = [None for x in range(self.number_of_nodes)]
        for x in range(len(self.head)-1):
            if x >= len(self.head): break;
            degree = self.head[x].getDegree()
            if array[degree] is None:
                array[degree] = self.head[x]
            else:
                a = array[degree]
                b = self.head[x]
                c = a.merge_tree(b)
                if(self.minimum is a or self.minimum is b):
                    self.minimum = c
                del self.head[x]
                self.head.remove(array[degree])
                array[degree] = None
                self.head.append(c)
                del array[:]
                self.merge()

    def traverse_heap(self):
        ##
        # Displays every nodes in Binomial Heap.
        # Displayed Format will be list of roots available in head
        # followed by nodes in each root of the particular tree.
        ##
        for x in self.head:
            print('head = ', x.getValue(), '|', x.getData())
            x.traverse_tree()
            print()

    def delete_min(self) -> BinomialTree:
        ##
        # Delete min OR Extract min operation of Binomial Heap
        # @returns Address of node with extracted minimum value from Binomial Heap
        ##
        minimum_to_be_returned = self.minimum
        children = []
        if self.minimum.getChild() is not None:
            t = self.minimum.getChild()
            children.append(t)
            while t.getSibling() is not None and t.getSibling() is not self.minimum.getChild():
                children.append(t.getSibling())
                q = t.getSibling()
                t.setSibling(None)
                t = q
            t.setSibling(None)

        self.head.remove(self.minimum)
        self.number_of_nodes -= pow(2, self.minimum.getDegree())
        if len(self.head) is not 0:
            self.minimum = self.head[0]
            for x in self.head:
                if self.minimum.getValue() > x.getValue():
                    self.minimum = x
        else:
            self.minimum = None
        for x in children:
            self.insert_tree(x)

        return minimum_to_be_returned

    def insert(self, *value: int):
        ##
        # Insert operation of Binomial Heap
        # @param *value : list of nodes to be inserted
        ##
        for x in value:
            self.insert_tree(BinomialTree.BinomialTree(val=x))

    def search_heap(self, value: int) -> BinomialTree:
        ##
        # Search the heap by values of nodes
        # @param value: value by which node is to be searched for.
        # @returns Address of the node with available value
        ##
        for x in self.head:
            if x.search_node(value):
                return x
        return None

    def search_heap_by_data(self, data: int) -> BinomialTree:
        ##
        # Search the heap by data field of nodes
        # @param value: data field by which node is to be searched for.
        # @return Address of node with available data.
        ##
        for x in self.head:
            if x.search_node_by_data(data):
                return x
        return None

    def decrease_key(self, key: int, value: int):
        ##
        # Decreases key operation of binomial heap.
        # It works by searching the node with given value and decreasing that value to argument
        # @param key: value field of nodes on which decrease key operation is to be perfomed
        # @param value: Modified value of the node
        ##
        aux = self.search_heap(key)
        if aux is None:
            return -1
        aux.decrease_node_value(key, value)
        aux.validate()
        if self.         minimum.getValue() > aux.getValue():
            self.minimum = aux

    def decrease_key_by_data(self, key: int, new_value: int):
        ##
        # Decreases key operation of binomial heap.
        # This works by searching the node with given data and decreasing the value of that node to argument
        # @param key: data field of nodes on which decrease key operation is to be performed.
        # @param value: Modified value field of the node
        ##
        aux = self.search_heap_by_data(key)
        if aux is None:
            return -1
        aux.decrease_node_value_by_datasearch(key, new_value)
        aux.validate()
        if self.minimum.getValue() > aux.getValue():
            self.minimum = aux

    def isEmpty(self):
        ##
        # Checks if Heap is empty or not
        # @return TRUE is Binomial Heap is empty and as no roots, else FALSE.
        if len(self.head) < 1 or self.head is None:
            return True
        return False


def create_heap_from_list(llist: list) -> BinomialHeap:
    ##
    # Creates Default Binomial Heap from list of values
    # @param llist: list of values for Binomial Heap generation
    # @return Address of Binomial Heap
    ##
    bh = BinomialHeap()
    index = 0
    for x in llist:
        bh.insert_tree(BinomialTree.BinomialTree(val=x, data=index))
        index += 1
    return bh
