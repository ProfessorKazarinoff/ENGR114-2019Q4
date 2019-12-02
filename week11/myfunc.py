# myfunc.py

import numpy as np

# prototype out the function to approximate e
def eapprox(K):
    k_array = np.random.randint(1,K+1,K)
    J=0
    for i in range(1,K+1):
        if not (i in k_array):
            J = J + 1
    e = K/J
    return e
