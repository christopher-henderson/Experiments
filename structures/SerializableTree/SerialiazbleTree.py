# binary tree
# class for a tree
# serializes into a file
# deserialzies
#

from random import randrange


class Node(object):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

    def add(self, node):
        if self <= node:
            if self.right is None:
                self.right = Node(node)
            else:
                self.right.add(node)
        else:
            if self.left is None:
                self.left = Node(node)
            else:
                self.left.add(node)

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
        # print ("hello from adding a right", value)
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    def equals(self, other):
        # Recursive equality rather than simple one-to-one node comparison.
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
        if self is other:
            return True
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
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

    def __init__(self, root=None):
        self.root = root if root is not None else Node()

    def add(self, value):
        if not self:
            self.value = value
        else:
            self.root.add(value)

    def serialize(self):
        if self.root is None:
            return [None, [], []]
        return self.root.serialize()

    @staticmethod
    def deserialize(serialized):
        return BinaryTree(Node.deserialize(serialized))

    def __eq__(self, other):
        if not isinstance(other, BinaryTree):
            return False
        if self is other:
            return True
        if self.root is None:
            return other.root is None
        return self.root.equals(other.root)

    def __repr__(self):
        return self.root.__repr__()


def build_random_tree(n):
    binary_tree = BinaryTree()
    for _ in range(n):
        # Add random characters from the [A-Z] ASCII range.
        character = chr(randrange(65, 91))
        binary_tree.add(character)
    return binary_tree


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
        # Asser that both trees serialize to the same structure.
        assert serialized_tree == deserialized_tree, '''
            FAILED to serialize to the same structure: {} :: {}
        '''.format(serialized_tree, deserialized_tree)


def main():
    print ("TESTING")
    test_binary_tree()
    print ("PASSED")

main()
