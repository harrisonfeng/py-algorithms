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


class Queue(objec):
    '''Queue

    A queue, differently of a stack, is a structure where the first 
    enqueue element (at the back) will be the first one to be dequeued.

             ---> d ---> c ---> b ---> a ---->
             in                              out

   So a queue is also called FIFO (first in first out) structure.
   '''
   def __init__(self):
       self._items = []

   def is_empty(self):
       '''determine whether the queue is empty.'''
       return not bool(self._items)

   def enqueue(self, data):
       '''insert an item at the back of the queue.'''
       self._items.insert(0, data)

   def dequeue(self):
       '''remove an item from the front of the queue.'''
       if self._items:
           return self._items.pop()
       else:
           print("This queue is empty")

   def size(self):
       '''return the size of the queue.'''
       return len(self._items)

   def peek(self):
       if self._items:
           return self._items[-1]
       else:
           print("This queue is empty")
