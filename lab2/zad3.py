import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from lab2.zad1 import DCT

matplotlib.use('TkAgg')

N = 100
fpr = 1000
x_values = np.arange(0, N) / fpr
x_sin = 50*np.sin(2*np.pi*50*x_values) + 100*np.sin(2*np.pi*100*x_values) + 150*np.sin(2*np.pi*150*x_values)

vector = DCT(N)

S = vector.T

# fig, ax = plt.subplots()
# line, = ax.plot(10, 10)
#
# for idx in range(N):
#     ax.clear()
#     ax.plot(vector[idx])
#     ax.plot(S[idx])
#     plt.pause(0.5)
#     print(idx)

Y = vector @ x_sin
# plt.plot(np.arange(0,N)*fpr/N/2, Y[1:N])
# plt.show()

# plt.plot(S @ Y)
plt.plot(x_sin - S @ Y)
plt.show()