# my_funcs.py

from math import factorial

def cos_approx(x,n_terms):
    
    approx = 0
    for i in range(0,n_terms):
        coef = (-1)**i
        num = x**(2*i)
        denom = factorial(2*i)
        term = coef*(num/denom)
        approx = approx + term
        
    return approx
