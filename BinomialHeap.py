import BinomialTree


class BinomialHeap:
    def __init__(self, n=0):
        self.head = []
        self.minimum = None
        self.number_of_nodes = n

    def insert_tree(self, bt: BinomialTree):
        self.head.append(bt)
        if self.minimum is None:
            self.minimum = bt
        else:
            if self.minimum.getValue() > bt.getValue():
                self.minimum = bt
        self.number_of_nodes += pow(2, bt.getDegree())
        self.merge()

    def merge(self):
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
        for x in self.head:
            print('head = ', x.getValue(), '|', x.getData())
            x.traverse_tree()
            print()

    def delete_min(self) -> BinomialTree:
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
        for x in value:
            self.insert_tree(BinomialTree.BinomialTree(val=x))

    def search_heap(self, value: int) -> BinomialTree:
        for x in self.head:
            if x.search_node(value):
                return x
        return None

    def search_heap_by_data(self, data: int) -> BinomialTree:
        for x in self.head:
            if x.search_node_by_data(data):
                return x
        return None

    def decrease_key(self, key: int, value: int):  # it decreases by value
        aux = self.search_heap(key)
        if aux is None:
            return -1
        aux.decrease_node_value(key, value)
        aux.validate()
        if self.         minimum.getValue() > aux.getValue():
            self.minimum = aux

    def decrease_key_by_data(self, key: int, new_value: int):
        aux = self.search_heap_by_data(key)
        if aux is None:
            return -1
        aux.decrease_node_value_by_datasearch(key, new_value)
        aux.validate()
        if self.minimum.getValue() > aux.getValue():
            self.minimum = aux

    def isEmpty(self):
        if len(self.head) < 1 or self.head is None:
            return True
        return False


def create_heap_from_list(llist: list) -> BinomialHeap:
    bh = BinomialHeap()
    index = 0
    for x in llist:
        bh.insert_tree(BinomialTree.BinomialTree(val=x, data=index))
        index += 1
    return bh
