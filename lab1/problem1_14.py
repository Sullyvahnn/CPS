import matplotlib
import numpy as np
from scipy.io.wavfile import write

matplotlib.use('TkAgg')


def generateDTMF(mobile_number):
    signal = []
    for number in mobile_number:
        match number:
            case "1":
                signal.append(generateTone(1209, 697))
            case "2":
                signal.append(generateTone(1336, 697))
            case "3":
                signal.append(generateTone(1477, 697))
            case "4":
                signal.append(generateTone(1209, 770))
            case "5":
                signal.append(generateTone(1336, 770))
            case "6":
                signal.append(generateTone(1477, 770))
            case "7":
                signal.append(generateTone(1209, 852))
            case "8":
                signal.append(generateTone(1336, 852))
            case "9":
                signal.append(generateTone(1477, 852))
            case "0":
                signal.append(generateTone(1336, 941))
            case _:
                print("wrong number")
                return
    return signal


def generateTone(freq1, freq2):
    t = np.arange(0, int(ts * fpr))
    A = 1000
    sin1 = A * np.sin(2 * np.pi * freq1 * t / fpr)
    sin2 = A * np.sin(2 * np.pi * freq2 * t / fpr)
    return sin1+sin2


ts = 0.5
fpr = 16000
phone_signals = generateDTMF("665668885")
signal_to_write = np.concatenate([np.int16(signal / np.max(np.abs(signal)) * 32767)
                                  for signal in phone_signals])
write("myPhone.wav", fpr, signal_to_write)
