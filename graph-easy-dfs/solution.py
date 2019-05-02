#! /bin/python


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        """
        Traverses the tree using DFS
        (navigating the tree from left to right)
        :param array: empty array
        :return: array which stored all of the Nodes' names
        """
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
