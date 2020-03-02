import numpy as np
import math
import statsmodels.api as sm
import statsmodels.formula.api as smf

def ro2(n, nn):
    ret = 0
    for i in range(min(n, nn, k)):
        ret += (time_series[n - k + i][0] - time_series[nn - k + i][0]) ** 2 + (time_series[n - k + i][1] - time_series[nn - k + i][1]) ** 2
    return ret

def tetta(a):
    if a < 0:
        return 0
    else:
        return 1

N = 2000
c = 0
a = 2
b = 1
sum = 0
time_series = []
delta_t = 0.01
for i in range(N):
    t = i * delta_t
    time_series.append([a * math.cos(t), b * math.sin(t)])
for k in range(20, 28):
    l = 1 / 128
    ro = []
    for n in range(k, N):
        for nn in range(k, N):
            ro.append(ro2(n, nn))
    while l >= 1 / 1024:
#        T = delta_t * N
        d = 0
        for n in range(len(ro)):
            sum += tetta(l**2 - ro[n])
        sum /= N**2
        c = sum
        d = math.log(c) / math.log(l)
        print('k =', k)
        print('l =', l)
        print('c =', c)
        print('d =', d)
        print()
        l /= 2
