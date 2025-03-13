import matplotlib
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
import numpy as np

matplotlib.use('TkAgg')


def generateSin(Amp):
    t = np.arange(0, fpr * ts)
    return Amp * np.sin(2 * np.pi * fc * t / fpr)


def evaluateBit(bit):
    if bit == '1':
        return generateSin(-A)
    else:
        return generateSin(A)


def code(string):
    sig = np.empty(0)
    for letter in string:
        binary_code = format(ord(letter), "08b")
        for bit in binary_code:
            char_sig = evaluateBit(bit)
            sig = np.concatenate([sig, char_sig])
    return sig


def findPhase(sig):
    if np.angle(np.real(np.fft.fft(sig)[0])) != 0:
        return 0
    return 1


def decodeChar(char_sig):
    bits = np.split(char_sig, 8)
    bit_code = ""
    for bit in bits:
        bit_code += str(findPhase(bit))
    return chr(int(bit_code, 2))


def decode(sig):
    char_fpr = int(ts * fpr * char_repr_length)
    num_syms = len(sig) // char_fpr
    message = ""
    for i in range(num_syms):
        start = i * char_fpr
        end = (i + 1) * char_fpr
        message += str(decodeChar(sig[start:end]))
    return message


char_repr_length = 8
name = "sex, narkotyki, wydzial informatyki"
fpr = int(16e3)
ts = 100e-3
fc = 500
A = 1

signal = code(name)
write("../lab1/signal.wav", fpr, signal)
# fig, axes = plt.subplots(nrows=8, ncols=2, sharex=False, sharey=False, figsize=(8, 8))
# bits = np.split(signal, char_repr_length)
# for i in range(8):
#     axes[i][0].plot(bits[i])
#     spectrum = np.real(np.fft.fft(signal)) / fpr
#     freqs = np.fft.fftfreq(len(signal), 1 / fpr)
#     axes[i][1].plot(freqs[:200], spectrum[:200])
# plt.show()

print(decode(signal))
# wolne w chuj, lepsza demodulacja

