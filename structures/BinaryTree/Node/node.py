from BinaryTreeExceptions import *

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

    def height(self, height=-1):
        height += 1
        if self.left is None:
            yield height
        else:
            yield max(self.left.height(height))
        if self.right is None:
            yield height
        else:
            yield max(self.right.height(height))

    def levelOf(self, element, level=0):
        if element == self.element:
            return level
        elif element < self.element and self.left is not None:
            return self.left.levelOf(element, level+1)
        elif element > self.element and self.right is not None:
            return self.right.levelOf(element, level+1)
        else:
            raise NoSuchElement(element)

    def isAncestorOf(self, targetAncestor, targetDescendant, ancestorSeen=False):
        if targetAncestor == self.element:
            ancestorSeen = True
        if targetDescendant == self.element:
            #===================================================================
            # This covers the case of checking duplicate values within the tree
            # which can result in similar values having an ancestor/descendant
            # relationship. But ONLY if there actually are duplicates.
            # If the programmer does isAncestorOf(5,5) and there is only one five,
            # then the answer is - no, five is not its own ancestor/descendant.
            #===================================================================
            if targetAncestor == targetDescendant:
                if self.right is not None:
                    return self.right.element == targetDescendant
                else:
                    return False
            else:
                return ancestorSeen
        elif targetDescendant < self.element and self.left is not None:
            return self.left.isAncestorOf(targetAncestor, targetDescendant, ancestorSeen)
        elif targetDescendant > self.element and self.right is not None:
            return self.right.isAncestorOf(targetAncestor, targetDescendant, ancestorSeen)
        else:
            raise NoSuchElement(targetDescendant)

    def descendants(self, element):
        '''
        @return tuple of the target element's descendants.
        '''
        if element == self.element:
            return tuple([descendant for descendant in self._buildDescendants()])
        elif element < self.element and self.left is not None:
            return self.left.descendants(element)
        elif element > self.element and self.right is not None:
            return self.right.descendants(element)
        else:
            raise NoSuchElement(element)

    def _buildDescendants(self):
        '''
        @return Generator of this node's descendants traversed in order.
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
            pass
        elif element < self.element and self.left is not None:
            yield self.element
            for ancestor in self.left.ancestors(element):
                yield ancestor
        elif element > self.element and self.right is not None:
            yield self.element
            for ancestor in self.right.ancestors(element):
                yield ancestor
        else:
            raise NoSuchElement(element)

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