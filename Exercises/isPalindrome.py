# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:45:13 2018

@author: Miko Man
"""

def isPalindrome(aString):
    if len(aString) == 1 or aString == "":
        return True
    
    if aString[0] == aString[-1]:
        return isPalindrome(aString[1:-1])
    else:
        return False