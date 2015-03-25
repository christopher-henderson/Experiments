from __future__ import division 

class Node(object):
    
    def __init__(self, element, parent=None):
        self.element = element
        self.parent = parent
        self.left = None
        self.right = None

    def __contains__(self, other):
        if other == self.element:
            return True
        elif other < self.element and self.left is not None:
            return other in self.left
        elif other > self.element and self.right is not None:
            return other in self.right
        else:
            return False

    def insert(self, other):
        if other >= self.element:
            if self.right is not None:
                self.right.insert(other)
            else:
                self.right = Node(other, parent=self)
        elif other < self.element:
            if self.left is not None:
                self.left.insert(other)
            else:
                self.left = Node(other, parent=self)

    def inOrder(self):
        if self.left:
            for element in self.left.inOrder():
                yield element
        yield self.element
        if self.right:
            for element in self.right.inOrder():
                yield element

    def preOrder(self):
        yield self.element
        if self.left:
            for element in self.left.preOrder():
                yield element
        if self.right:
            for element in self.right.preOrder():
                yield element

    def postOrder(self):
        if self.left:
            for element in self.left.postOrder():
                yield element
        if self.right:
            for element in self.right.postOrder():
                yield element
        yield self.element

class BinaryTree(object):
    
    def __init__(self, collection):
        self.root = Node(collection[0])
        for item in collection[1::]:
            self.root.insert(item)
    
    def __contains__(self, element):
        return element in self.root
    
    def __str__(self):
        return str(self.list())
    
    def insert(self, element):
        self.root.insert(element)
    
    def list(self, order='inOrder'):
        if order == 'inOrder':
            return [item for item in self.root.inOrder()]
        elif order == 'preOrder':
            return [item for item in self.root.preOrder()]
        elif order == 'postOrder':
            return [item for item in self.root.postOrder()]
        else:
            raise NotImplementedError('{ORDER} is not a supported traversal algorithm.'.format(ORDER=order))


tree = BinaryTree([72,61,73])
print (tree.list(order='postOrder'))