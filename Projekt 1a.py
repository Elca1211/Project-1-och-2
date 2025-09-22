import numpy as np
import matplotlib.pyplot as plt


rho = 1000
g = 9.81
H = 12

y = np.array([0, 2, 4, 6, 8, 10, 12])
w = np.array([10.00, 11.18, 12.18, 12.20, 13.00, 13.50, 14.00])

def force(x):
    w_x = np.interp(x, y, w) 
    return rho * g * (H - x) * w_x


def trapets(func, a, b, n): 
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = func(x)
    T = h * (np.sum(fx) - (fx[0] + fx[-1]) / 2)
    return T


resultat = (trapets(force, 0, 12, 100))

xx = np.linspace(0, 12, 300) 
yy = force(xx)
f_points = rho * g * (H - y) * w
print(f'Den resulterande kraften är = {resultat} N')

plt.figure(figsize=(8,5))
plt.plot(xx, yy, label="Interpolerad integrand f(y)")
plt.scatter(y, f_points, color="red", label="Mätpunkter")
plt.xlabel("y [m]")
plt.ylabel("f(y) [N/m]")
plt.title("Integranden för dammkraften")
plt.legend()
plt.show()



T_h = trapets(force, 0, 12, 6)    
T_2h = trapets(force, 0, 12, 3)
E_h = (T_h - T_2h) / ((2**2)-1)
print(f'Diskritiseringsfelet = {E_h} N')