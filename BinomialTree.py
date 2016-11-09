class BinomialTree(object):
    """
    This class is defined for a single tree or min-heap in Binomial Heap which has only one root and follows min-heap property.
    Every node is a object of Node class and has a key-value pair along with other data like address of child, address of sibling and degree of that node.
    """

class BinomialTree:
    def __init__(self, val, degree=0, child=None, sibling=None, data=0):
        ##
        # Default constructor for calling Binomial Tree.
        # @param val: represents value of root node where by value of the nodes in tree, min-heap property is satisfied
        # @param degree: degree of the root node
        # @param child: object to the child of root node
        # @param sibling: sibling of root node if any, By default is set NULL
        # @param data: data is like key which is unique to every node to identify any node
        ##

        ## Stores the address of the child node. If there are no child of the node, then stores NULL.
        self.child = child
        ## Stores integer representing degree of the node. Degree refers to number of child of the node
        self.degree = degree
        ## Stores value from key-value pair. Binomial Tree follows min-Heap property on basis of this value.
        self.value = val
        ## Stores address of sibling of the node. By Default is set to NULL.
        self.sibling = sibling
        ## Stores key from key-value pair. Since keys are unique and so is the data field are also unique in while Binomial Tree.
        self.data = data

    def setDegree(self, degree):
        ##
        # Setter method to set degree of node
        # @param degree: sets degree of node to arguments value
        ##
        self.degree = degree

    def setValue(self, val):
        ##
        # Setter method to set Value of node
        # @param val: sets value of node to arguments value
        ##
        self.value = val

    def setSibling(self, bt):
        ##
        # Setter method to set sibling of node
        # @param degree: sets address of sibling of the node to arguments value
        ##
        self.sibling = bt

    def setChild(self, bt):
        ##
        # Setter method to set child of node
        # @param degree: sets address of child of node to arguments value
        ##
        self.child = bt

    def getDegree(self):
        ##
        # Getter method to get degree of node
        # @returns: degree of the node.
        ##
        return self.degree

    def getValue(self):
        ##
        # Getter method to get value of node
        # @returns: Value of the node.
        ##
        return self.value

    def getSibling(self) -> BinomialTree:
        ##
        # Getter method to get Sibling of node
        # @returns: Address of the Sibling of the node.
        ##
        return self.sibling

    def getChild(self) -> BinomialTree:
        ##
        # Getter method to get Child of node
        # @returns: Address of the Child of the node.
        ##
        return self.child

    def setData(self, data: int):
        ##
        # Setter method to set Data field of node
        # @param data: Sets data of the node to argument's value.
        ##
        self.data = data

    def getData(self):
        ##
        # Getter method to get Data of node
        # @returns: Data of the node.
        ##
        return self.data

    def traverse_tree(self):
        ##
        # This function displays every node of tree from root to leaves
        # displayed format will be value | data.
        ##

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
        ##
        # This function merges two trees if both their root's degrees are same.
        # The root with higher value becomes child of other tree's root.
        # @param bt: Binary Tree with same degree as this
        # @return Single Binary Tree with merged operation
        ##
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
        ##
        # To search any node by value
        # @param value: value on the basis of which node will be sarched
        # @return TRUE if node with given value is present, else FALSE if not
        ##
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
        ##
        # To search node in Binomial Tree by data.
        # @param data: data by which node is to be searched
        # @return TRUE if node with given data is present, else FALSE if not.
        ##
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
        ##
        # This function is used to decrease node's value by searching through the value only.
        # Since there may be more than one node with same value, first node in searching is selected.
        # @param initval: node to be searched for
        # @param finalval: value to be decreased to this finalvalue.
        # @return TRUE if operation of decrease key is successful else FALSE
        ##
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
        ##
        # This function is used to decrease node's value by searching through the data.
        # There can be only one node with given data because data field is unique in whole tree.
        # @param data: node to be searched for with given data
        # @param finalval: value to be decreased to this finalvalue.
        # @return TRUE if operation of decrease key is successful else FALSE
        ##
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
        ##
        # This function validates Binomial Tree by checking if min-heap property is followed or not.
        # If not then it will rearrange nodes to follow min-heap property
        ##
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
