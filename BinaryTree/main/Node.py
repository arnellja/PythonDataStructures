from recursioncounter import RecursionCounter # import recursion counter to be used by unit test.

class Node():
    """object definition fo a Node to be used in Binary Search Tree class"""


    def __init__(self, data): # constructor method for the Node class, including variables of left and right children for each node, data, and the height of a particular node.
        self.left_child = None
        self.right_child = None
        self.data = data
        self.height = 0

    def is_leaf(self): # used to check if a Node is a leaf of the Binary Search Tree.
        if (self.height == 0):
            return True
        else:
            return False
        
    def update_height(self): # updates the height of a node by one.
        self.height += 1

    def __str__(self): # to string method to be used for each node, printing the data, height for each Node, and specifies if Node.
        leaf = ""
        if (self.is_leaf()):
            leaf = " [leaf]"
        return "{} ({}){}".format(self.data, self.height, leaf)