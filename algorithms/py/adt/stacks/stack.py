#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2018 Harrison Feng <feng.harrison@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


___version__ = 1.0.0


class Stack(object):
    '''Stack

    A stack is a linear data structure that can be accessed only at one of its
    ends for either storing or retriving. Stack is called LIFO(last in first
    out) structure too.
    '''

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
