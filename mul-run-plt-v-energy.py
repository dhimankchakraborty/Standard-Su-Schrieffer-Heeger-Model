import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




w = 1
N = 20
total_sites = 2 * N

v_start = 0
v_end = 2.5
v_count = 101
v_arr = np.round(np.linspace(v_start, v_end, v_count), 4)


e_val_arr = []
for v in v_arr:
    hamiltonian = generate_hamiltonian(N, v, w)

    e_val = np.linalg.eigvalsh(hamiltonian)
    e_val_arr.append(e_val)

dim = len(e_val)
e_val_arr = np.array(e_val_arr).transpose()
# print(e_val_arr.shape())
# print(np.shape(e_val_arr))
# print(e_val_arr)


for i in range(dim):
    plt.plot(v_arr, e_val_arr[i])
plt.grid()
plt.ylabel(r"Energy ($E$)")
plt.xlabel(r"Intra-Cell Hopping ($v$)")
plt.show()