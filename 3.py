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

def SSA(x, r):
    tau = (len(x) + 1) // 2
    n = len(x) + 1 - tau
    X = np.array([x[i: i + n] for i in range(tau)])
#    print(X)
    _, V = np.linalg.eig(X @ X.T / n)
    v_tau = V[-1, : r]
    v_tau_V_spark_T = v_tau @ V[: tau - 1, : r].T
    denom = 1 - v_tau @ v_tau.T
    Q = x[-tau + 1:]
    return (v_tau_V_spark_T @ Q) / denom

data = get_data()
print(SSA(data, 100))
