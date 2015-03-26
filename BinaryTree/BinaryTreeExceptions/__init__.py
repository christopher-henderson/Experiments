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

class UnsupportedTraversalError(BinaryTreeError):
    def __init__(self, algorithm):
        self.algorithm = algorithm
    def __str__(self):
        return '{ALGORITHM} is not a supported traversal algorithm.'.format(ORDER=self.algorithm)