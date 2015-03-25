from functools import wraps

class BinaryTreeError(Exception):
    pass

class EmptyTree(BinaryTreeError):
    def __init__(self):
        pass
    def __str__(self):
        return 'Binary Tree is empty.'

class NoSuchElement(BinaryTreeError):
    def __init__(self, element):
        self.element = element
    def __str__(self):
        return '{ELEMENT} could not be found.'.format(ELEMENT=self.element)

def NotEmpty(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        if self.isEmpty():
            raise EmptyTree()
        else:
            return function(self, *args, **kwargs)
    return wrapper

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

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.left is None and self.right is None

    def isInnerNode(self):
        return not self.isRoot() and not self.isLeaf()

    def descendents(self, element):
        '''
        @return tuple of the target element's descendents.
        '''
        if element == self.element:
            return tuple([descendent for descendent in self._buildDescendents()])
        elif element < self.element and self.left is not None:
            return self.left.descendents(element)
        elif element > self.element and self.right is not None:
            return self.right.descendents(element)
        else:
            raise NoSuchElement(element)

    def _buildDescendents(self):
        '''
        @return Generator of this node's descendents traversed in order.
        '''
        if self.left:
            for element in self.left.inOrder():
                yield element
        if self.right:
            for element in self.right.inOrder():
                yield element

    def ancestors(self, element):
        '''
        @param element: Target element whose ancestors we want.
        @return tuple of the target element's ancestors.
        @
        '''
        if element == self.element:
            return tuple([ancestor for ancestor in self._buildAncestors()])
        elif element < self.element and self.left is not None:
            return self.left.ancestors(element)
        elif element > self.element and self.right is not None:
            return self.right.ancestors(element)
        else:
            raise NoSuchElement(element)

    def _buildAncestors(self):
        '''
        @return Generator of this node's ancestors traversed in order.
        '''
        if not self.isRoot():
            yield self.parent.element
            for ancestor in self.parent._buildAncestors():
                yield ancestor

    def min(self):
        if self.left is not None:
            return self.left.min()
        else:
            return self.element

    def max(self):
        if self.right is not None:
            return self.right.max()
        else:
            return self.element

    def insert(self, element):
        '''
        @param element: Element to insert into the tree.
        '''
        if element >= self.element:
            if self.right is not None:
                self.right.insert(element)
            else:
                self.right = Node(element, parent=self)
        elif element < self.element:
            if self.left is not None:
                self.left.insert(element)
            else:
                self.left = Node(element, parent=self)

    def attach(self, root):
        '''
        @param element: Element to insert into the tree.
        '''
        if root.element >= self.element:
            if self.right is None:
                self.right = root
            else:
                self.right.attach(root)
        elif root.element < self.element:
            if self.left is None:
                self.left = root
            else:
                self.left.attach(root)

    def _detach(self):
        if self.parent.left == self:
            self.parent.left = None
        elif self.parent.right == self:
            self.parent.right = None
        return self

    def detachAt(self, element):
        if element == self.element:
            return self._detach()
        elif self.left and element < self.element:
            return self.left.detachAt(element)
        elif self.right and element > self.element:
            return self.right.detachAt(element)
        else:
            raise NoSuchElement(element)

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
        return str(self.list())
    
    def isEmpty(self):
        return self.root is None
    
    def insert(self, element):
        if self.isEmpty():
            self.root = Node(element)
        else:
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
    
    @NotEmpty
    def decendentsOf(self, element):
        return self.root.descendents(element)

    @NotEmpty
    def ancestorsOf(self, element):
        return self.root.ancestors(element)

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

    def attach(self, tree):
        if self.root is None:
            self.root = tree
        else:
            self.root.attach(tree.root)