from __future__ import division

class Node(object):
    
    def __init__(self, element, leftSide, rightSide, parent=None):
        self.element = element
        self.parent = parent
        if len(leftSide) is 0:
            self.left = None
        else:
            leftMiddle = len(leftSide)//2
            self.left = Node(leftSide[leftMiddle],
                             leftSide[:leftMiddle:],
                             leftSide[leftMiddle+1::],
                             parent=self)
        if len(rightSide) is 0:
            self.right = None
        else:
            rightMiddle = len(rightSide)//2
            self.right = Node(rightSide[rightMiddle],
                              rightSide[:rightMiddle:],
                              rightSide[rightMiddle+1::],
                              parent=self)

    def __contains__(self, other):
        if other == self.element:
            return True
        if self.left is not None and other in self.left:
            return True
        if self.right is not None and other in self.right:
            return True
        else:
            return False

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
            for element in self.left.preOrder():
                yield element
        if self.right:
            for element in self.right.preOrder():
                yield element
        yield self.element

class BinaryTree(object):
    
    def __init__(self, collection):
        sorted(collection)
        middle = len(collection) // 2
        self.root = Node(collection[middle],
                         collection[:middle:],
                         collection[middle+1::])
    
    def __contains__(self, element):
        return element in self.root
    
    def __str__(self):
        return str(self.list())
    
    def list(self, order='inOrder'):
        if order == 'inOrder':
            return [item for item in self.root.inOrder()]
        elif order == 'preOrder':
            return [item for item in self.root.preOrder()]
        elif order == 'postOrder':
            return [item for item in self.root.postOrder()]
        else:
            raise NotImplementedError('{ORDER} is not a supported algorithm.'.format(ORDER=order))