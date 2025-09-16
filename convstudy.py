import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def humps(x):
    return 1 / (( x - 0.3)**2 + 0.01) + 1/(( x - 0.9)**2 + 0.04) - 6

def trapets(func, a, b, n): 
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = func(x)
    T = h * (np.sum(fx) - (fx[0] + fx[-1]) / 2)
    return T

def simpson(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = func(x)
    S = (h/3) * (fx[0] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-2:2]) + fx[-1])
    return S

a = 0
b = 1.2
xx = np.linspace(a, b, 200)
# plt.plot(xx, humps(xx))

Iref, err = quad(humps, a, b)
steps = 10
n = 4
hvec = np.zeros(steps)
EThvec = np.zeros(steps)
EShvec = np.zeros(steps)
for ind in range(10):
    Th = trapets(humps, a, b, n)
    T2h = trapets(humps, a, b, int(n/2))
    Sh = simpson(humps, a, b, n)
    S2h = simpson(humps, a, b, int(n/2))
    ETh = Iref - Th
    ET2h = Iref - T2h
    ESh = Iref - Sh
    ES2h = Iref - S2h
    hvec[ind] = (b - a) / n
    EThvec[ind] = ETh
    EShvec[ind] = ESh
    # print(ESh) 
    # print(f'ET(2h) / ET(h): {ET2h / ETh}')
    # print(f'ES(2h) / ES(h): {ES2h / ESh}') 
    n = 2 * n

# för att få fram grafen
plt.loglog(hvec, EThvec, '-ob')
plt.loglog(hvec, EShvec, '-xr')
plt.show()

n = 4 
T = trapets(humps, a, b, n)
S = simpson(humps, a, b, n)
ET = Iref - T
ES = Iref - S
print(ET)
print(ES)
