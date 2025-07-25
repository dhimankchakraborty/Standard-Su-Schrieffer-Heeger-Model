import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from functions import *




k_arr = np.linspace(-1 * np.pi, np.pi, 101)
# print(k_arr)


v = 1
w = 0
plt.subplot(2, 5, 1)
plt.plot(k_arr, dispersion_relation(k_arr, v, w), color='k')
plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w), color='k')
plt.xticks(np.linspace(-1 * np.pi, np.pi, 3))
plt.grid()

plt.subplot(2, 5, 6)

plt.scatter(d_x(k_arr, v, w), d_y(k_arr, w), color='k')
plt.scatter(0, 0, color='k')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1)
plt.axvline(x=0, color='k', linestyle='--', linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-2, -1, 0, 1, 2])
plt.grid()



v = 1
w = 0.5
plt.subplot(2, 5, 2)
plt.plot(k_arr, dispersion_relation(k_arr, v, w), color='k')
plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w), color='k')
plt.xticks(np.linspace(-1 * np.pi, np.pi, 3))
plt.grid()

plt.subplot(2, 5, 7)
plt.plot(d_x(k_arr, v, w), d_y(k_arr, w), color='k')
plt.scatter(0, 0, color='k')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1)
plt.axvline(x=0, color='k', linestyle='--', linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-2, -1, 0, 1, 2])
plt.grid()



v = 1
w = 1
plt.subplot(2, 5, 3)
plt.plot(k_arr, dispersion_relation(k_arr, v, w), color='k')
plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w), color='k')
plt.xticks(np.linspace(-1 * np.pi, np.pi, 3))
plt.grid()

plt.subplot(2, 5, 8)
plt.plot(d_x(k_arr, v, w), d_y(k_arr, w), color='k')
plt.scatter(0, 0, color='k')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1)
plt.axvline(x=0, color='k', linestyle='--', linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-2, -1, 0, 1, 2])
plt.grid()



v = 0.5
w = 1
plt.subplot(2, 5, 4)
plt.plot(k_arr, dispersion_relation(k_arr, v, w), color='k')
plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w), color='k')
plt.xticks(np.linspace(-1 * np.pi, np.pi, 3))
plt.grid()

plt.subplot(2, 5, 9)
plt.plot(d_x(k_arr, v, w), d_y(k_arr, w), color='k')
plt.scatter(0, 0, color='k')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1)
plt.axvline(x=0, color='k', linestyle='--', linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-2, -1, 0, 1, 2])
plt.grid()



v = 0
w = 1
plt.subplot(2, 5, 5)
plt.plot(k_arr, dispersion_relation(k_arr, v, w), color='k')
plt.plot(k_arr, -1 * dispersion_relation(k_arr, v, w), color='k')
plt.xticks(np.linspace(-1 * np.pi, np.pi, 3))
plt.grid()

plt.subplot(2, 5, 10)
plt.plot(d_x(k_arr, v, w), d_y(k_arr, w), color='k')
plt.scatter(0, 0, color='k')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1)
plt.axvline(x=0, color='k', linestyle='--', linewidth=1)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-2, -1, 0, 1, 2])
plt.grid()
plt.show()
