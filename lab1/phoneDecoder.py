import matplotlib
import scipy
from scipy.io.wavfile import read
from matplotlib import pyplot as plt
import numpy as np

matplotlib.use('TkAgg')


def find_nearest(value, array):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def matchSymbol(f):
    f.sort()
    DTMF_freqs_x = np.array([1209, 1336, 1477, 1633])
    DTMF_freqs_y = np.array([697, 770, 852, 941])
    freq_y = find_nearest(f[0], DTMF_freqs_y)
    freq_x = find_nearest(f[1], DTMF_freqs_x)
    match freq_x, freq_y:
        case 1209, 697:
            return "1"
        case 1336, 697:
            return "2"
        case 1477, 697:
            return "3"
        case 1209, 770:
            return "4"
        case 1336, 770:
            return "5"
        case 1477, 770:
            return "6"
        case 1209, 852:
            return "7"
        case 1336, 852:
            return "8"
        case 1477, 852:
            return "9"
        case 1336, 941:
            return "0"


fpr, data = read("myPhone.wav")
buffer = 8000
ts = 0.5

num_sym = int((len(data)) / buffer)

fig, axes = plt.subplots(num_sym, 2, figsize=(15, 6))
start = 300
end = 800
half = buffer // 2
decoded_number = ""
for i in range(0, num_sym):
    symbol_data = data[i * buffer:(i + 1) * buffer]
    spectrum = np.abs(scipy.fft.fft(symbol_data))
    magnitude = spectrum / buffer
    freqs = np.fft.fftfreq(buffer, 1 / fpr)
    # only second half
    magnitude = magnitude[:half]
    freqs = freqs[:half]
    # find dominant freqs
    top_n = 2
    dominant_indices = np.argsort(magnitude)[-top_n:]
    dominant_freqs = freqs[dominant_indices]
    decoded_number += matchSymbol(dominant_freqs)
    # plot
    axes[i][0].plot(symbol_data[:1000])
    axes[i][1].plot(freqs[start:end], magnitude[start:end])
# plt.show()
print("Your number is:", decoded_number)
