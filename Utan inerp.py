import numpy as np
import matplotlib.pyplot as plt

p = 1000 * 9.81 # Tryckkonstanten 
y = np.array([0, 2, 4, 6, 8, 10, 12])
w = np.array([10.00, 11.18, 12.18, 12.20, 13.00, 13.50, 14.00])
H = 12.0 

f = (H - y) * w
h = 2

trapets = h * ( 0.5*f[0] + f[1:-1].sum() +  0.5 * f[-1] )

F = p * trapets 
f_points = p * (H - y) * w
print(f'Den resulterande kraften är = {F} N')

plt.figure(figsize=(8,5))
plt.plot(y, f, marker = 'o', label = "f(y) = (H-y) * w(y)")
plt.xlabel("y [m]")
plt.ylabel("f(y) [N/m]")
plt.title("Integranden för dammkraften")
plt.legend()
plt.grid(True)
plt.show()
