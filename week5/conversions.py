# conversions.py

# a function to convert teaspoons to mL
# 1 teaspoon = 4.92892 mL
def ts2ml(ts):
    """
    ts2ml() is a funciton to convert teaspons to mL
    input: teaspoons, int or float
    output: mL, int or float
    
    example:
    
    ts2ml(2)
    
        9.85784
    
    """
    ml = ts*4.92892
    return ml
