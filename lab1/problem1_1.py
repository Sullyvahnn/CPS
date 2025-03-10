import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.signal import spectrogram

matplotlib.use('TkAgg')


def sub_sin(Amp, freq, phase):
    return Amp * np.sin(2 * np.pi * freq * t + phase)


fpr = 44100
dt = 1 / fpr
Nx = 3*fpr
n = np.arange(1, Nx-1)
p1 = np.pi/4
t = dt * n

y1 = sub_sin(50,    1000, 0)
y2 = sub_sin(1,1500, 0)
y3 = sub_sin(1, 2500, 0)
# y_sum = y1 + y2 + y3

gaussian_noise = np.random.normal(0, 1, len(t))
uniform_noise = np.random.uniform(0, 1, len(t))
fig, axes = plt.subplots(5, 1, figsize=(12, 4))

# Plot data
axes[0].plot(t, y1)
axes[0].set_title("First")

axes[1].plot(t, y2)
axes[1].set_title("Second")

axes[2].plot(t, y3)
axes[2].set_title("Third")
axes[2].set_ylim(-5, 5)

# axes[3].plot(t, y_sum)
# axes[3].set_title("Sum")
# axes[3].set_ylim(-5, 5)

axes[3].plot(t, gaussian_noise)
axes[3].set_title("Gaussian Noise")
axes[3].set_ylim(-5, 5)

axes[4].plot(t, uniform_noise)
axes[4].set_title("Normal Noise")
axes[4].set_ylim(-5, 5)

signal_gaussian_noise = y1+gaussian_noise
signal_uniform_noise = y1+uniform_noise

plt.tight_layout()
# plt.show()

# signal_gaussian_noise = np.int16(signal_gaussian_noise / np.max(np.abs(signal_gaussian_noise)) * 32767)
# signal_uniform_noise = np.int16(signal_uniform_noise / np.max(np.abs(signal_uniform_noise)) * 32767)
# y1 = np.int16(y1 / np.max(np.abs(y1)) * 32767)
# write("y1.wav", fpr, y1)
# write("uniform.wav", fpr, signal_uniform_noise)
# write("gaussian.wav", fpr, signal_gaussian_noise)

fig1, axes1 = plt.subplots(3, 1, figsize=(12, 4))

# Plot data
axes1[0].specgram(y1, Fs=fpr, cmap="inferno")
axes1[0].set_title("First")

axes1[1].specgram(y1+gaussian_noise, Fs=fpr, cmap="inferno")
axes1[1].set_title("Gaussian Noise")
axes1[1].set_ylim(-5, 5)

axes1[2].specgram(y1+uniform_noise, Fs=fpr, cmap="inferno")
axes1[2].set_title("Normal Noise")
axes1[2].set_ylim(-5, 5)

plt.tight_layout()
plt.show()


