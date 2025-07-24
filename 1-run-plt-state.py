import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




v = 1
w = 2
N = 10
total_sites = 2 * N
topo_state_no = 2


topo_state_arr = []
topo_state_idx_arr = []
hamiltonian = generate_hamiltonian(N, v, w)

e_val, e_vec = np.linalg.eigh(hamiltonian)

e_val_abs = np.abs(e_val)
e_val_abs_sorted = np.sort(e_val_abs)
for i in range(topo_state_no):
    topo_state_idx_arr.append((e_val_abs == e_val_abs_sorted[i]).argmax())

for i in topo_state_idx_arr:
    topo_state_arr.append(e_vec[:, i])


topo_state_arr = np.array(topo_state_arr)

# print(topo_state_arr)

e_vec = e_vec.transpose()


# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[0], label='State 1')
# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[1], label='State 2')
# plt.grid()
# plt.show()


# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[0]**2, label='State 1')
# plt.plot(np.arange(1, total_sites + 1), topo_state_arr[1]**2, label='State 2')
# plt.grid()
# plt.show()


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
