import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import read
from zad1 import DCT
matplotlib.use('TkAgg')

fs, sig = read("mowa.wav")
plt.plot(sig)
points = np.random.randint(low=0, high=len(sig), size=10)
for point in points:
    data_sample = sig[point:point+256]
    vector, freq_values = DCT(256, fs)
    X_sample = vector @ data_sample
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=False, sharey=False)
    ax[0].plot(freq_values, data_sample)
    ax[1].plot(freq_values, X_sample)
    plt.show()

