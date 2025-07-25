import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 1.1
w = 1
N = 20
total_sites = 2 * N


hamiltonian = generate_hamiltonian(N, v, w)

e_val, e_vec = np.linalg.eigh(hamiltonian)

mid_up_idx = total_sites // 2
# topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1, mid_up_idx - 2, mid_up_idx + 1])
topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1])



for idx, i in enumerate(topo_state_idx_arr):
    plt.subplot(2, 2, idx + 1)
    plt.plot(np.arange(1, total_sites + 1), e_vec[:, i], marker='x', color='k')
    plt.title(f'Wave function vs Site Index for Energy: {np.round(e_val[i], 7)}')
    plt.grid()
    plt.xlabel('Site Index')
    plt.ylabel('Wave Function')


for idx, i in enumerate(topo_state_idx_arr):
    plt.subplot(2, 2, 3 + idx)
    plt.plot(np.arange(1, total_sites + 1), e_vec[:, i]**2, marker='x', color='k')
    plt.title(f'Probability Density vs Site Index for Energy: {np.round(e_val[i], 7)}')
    plt.grid()
    plt.xlabel('Site Index')
    plt.ylabel('Probability Density')
plt.suptitle(f'Wave Function and Probability Density at Sites \nNo. of unit cells (N): {N}, Intra-cell Hopping Constant (v): {v} & Inter-cell Hopping Constant (w): {w}')
plt.subplots_adjust(hspace=0.4)
plt.show()

