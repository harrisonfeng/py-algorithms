#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ********************************************************************
# *  _   _                 _                   _____                 *
# * | | | | __ _ _ __ _ __(_)___  ___  _ __   |  ___|__ _ __   __ _  *
# * | |_| |/ _` | '__| '__| / __|/ _ \| '_ \  | |_ / _ \ '_ \ / _` | *
# * |  _  | (_| | |  | |  | \__ \ (_) | | | | |  _|  __/ | | | (_| | *
# * |_| |_|\__,_|_|  |_|  |_|___/\___/|_| |_| |_|  \___|_| |_|\__, | *
# *                                                           |___/  *
# *                                                                  *
# ********************************************************************
# * Copyright 2014 Harrison Feng <feng.harrison@gmail.com>           *
# * All rights, including trade secret rights, reserved.             *
# ********************************************************************
#
# @author Harrison Feng <feng.harrison@gmail.com>
#
#

___version__ = 1.0.0


class Stack(object):
    '''Stack implementation'''
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self._items:
            return self._items.pop()
        else:
            print("This stack is empty!")

    def peek(self):
        if self._items:
            return self._items[-1]
        else:
            print("This stack is empty!")

    def __repr__(self):
        print "{}".format(self._items)

class Node(object):
    '''Node implementation'''
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class StackL(object):
    '''Stack implementation with linked list'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        return not bool(self._head)

    def push(self, data):
        self._head = Node(data, self._head)

    def pop(self):
        if self._head:
            data = self._head.data
            self._head = self._head.next
            return data
        else:
            print("This stack is empty!")

    def peek(self):
        if self._head:
            return self._head.data
        else:
            print("This stack is empty!")

    def size(self):
        if self._head:
            node = self._head
            n = 0
            while node:
                node = node.next
                n += 1
            return n
        else:
            return 0
