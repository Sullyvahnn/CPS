import matplotlib
import numpy as np
from scipy.fft import dct, idct
from matplotlib import pyplot as plt
from scipy.io.wavfile import read
import sounddevice as sd
matplotlib.use('TkAgg')

fs, sig = read("my_speech.wav")
sig = sig[10000:] # puste

# plt.plot(sig)
# plt.show()

c = dct(sig, norm='ortho')
num_coeff = int(0.25 * len(c))
c_reduced = np.zeros_like(c)
# c_reduced[num_coeff:] = c[num_coeff:]
c[np.abs(c) < 100] = 0

reconstructed_signal = idct(c, norm='ortho')
reconstructed_signal /= np.max(np.abs(reconstructed_signal))
t = np.arange(len(sig)) / fs
noise = 400*np.sin(2 * np.pi * 250 * t)
noised_sig = sig + noise
noised_sig /= np.max(np.abs(noised_sig))
plt.plot(noised_sig)
plt.show()
sd.play(noised_sig, fs)
sd.wait()

c_noised = dct(noised_sig, norm='ortho')
c_noised[250] = 0
sig_denoised = idct(c_noised, norm='ortho')
sig_denoised = sig_denoised / np.max(np.abs(sig_denoised))

# sd.play(sig_denoised, fs)
# sd.wait()


