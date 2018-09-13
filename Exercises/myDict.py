# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:30:00 2018

@author: Miko Man
"""

class myDict(object):
    def __init__(self):
        self.keys = []
        self.values = []
    def assign(self, k, v):
        if k in self.keys:
            keyIndex = self.keys.index(k)
            self.values[keyIndex] = v
        else:
            self.keys.append(k)
            self.values.append(v)
        
    def getval(self, k):
        if k in self.keys:
            keyIndex = self.keys.index(k)
            return self.values[keyIndex]
        else:
            raise KeyError
    def delete(self, k):
        if k in self.keys:
            keyIndex = self.keys.index(k)
            self.keys.remove(k)
            self.values.remove(self.values[keyIndex])
        else:
            raise KeyError
        