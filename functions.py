import numpy as np
import scipy as sp




def generate_hamiltonian(N, v, w):
    tot_sites = 2 * N

    H = np.zeros((tot_sites, tot_sites))

    for k in range(N):
        H[2*k-1,2*k] = w
        H[2*k,2*k-1] = w
        H[2*k,2*k+1] = v
        H[2*k+1,2*k] = v
    
    H[-1,0] = 0
    H[0,-1] = 0

    return H



def dispersion_relation(k, v, w):
    res = np.sqrt(np.square(v) + np.square(w) + 2 * v * w * np.cos(k))

    return res



def d_x(k, v, w):
    return v + w * np.cos(k)



def d_y(k, w):
    return w * np.sin(k)
