# 1 0 0 1 -1 0 1 => a, b
# 1 0 0 1 -1 0 3 => p
import numpy as np
import math

s = input().split()
x = []
y = []
t = int(s[6])
for i in range(3):
    x.append(float(s[i * 2]))
    y.append(float(s[i * 2 + 1]))
if t == 3:
    p = y[0] * y[0] / (2 * x[0])
    print('p =', p)
else:
    c = 0 # = 1 / a^2
    d = 0 # = 1 / b^2
    a = 0
    b = 0
    f = [1.0, 1.0]
    m = [[x[0]**2, y[0]**2], [x[1]**2, y[1]**2]]
    print(*m)
    c, d = np.linalg.solve(m, f)
    print(c, d)
    if t == 1:
        a = math.sqrt(1 / c)
        b = math.sqrt(1 / d)
    else:
        if c < 0:
            c, d = d, c
        a = math.sqrt(1 / c)
        b = math.sqrt(1 / -d)
    print('a =', a)
    print('b =', b)
