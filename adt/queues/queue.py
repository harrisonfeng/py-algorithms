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
