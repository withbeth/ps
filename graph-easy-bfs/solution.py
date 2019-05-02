#! /bin/python
from Queue import Queue


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array=[]):
        q = Queue()
        q.put(self)
        while q.empty() is False:
            current = q.get()
            array.append(current.name)
            map(q.put, current.children)
        return array



