from recursioncounter import RecursionCounter # import recursion counter.

class BinarySearchTree():
    """object definition for a binary search tree"""

    def __init__(self): # constructor for Binary Search Tree with variable of root of tree.
        self.root = None

    def is_empty(self): # checks if Binary Search Tree is empty.
        if (self.root == None):
            return True
        else:
            return False

    def add_helper(cursor, data): # recursive helper for the add function. Finds location where a new node should be inserted.
        RecursionCounter()
        if (cursor.data == data):
            print("Duplicate Data Provided")
            return 0
        if (data < cursor.data):
            if (cursor.left_child == None):
                cursor.left_child = Node(data)
                if (cursor.right_child == None):
                    return 1
                return 0
            elif (data > cursor.left_child.data):
                newNode = Node(data)
                newNode.height = cursor.height - 1
                cursor.left_child.right_child = newNode
                return 0
            else:
                return BinarySearchTree.add_helper(cursor.left_child, data)
        else:
            if (cursor.right_child == None):
                cursor.right_child = Node(data)
                if (cursor.left_child == None):
                    return 1
                return 0
            elif (data < cursor.right_child.data):

                newNode = Node(data)
                cursor.right_child.left_child = newNode
                return 0
            else:
                return BinarySearchTree.add_helper(cursor.right_child, data)    

    def add(self, data): # add method used to add new nodes to the Binary Search Tree.
        if (self.root == None):
            self.root = Node(data)
            self.root.height = 1
        elif (self.root.data == data):
            print("Duplicate Data Provided")
        elif (self.root.data < data):
            if (self.root.right_child == None):
                self.root.right_child = Node(data)
            else:
                self.root.height += BinarySearchTree.add_helper(self.root.right_child, data)
        else:
            if (self.root.left_child == None):
                self.root.left_child = Node(data)
            else:
                self.root.height += BinarySearchTree.add_helper(self.root.left_child, data)

    def remove(self, data): # used to remove a requested node from the Binary Search Tree.
        if (self.root.data == data):
            if (self.root.right_child == None and root.left_child == None):
                self.root = None
            elif (self.root.right_child == None):
                self.root.left_child.height = self.root.height - 1
                self.root = self.root.left_child
            elif (self.root.right_child.left_child == None):
                self.root.right_child.left_child = self.root.left_child
                self.root.right_child.height = self.root.height - 1
                self.root = self.root.right_child
            else:
                self.root.right_child.left_child.left_child = self.root.left_child
                self.root.right_child.left_child.right_child = self.root.right_child
                self.root.right_child.left_child.height = self.root.height - 1
                self.root = self.root.right_child.left_child
                self.root.right_child.left_child = None
        elif (self.root.data < data):
            BinarySearchTree.remove_helper(self.root, self.root.right_child, data)
        else:
            BinarySearchTree.remove_helper(self.root, self.root.left_child, data)

    def remove_helper(precursor, cursor, data): # recursive helper for remove function, for finding nodes past root to remove.
        RecursionCounter()
        if (cursor.data == data):
            if (cursor.right_child == None and cursor.left_child == None):
                if (precursor.right_child == cursor):
                    precursor.right_child = cursor.right_child
                else:
                    precursor.left_child = cursor.left_child
            elif (cursor.right_child == None):
                cursor.data = cursor.left_child.data
                cursor.right_child = cursor.left_child.right_child
                cursor.left_child = None
            elif (cursor.right_child.left_child == None):
                cursor.data = cursor.right_child.data
                cursor.right_child = None
            else:
                cursor.data = cursor.right_child.left_child.data
                cursor.right_child.left_child = None
        else:
            if (cursor.right_child == None and cursor.left_child == None):
                return False
            elif (cursor.data < data):
                BinarySearchTree.remove_helper(cursor, cursor.right_child, data)
            else:
                BinarySearchTree.remove_helper(cursor, cursor.left_child, data)

    def find(self, data): # used to find node with given data in tree, returns Node.
        if (self.root == None):
            return None
        elif (self.root.data == data):
            return root
        elif (self.root.data < data):
            if (self.root.right_child == None):
                return None
            else:
                return BinarySearchTree.find_helper(data, root.right_child)
        else:
            if (self.root.left_child == None):
                return None
            else:
                return BinarySearchTree.find_helper(data, self.root.left_child)


    def find_helper(data, cursor): # recursive helper for the find function.
        RecursionCounter()
        if (cursor.data == data):
            return cursor
        if (cursor.data < data):
            if (cursor.right_child == None):
                return None
            elif (cursor.right_child > data):
                return None
            else:
                return BinarySearchTree.find_helper(data, cursor.right_child)
        else:
            if (cursor.left_child == None):
                return None
            elif (cursor.left_child.data < data):
                return None
            else:
                return BinarySearchTree.find_helper(data, cursor.left_child)

    def rebalance_tree(self): # method used to rebalance an unbalanced Binary Search Tree.
        list = self.inorder()
        self.root = None
        self.add(list[(len(list) // 2)])
        BinarySearchTree.rebalance_helper(self, list[0: (len(list) // 2)])
        BinarySearchTree.rebalance_helper(self, list[(len(list) // 2 + 1): len(list)])
        BinarySearchTree.set_heights(self.root)

    def rebalance_helper(tree, list): # recursive helper for the rebalance_tree method.
        RecursionCounter()
        tree.add(list[(len(list) // 2)])
        if (len(list) == 1):
            return 0
        else:
            BinarySearchTree.rebalance_helper(tree, list[0 : int(len(list) // 2)])
            BinarySearchTree.rebalance_helper(tree, list[(len(list) // 2) + 1: len(list)])

    def set_heights(node): # retrieves accurate heights for every node in the tree.
        RecursionCounter()
        if (node != None):
            BinarySearchTree.set_heights(node.left_child)
            node.height = BinarySearchTree.retrieve_height(node)
            BinarySearchTree.set_heights(node.right_child)

    def height(self): # returns height of overall tree.
        if (self.root == None):
            return -1
        return self.root.height


    def inorder(self): # used to access an inorder list of the contents of the tree.
        list = []
        return BinarySearchTree.inorder_recursive(self.root, list)

    def inorder_recursive(node, list): # recursive helper for the inorder traversal.
        RecursionCounter()
        if (node != None):
            BinarySearchTree.inorder_recursive(node.left_child, list)
            list.append(node.data)
            BinarySearchTree.inorder_recursive(node.right_child, list)
            return list

    def preorder_recursive(node): # recursive helper for the preorder traversal.
        RecursionCounter()
        if (node != None):
            print("{}, ".format(node.data), end = "")
            BinarySearchTree.preorder_recursive(node.left_child)
            BinarySearchTree.preorder_recursive(node.right_child)

    def preorder(self): # used to print a preorder traversal of the tree.
        BinarySearchTree.preorder_recursive(self.root)

    
             
    def __str__(self): # tostring method for the BinarySearchTree class.
        BinarySearchTree.print_helper(self.root, -1)
        return ""

    def print_helper(cursor, offset): # used to show a representation of the tree.
        RecursionCounter()

        offset += 1
        if (cursor != None):
            cursor.height = BinarySearchTree.retrieve_height(cursor)

            for x in range(offset):
                print("    ", end = "")
            print(cursor)
            
            if ((cursor != None) and (cursor.right_child != None and cursor.left_child == None)):
               for x in range(offset + 1):
                   print("    ", end = "")
               print("[Empty]")

            BinarySearchTree.print_helper(cursor.left_child, offset)

            if ((cursor != None) and (cursor.right_child == None and cursor.left_child != None)):
                for x in range(offset + 1):
                    print("    ", end  = "")
                print("[Empty]")
            BinarySearchTree.print_helper(cursor.right_child, offset)
        

    def __len__(self): # returns length of the tree.
        size = 1
        if (self.root == None):
            return 0
        elif(self.root.left_child == None and self.root.right_child == None):
            return 1
        elif (self.root.left_child == None):
            size += BinarySearchTree.length_helper(self.root.right_child)
        elif (self.root.right_child == None):
            size += BinarySearchTree.length_helper(self.root.left_child)
        else:
            size += BinarySearchTree.length_helper(self.root.right_child)
            size += BinarySearchTree.length_helper(self.root.left_child)
        return size

    def length_helper(cursor): # recursive helper used to calculate length of tree.
        RecursionCounter
        value = 1
        if (cursor.left_child == None and cursor.right_child == None):
            return 1
        elif (cursor.left_child == None):
            return 1 + BinarySearchTree.length_helper(cursor.right_child)
        elif (cursor.right_child == None):
            return 1 + BinarySearchTree.length_helper(cursor.left_child)
        else:
            value += BinarySearchTree.length_helper(cursor.right_child)
            value += BinarySearchTree.length_helper(cursor.left_child)
            return value

    def retrieve_height(cursor): # used to calculate the height of a given node.
        height1 = 0
        height2 = 0
        if(cursor.left_child == None and cursor.right_child == None):
            return 0
        elif(cursor.left_child == None):
            return 1 + BinarySearchTree.retrieve_height(cursor.right_child)
        elif(cursor.right_child == None):
            return 1 + BinarySearchTree.retrieve_height(cursor.left_child)
        else:
            height1 = 1 + BinarySearchTree.retrieve_height(cursor.left_child)
            height2 = 1 + BinarySearchTree.retrieve_height(cursor.right_child)
            if (height1 >= height2):
                return height1
            else:
                return height2

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