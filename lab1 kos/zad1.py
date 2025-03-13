import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import resample
matplotlib.use('TkAgg')


def ret_t_lin(A, f_sig, fprs, t):
    ret_t = []
    ret_sin = []
    for f in fprs:
        t_values = np.arange(0, f * t) / f
        ret_t.append(t_values)
        ret_sin.append(A * np.sin(t_values * 2 * np.pi * f_sig))
    return ret_t, ret_sin


def A():
    A = 230
    t = 0.1
    f_sig = 50

    fpr = [int(10e3), 500, 200]
    style = ['b-', 'r-o', 'k-x']
    t_lin, sins = ret_t_lin(A, f_sig, fpr, t)

    # fig, ax = plt.subplots(nrows=3, ncols=1, sharex=False, sharey=False)
    for i in range(3):
        # ax[i].plot(t_lin[i], sins[i], style[i])
        plt.plot(t_lin[i], sins[i], style[i])
    plt.show()


# B
def B():
    f = 50
    t = 1
    fpr = [int(10e3), 49, 50, 51]
    # fpr = [int(10e3), 26, 25, 24]
    styles = ['b-', 'g-o', 'r-o', 'k-o']
    t_lin, sins = ret_t_lin(1, f, fpr, t)
    # fig, ax = plt.subplots(nrows=4, ncols=1, sharex=False, sharey=False)
    for i in range(4):
        # ax[i].plot(t_lin[i], sins[i], styles[i])
        plt.plot(t_lin[i], sins[i], styles[i])
    plt.show()


def C():
    fpr = 100
    t = 1
    fs = np.arange(0, 300, 5)
    t = np.arange(0, t, 1 / fpr)
    sins = []
    coss = []
    for f in fs:
        sins.append(np.sin(2 * np.pi * f * t))
        coss.append(np.cos(2 * np.pi * f * t))
    sins = coss
    # plt.plot(t,sins[1], 'go')
    # plt.plot(t,sins[int(105/5)], 'ro')
    # plt.plot(t,sins[int(205/5)], 'yo')

    plt.plot(t, sins[int(95 / 5)], 'go')
    plt.plot(t, sins[int(295 / 5)], 'ro')
    plt.plot(t, sins[int(195 / 5)], 'yo')

    # plt.plot(t,sins[int(95/5)])
    # plt.plot(t,sins[int(105/5)])

    plt.show()


def D():
    t = 1
    fpr = int(10e3)
    fpr2 = 25
    fn = 50
    fm = 1
    df = 5
    t = np.arange(0, t, 1 / fpr)
    # sin = np.sin(2 * np.pi * t * fm)
    modulated_sin = np.cos(2 * np.pi * fn * t + df*np.sin(2*np.pi*fm*t))

    probed_signal = modulated_sin[::400]
    probed_t = t[::400]

    # plt.plot(probed_t, probed_signal, 'o')
    # plt.plot(t, modulated_sin)
    # plt.show()

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=False, sharey=False)
    ax[0].specgram(probed_signal, Fs=fpr2, NFFT=256, noverlap=128, cmap='plasma')
    ax[0].set_ylim(0, 12.5)
    ax[0].set_title('Probed spectrum')
    # występuje alliasing
    # częstotliwość ograniczona do nyquista

    ax[1].specgram(modulated_sin, Fs=fpr, NFFT=1024, noverlap=512, cmap='plasma')
    ax[1].set_ylim(0, 400)
    ax[1].set_title('Original spectrum')
    # nie ma filtra dolno przepustowego
    plt.show()


D()

