# week7_funcs.py

import math

def cyl_vol(d,h):
    """
    cyl_vol() is a fuction to calculate the volume of a cylinder
    input: d, diameter of the cylinder (int or float), h, height of the cylinder (int or float), both positional only arguments
    output: v, the volume of a cylinder, float
    
    example:
        
        cyl_vol(2,1)
        
        3.141592653589793
    """
    r = d/2
    a = math.pi*(r**2)
    v = a*h
    return v

def rect_area(base=1,height=1):
    """
    rect_area() is a function to calculate the area of a rectangle
    
    input: base, height (both ints or floats) and keyword arguments
    output: area (float)
    
    example:
    
        rect_area(5,10)
        
        50
    """
    area = base*height
    return area










