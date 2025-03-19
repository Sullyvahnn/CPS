import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def DCT(N, fpr):
    vector = []
    for k in range(N):
        alpha = np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N)
        row = [alpha * np.cos((np.pi * (k)) / N * (n + 0.5)) for n in range(N)]
        vector.append(row)
    vector = np.array(vector)
    freq_values = np.arange(0, N) * fpr / N / 2
    return vector, freq_values


if __name__ == '__main__':
    N = 100
    x_values = np.arange(0, N)
    x_sin = np.random.rand(N)
    vector = DCT(N)

    # orthogonal check
    # G = vector @ vector.T - np.eye(len(vector @ vector.T))
    # orthogonal_check = np.sum([G[i][i] for i in range(N)])
    # print(orthogonal_check)
    X_sin = vector @ x_sin

    # reverse
    S = vector.T
    reconstructed = S @ X_sin
    plt.plot(x_sin)
    plt.plot(reconstructed)
    plt.show()

    # A = np.random.rand(N,N)
    # S = np.linalg.inv(A)
    # print((A@S).astype(int))
    # print((A@A.T).astype(int))
    # Y = A @ x_sin
    # X = S @ Y
    # plt.plot(X)
    # plt.plot(x_sin)
    # plt.show()
    # print(X==x_sin)
