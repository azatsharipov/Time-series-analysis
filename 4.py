import numpy as np
import math
import csv
from matplotlib import pyplot as plt

def get_data():
    # https://www.finam.ru/profile/moex-akcii/gazprom/export/
    file = open('data.csv', 'r')
    reader = csv.reader(file, delimiter=';')
#    print(reader)
    ret = []
    for a in reader:
        if a[4] != '<OPEN>':
            ret.append(float(a[4]))
#    print(ret)

    return np.array(ret)

def LA(data, p, second_order=True):
    eps = 1e-6
    Xi = 3 * (p + 1)
    X = data[np.arange(p) + np.arange(len(data) - p)[:, None]]
    omega = np.argpartition(np.sum(np.power(X - data[-p:], 2), axis=1), Xi)[:Xi]
    if not second_order:
        Y = np.hstack((np.ones(Xi)[:, None], X[omega]))
    else:
        idx = np.arange(p)[:, None] - np.arange(p) <= 0
        Y = np.hstack((np.ones(Xi)[:, None], (X[omega, :, None] * X[omega, None, :])[:, idx]))
    params = np.linalg.solve(Y.T @ Y + eps * np.eye(Y.shape[1]), Y.T @ data[omega + p])
    if not second_order:
        return params, np.sum(params * np.hstack([1, data[-p:]]))
    else:
        return params, np.sum(params * np.hstack([1, (data[-p:, None] * data[-p:])[idx]]))

data = get_data()
print(LA(data, 100, False)[1])
