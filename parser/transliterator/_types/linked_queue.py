# -*- coding: utf-8 -*-
# Author: Linzo99
# Mail: xxx@xx
# Created Time: Wed Oct 12

class LinkedQueue:

    class _Node:
        def __init__(self, ele, next=None):
            self._ele = ele
            self._next = next
            self._prev = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._ele

    def dequeue(self, ele):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._head._ele
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, ele):
        newest = self._Node(ele, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail 
        self._tail = newest
        self._size += 1
