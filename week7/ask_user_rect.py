# ask_user_rect.py
"""
a Python script to ask a user for a base and height, then calclate the area of a rectangle
"""

from week7_funcs import rect_area

# ask user for base and height
b_str = input('Base: ')
h_str = input('Height: ')
# calculate the area of the rectangle
b_flt = float(b_str)
h_flt = float(h_str)
a = rect_area(base=b_flt,height=h_flt)

# print out the results to the user
print(f'The area is: {round(a,1)}')
