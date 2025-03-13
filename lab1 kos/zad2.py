import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def sinc_interp(points, t_val, fpr):
    y = np.zeros(len(t_val))
    T = 1/fpr
    for i in range(len(points)):
        y += points[i] * np.sinc((t_val - i * T)/T)

    return y


fpr = int(10e3)
fpr_old = 200
f=10
duration = 1


t = np.arange(0, duration, 1/fpr_old)
t_new = np.arange(0, duration, 1/fpr)

old_sig = np.sin(2*np.pi*t*f)

interpolated_sig = sinc_interp(old_sig, t_new, fpr_old)

plt.plot(t, old_sig, 'o')
plt.plot(t_new, interpolated_sig)
plt.show()



