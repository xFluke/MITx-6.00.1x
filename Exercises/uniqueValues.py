# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:59:18 2018

@author: Miko Man
"""

def uniqueValues(aDict):
    uniqueKeys = []
    
    for key in aDict.keys():
        foundOriginal = False
        for value in aDict.values():
            if aDict[key] == value and not foundOriginal:
                foundOriginal = True
            elif aDict[key] == value and foundOriginal:
                break
        else:
            uniqueKeys.append(key)
    
    uniqueKeys.sort()
    return uniqueKeys

