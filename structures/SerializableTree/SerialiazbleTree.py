'''
A serializable and deserializable binary tree.
'''

from random import randrange


class Node(object):

    '''
    A node of a given binary search tree. Holds a reference to its own value
    and to its two children. Values that less than or equal to this node are
    added to the left, values that are greater than this node are added to the
    right.
    '''

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

    def add(self, value):
        if self.value is None:
            self.value = value
            return
        if self < value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add(value)

    def serialize(self):
        return [self.value,
                self.left.serialize() if self.left is not None else [],
                self.right.serialize() if self.right is not None else []
                ]

    @staticmethod
    def deserialize(serialized_tree):
        root = Node(serialized_tree[0])
        if serialized_tree[1]:
            root.left = Node.deserialize(serialized_tree[1])
        if serialized_tree[2]:
            root.right = Node.deserialize(serialized_tree[2])
        return root

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    def equals(self, other):
        '''
        Recursive equality check for deep tree comparisons.
        For one-to-one node comparisons see Node.__eq__
        '''
        if not isinstance(other, Node):
            return False
        root_is_equal = self == other
        left_is_equal = self.left.equals(other.left) if self.left is not None else other.left is None
        right_is_equal = self.right.equals(other.right) if self.right is not None else other.right is None
        return root_is_equal and left_is_equal and right_is_equal

    def __bool__(self):
        return self.value is not None

    def __repr__(self):
        return "[<{ROOT}>, <{LEFT}> <{RIGHT}>]".format(
                ROOT=self.value,
                LEFT=self.left,
                RIGHT=self.right
            )

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        '''
        Simple one to one comparison. This simply tests the value of this
        node against the value of another (or a raw value). It does not test
        its children for equivalency. For deeper equivalency checks refer to
        Node.equals
        '''
        if self is other:
            return True
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
        '''
        Less than comparison against a single other node or a comparable
        raw value.

        E.G.
            Node(5) < Node(6)
        or
            Node(5) < 6
        '''
        if isinstance(other, Node):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        return not(self <= other)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return not self < other


class BinaryTree(object):

    '''
    A serializable and deserializable binary tree.
    '''

    def __init__(self, root=None):
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node()
            if hasattr(root, "__iter__"):
                # Construct the tree from an iterable of values.
                for value in root:
                    self.add(value)
            else:
                self.add(root)

    def add(self, value):
        self.root.add(value)

    def serialize(self):
        return self.root.serialize()

    @staticmethod
    def deserialize(serialized):
        return BinaryTree(Node.deserialize(serialized))

    def __eq__(self, other):
        if not isinstance(other, BinaryTree):
            return False
        if self is other:
            return True
        return self.root.equals(other.root)

    def __repr__(self):
        return self.root.__repr__()


def build_random_tree(n):
    # Build a binary tree from n number of random upper case ASCII characters.
    return BinaryTree(chr(randrange(65, 91)) for _ in range(n))


def test_binary_tree():
    for number_of_elements in range(100):
        binary_tree = build_random_tree(number_of_elements)
        serialized_tree = binary_tree.serialize()
        derived_tree = BinaryTree.deserialize(serialized_tree)
        deserialized_tree = derived_tree.serialize()
        # Assert that both instances of the tree are equivalent.
        assert binary_tree == derived_tree, '''
            FAILED to construct equivalent tree from serialized: {} :: {}
        '''.format(binary_tree, derived_tree)
        # Assert that both trees serialize to the same structure.
        assert serialized_tree == deserialized_tree, '''
            FAILED to serialize to the same structure: {} :: {}
        '''.format(serialized_tree, deserialized_tree)


def test_hardcoded_example():
    serialized = ['A', ['B', ['C', [], []], []], []]
    binary_tree = BinaryTree.deserialize(serialized)
    deserialized_tree = binary_tree.serialize()
    assert serialized == deserialized_tree, '''
        FAILED to serialize to same structure: {} :: {}
    '''.format(serialized, deserialized_tree)


def main():
    print ("Testing random trees.")
    test_binary_tree()
    print ("Testing hardcoded tree.")
    test_hardcoded_example()
    print ("SUCCESS")

main()
