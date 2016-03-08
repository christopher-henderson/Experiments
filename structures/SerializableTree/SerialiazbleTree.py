# binary tree
# class for a tree
# serializes into a file
# deserialzies
#


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

    def add(self, node):
        pass

    def serialize(self, serialized):
        sub_serialized = list()
        sub_serialized.append(self.value)
        sub_serialized.append(
            self.left.serialize(
                sub_serialized) if self.left is not None else [])
        sub_serialized.append(
            self.right.serialize(
                sub_serialized)if self.right is not None else [])
        serialized.append(sub_serialized)
        return sub_serialized

    @staticmethod
    def deserialize(serialzied):
        print (serialzied)
        if len(serialzied) is 1:
            return Node(serialzied[0])
        root = Node(serialzied[0])
        if len(serialzied[1]) is not 0:
            root.left = Node.deserialize(serialzied[1])
        else:
            root.left = None
        if len(serialzied[2]) is not 0:
            root.right = Node.deserialize(serialzied[2])
        else:
            root.right = None
        return root


    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        # print ("hello from adding a right", value)
        self._right = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def add(self, node):
        self.root.add(node)

    def serialize(self):
        serialzied = list()
        return self.root.serialize(serialzied)

    def deserialize(self, serialzied):
        # [A (B (C) ()) ()]
        self.root = Node.deserialize(serialzied)


def main():
    serialzied = ['A', ['B', ['C'], []], []]
    tree = BinaryTree()
    tree.deserialize(serialzied)
    print (tree.serialize())

main()

# me (left) (right)
# A (B (C) ()) ()
# A (B) (C)

# in order order
#     left me right

# pre order
#     me left right