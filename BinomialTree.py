class BinomialTree(object):
    """
    This class is defined for a single tree or min-heap in Binomial Heap which has only one root and follows min-heap property.
    Every node is a object of Node class and has following data structure
    """
    def getValue(self):
        pass

    def getChild(self):
        pass

    def validate(self):
        pass

    def getData(self):
        pass

    def decrease_node_value_by_datasearch(self, data, finalval):
        pass


class BinomialTree:
    def __init__(self, val, degree=0, child=None, sibling=None, data=0):
        """
        Default constructor for calling Binomial Tree.
        :param val: represents value of root node where by value of the nodes in tree, min-heap property is satisfied
        :param degree: degree of the root node
        :param child: object to the child of root node
        :param sibling: sibling of root node if any, By default is set NULL
        :param data: data is like key which is unique to every node to identify any node
        """
        self.child = child
        self.degree = degree
        self.value = val
        self.sibling = sibling
        self.data = data

    def setDegree(self, degree):
        self.degree = degree

    def setValue(self, val):
        self.value = val

    def setSibling(self, bt):
        self.sibling = bt

    def setChild(self, bt):
        self.child = bt

    def getDegree(self):
        return self.degree

    def getValue(self):
        return self.value

    def getSibling(self) -> BinomialTree:
        return self.sibling

    def getChild(self) -> BinomialTree:
        return self.child

    def setData(self, data: int):
        self.data = data

    def getData(self):
        return self.data

    def traverse_tree(self):
        """
        This function displays every node of tree from root to leaves
        :return:
        """
        t = self
        print(t.getValue(), '|', t.getData(), end=' ')
        if t.getChild() is not None:
            t.getChild().traverse_tree()
        while t.getSibling() is not self and t.getSibling() is not None:
            t = t.getSibling()
            print(t.getValue(), '|', t.getData(), end=' ')
            if t.getChild() is not None:
                t.getChild().traverse_tree()

    def merge_tree(self, bt: BinomialTree) -> BinomialTree:
        """
        This function merges two trees if both their root's degrees are same. The root with higher value becomes child of other tree's root.
        :param bt: Binary Tree with same degree as this
        :return: Single Binary Tree with merged operation
        """
        if self.getValue() <= bt.getValue():
            if self.getChild() is not None:  # No Child then attach this as directly as child of itself.
                t = self.getChild()
                if t.getSibling() is not None:
                    bt.setSibling(t.getSibling())
                    t.setSibling(bt)
                else:
                    bt.setSibling(t)
                    t.setSibling(bt)
            else:
                self.setChild(bt)
            self.setDegree(self.getDegree() + 1)
            return self
        else:
            bt = bt.merge_tree(self)
            return bt

    def search_node(self, value: int) -> bool:
        flag = False
        t = self
        if t.getValue() is value:
            return True
        if t.getChild() is not None:
            flag = t.getChild().search_node(value)
            if flag:
                return True
        while t.getSibling() is not self and t.getSibling() is not None:
            t = t.getSibling()
            if t.getValue() == value:
                return True
            if t.getChild() is not None:
                flag = t.getChild().search_node(value)
                if flag:
                    return True
        return flag

    def search_node_by_data(self, data: int) -> bool:
        flag = False
        t = self
        if t.getData() is data:
            return True
        if t.getChild() is not None:
            flag = t.getChild().search_node_by_data(data)
            if flag:
                return True
        while t.getSibling() is not self and t.getSibling() is not None:
            t = t.getSibling()
            if t.getData() == data:
                return True
            if t.getChild() is not None:
                flag = t.getChild().search_node_by_data(data)
                if flag:
                    return True
        return flag

    def decrease_node_value(self, initval: int, finalval: int) -> bool:
        if self.getValue() is initval:
            self.setValue(finalval)
            return True
        if self.getChild() is not None:
            if self.getChild().decrease_node_value(initval, finalval):
                return True
        if self.getSibling() is not None:
            t = self
            while t.getSibling() is not None and t.getSibling() is not self:
                t = t.getSibling()
                if t.getValue() is initval:
                    t.setValue(finalval)
                    return True
                else:
                    if t.getChild() is not None:
                        if t.getChild().decrease_node_value(initval, finalval):
                            return True
        return False

    def decrease_node_value_by_datasearch(self, data: int, finalval: int) -> bool:
        if self.getData() is data:
            self.setValue(finalval)
            return True
        if self.getChild() is not None:
            if self.getChild().decrease_node_value_by_datasearch(data, finalval):
                return True
        if self.getSibling() is not None:
            t = self
            while t.getSibling() is not None and t.getSibling() is not self:
                t = t.getSibling()
                if t.getData() is data:
                    t.setValue(finalval)
                    return True
                else:
                    if t.getChild() is not None:
                        if t.getChild().decrease_node_value_by_datasearch(data, finalval):
                            return True
        return False

    def validate(self):
        children = []
        if self.getChild() is not None:
            t = self.getChild()
            for _ in range(self.getDegree()):
                children.append(t)
                t = t.getSibling()

            for x in children:
                x.validate()

            for x in children:
                if self.getValue() > x.getValue():
                    aux = self.getValue()
                    auxdata = self.getData()
                    self.setValue(x.getValue())
                    self.setData(x.getData())
                    x.setValue(aux)
                    x.setData(auxdata)
                    break


if __name__ == '__main__':
    print('Working in BinomialTree')
