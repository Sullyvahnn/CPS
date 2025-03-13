import numpy as np
import scipy.io as scipy
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
data = scipy.loadmat('adsl_x.mat')['x'].flatten()


def myCorrelation(sig1, sig2):
    len1, len2 = len(sig1), len(sig2)
    sig1 = np.concatenate([sig1, np.zeros(len2)])
    corr_values_ = np.zeros(len1)
    for j in range(len1):
        correlation_sum = 0
        for i in range(0, len2):
            correlation_sum += sig1[i+j] * sig2[i]
        corr_values_[j] = correlation_sum
    return corr_values_


l = 4
N = 512
M = 32
for i in range(len(data)):
    prefix = data[i:i+M]
    # print(data[0:32])
    # print(data[480:512])
    corr_values = myCorrelation(data, prefix)
    max_idx = np.argmax(corr_values)
    # fig, axis = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
    # axis[0].plot(np.arange(0,len(chunk)), chunk)
    # axis[1].plot(np.arange(0,len(prefix)), prefix)
    plt.plot(corr_values)
    plt.show()
    print(max_idx)


