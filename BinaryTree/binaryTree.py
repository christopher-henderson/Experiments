from functools import wraps
from BinaryTreeExceptions import *
from Node import Node

def NotEmpty(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        if self.isEmpty():
            raise EmptyTree()
        else:
            return function(self, *args, **kwargs)
    return wrapper

class BinaryTree(object):
    
    def __init__(self, *args):
        self.root = None
        if len(args) is 0:
            #===================================================================
            # Default, empty, constructor.
            # >>> tree = BinaryTree()
            #===================================================================
            pass
        elif isinstance(args[0], Node):
            #===================================================================
            # Use the given node as the root of this tree.
            #===================================================================
            self.root = args[0]
        elif '__iter__' in dir(args[0]):
            #===================================================================
            # Construct the binary tree using the given iterable.
            # >>> evens = BinaryTree(number for number in range(101) if number % 2 is 0)
            #===================================================================
            for element in args[0]:
                self.insert(element)
        else:
            #===================================================================
            # Construct the binary tree using all given elements.
            # >>> random = BinaryTree(56,7,2,5,8,23)
            #===================================================================
            for element in args:
                self.insert(element)
    
    def __contains__(self, element):
        return element in self.root
    
    def __str__(self):
        return str(self.inOrder())
    
    def isEmpty(self):
        return self.root is None
    
    def insert(self, element):
        if self.isEmpty():
            self.root = Node(element)
        else:
            self.root.insert(element)
        return self
    
    def inOrder(self):
        return tuple(item for item in self.root.inOrder())
    
    def preOrder(self):
        return tuple(item for item in self.root.preOrder())
    
    def postOrder(self):
        return tuple(item for item in self.root.postOrder())

    @NotEmpty
    def decendentsOf(self, element):
        return self.root.descendents(element)

    @NotEmpty
    def ancestorsOf(self, element):
        return tuple(ancestor for ancestor in self.root.ancestors(element))

    @NotEmpty
    def isAncestorOf(self, targetAncestor, targetDescendent):
        return self.root.isAncestorOf(targetAncestor, targetDescendent)

    @NotEmpty
    def isDescendentOf(self, targetDescendent, targetAncestor):
        return self.root.isAncestorOf(targetAncestor, targetDescendent)

    @NotEmpty
    def min(self):
        return self.root.min()

    @NotEmpty
    def max(self):
        return self.root.max()

    @NotEmpty
    def root(self):
        return self.root.element

    @NotEmpty
    def detachAt(self, element):
        return BinaryTree(self.root.detachAt(element))

    @NotEmpty
    def levelOf(self, element):
        return self.root.levelOf(element)

    @NotEmpty
    def height(self):
        return max(self.root.height())

    def attach(self, tree):
        if not isinstance(tree, BinaryTree):
            raise TypeError('Expected a Node. Received a {CLASS}'.format(CLASS=tree.__class__))
        if self.root is None:
            self.root = tree
        else:
            self.root.attach(tree.root)
        return self