import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 0.75
w = 1
N = 20
total_sites = 2 * N
# topo_state_no = 2


hamiltonian = generate_hamiltonian(N, v, w)

e_val, e_vec = np.linalg.eigh(hamiltonian)

mid_up_idx = total_sites // 2
# topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1, mid_up_idx - 2, mid_up_idx + 1])
topo_state_idx_arr = np.array([mid_up_idx, mid_up_idx - 1])
marker_list = ['o', 'x']

# print(topo_state_arr)

# e_vec = e_vec.transpose()
# print(topo_state_idx_arr)

# plt.hist(e_vec[:, 50])
# plt.show()



for idx, i in enumerate(topo_state_idx_arr):
    plt.subplot(2, 2, idx + 1)
    plt.plot(np.arange(1, total_sites + 1), e_vec[:, i], marker='x', color='k')
    plt.title(f'Wave function vs Site Index for Energy: {np.round(e_val[i], 7)}')
    plt.grid()
    plt.xlabel('Site Index')
    plt.ylabel('Wave Function')
    # plt.legend()
    # print(np.linalg.norm(e_vec[:, i]))
# plt.legend()
# plt.grid()
# plt.show()


for idx, i in enumerate(topo_state_idx_arr):
    plt.subplot(2, 2, 3 + idx)
    plt.plot(np.arange(1, total_sites + 1), e_vec[:, i]**2, marker='x', color='k')
    plt.title(f'Probability Density vs Site Index for Energy: {np.round(e_val[i], 7)}')
    plt.grid()
    plt.xlabel('Site Index')
    plt.ylabel('Probability Density')
    # plt.legend()

plt.suptitle(f'Wave Function and Probability Density at Sites \nIntra-cell Hopping Constant (v): {v} & Inter-cell Hopping Constant (w): {w}')
# plt.tight_layout()
plt.subplots_adjust(hspace=0.4)
plt.show()


# plt.plot(np.arange(1, total_sites + 1), e_vec[total_sites // 2 - 1], label='State 1 M1')
# plt.plot(np.arange(1, total_sites + 1), e_vec[total_sites // 2], label='State 2 M1')
# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[0], label='State 1 M2')
# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[1], label='State 2 M2')
# plt.legend()
# plt.grid()
# plt.show()


# plt.plot(np.arange(1, total_sites + 1), e_vec[total_sites // 2 - 1]**2, label='State 1 M1')
# plt.plot(np.arange(1, total_sites + 1), e_vec[total_sites // 2]**2, label='State 2 M1')
# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[0]**2, label='State 1 M2')
# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[1]**2, label='State 2 M2')
# plt.legend()
# plt.grid()
# plt.show()
