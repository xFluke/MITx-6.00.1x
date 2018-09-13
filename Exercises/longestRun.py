# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:49:11 2018

@author: Miko Man
"""

def longestRun(L):
    longest = 0
    currentNum = 0
    previousRun = 0
    for number in L:
        if number >= previousRun:
            currentNum += 1
        else:
            currentNum = 1 
        previousRun = number
        
        if currentNum > longest:
            longest = currentNum

    return longest
