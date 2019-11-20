# myfuncs.py
"""
A python that contains a function that calculates the approximation of the cosine function using a taylor series
"""

from math import factorial

def approx_cos(x,n_terms):
    approx = 1
    for i in range(1,n_terms+1):
        term = ((-1)**i)  * ((x**(i*2)) / (factorial(i*2)))
        approx = approx + term
    
    return approx
