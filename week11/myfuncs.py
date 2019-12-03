# myfuncs.py
import numpy as np

def eapprox(K):
    J = 0
    rand_num_lst = np.random.randint(1,K+1,K)
    for i in range(1,K+1):
        if not i in rand_num_lst:
            J = J + 1
    return K/J
 