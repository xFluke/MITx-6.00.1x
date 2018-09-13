# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Miko Man

Specification:
Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""
from math import tan
from math import pi

def polysum(n, s):
    '''
    n: number of sides
    s: length of sides
    
    returns: the sum of the area and the square of the perimeter of the regular polygon
    '''
    
    # Compute area and perimeter
    area = (0.25*n*s**2) / tan(pi/n)
    perimeter = n*s
    
    return round(area + perimeter**2, 4)
