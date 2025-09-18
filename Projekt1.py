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


resultat = (trapets(force, 0, 12, 500))

xx = np.linspace(0, 12, 300) 
yy = force(xx)
f_points = rho * g * (H - y) * w
print(resultat)

plt.figure(figsize=(8,5))
plt.plot(xx, yy, label="Interpolerad integrand f(y)")
plt.scatter(y, f_points, color="red", label="Mätpunkter")
plt.xlabel("y [m]")
plt.ylabel("f(y) [N/m]")
plt.title("Integranden för dammkraften")
plt.legend()
plt.show()