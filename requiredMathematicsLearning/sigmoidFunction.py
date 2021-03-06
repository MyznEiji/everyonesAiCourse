import matplotlib.pyplot as plt
import numpy as np
import math


def sigmoid(a):
    s = 1 / (1 + e**-a)
    return s


e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# y = 1 / (1 + e^(-x))
# y_sig = 1 / (1 + e**-x)
y_sig = sigmoid(x)

plt.plot(x, y_sig)
plt.show()


def sigmoid(a):
    s = 1 / (1 + e**-a)
    return s


e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# シグモイド関数: y = 1 / (1 + e^(-x))
y_sig = sigmoid(x)
# シグモイド関数の傾き
y_dsig = (sigmoid(x + dx) - sigmoid(x)) / dx

plt.plot(x, y_sig, label="sigmoid")
plt.plot(x, y_dsig, label="d_sigmoid")
plt.legend()
plt.show()


def sigmoid(a):
    s = 1 / (1 + e**-a)
    return s


def d_sigmoid(a):
    d = sigmoid(a) * (1 - sigmoid(a))
    return d


e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

# シグモイド関数: y = 1 / (1 + e^(-x))
y_sig = sigmoid(x)
# シグモイド関数の傾き: 微分
y_dsig = (sigmoid(x + dx) - sigmoid(x)) / dx
# シグモイド関数の微分
# dy_sig = sigmoid(x)*(1 - sigmoid(x))
dy_sig = d_sigmoid(x)

plt.plot(x, y_sig, label="sigmoid")
plt.plot(x, y_dsig, label="d_sigmoid")
plt.plot(x, dy_sig, label="dy_sigmoid")
plt.legend()
plt.show()
