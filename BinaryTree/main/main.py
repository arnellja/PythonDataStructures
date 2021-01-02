from recursioncounter import RecursionCounter # import recursion counter.
import math
from binarysearchtree import Node, BinarySearchTree # import BinarySearchTree class into main module.
from Node import Node # import Node Class into main module.

#This main module instantiates a Binary Search Tree, adds values to the tree, prints the tree, removes a sequence of values, and prints the altered tree.


def main():
    tree = BinarySearchTree() # instantiating the BinarySearchTree to be used.

    for x in range(511):
        tree.add(3)

    tree.rebalance_tree()

    print(tree)








main()