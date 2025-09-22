import numpy as np
import matplotlib.pyplot as plt

# Vi använder din force_newtonsmill
def simpson(func, a, b, n):
    if n % 2 == 1:
        raise ValueError("n måste vara jämnt")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = func(x)
    return (h/3) * (fx[0] + 4*np.sum(fx[1:-1:2]) + 2*np.sum(fx[2:-2:2]) + fx[-1])

p = 9810.0
def w(y):
    return 20 - 10*np.exp(-0.0012*y**2)
def integrand(y, D):
    return p * (D - y) * w(y)
def force_newtonsmill(D, n):
    return simpson(lambda y: integrand(y, D), 0, D, n)

# Konvergensstudie
D = 20
F_ref = force_newtonsmill(D, 4000)   # "referensvärde"
n_list = [10, 20, 40, 80, 160, 320, 640]
errors = []

for n in n_list:
    F_n = force_newtonsmill(D, n)
    errors.append(abs(F_n - F_ref))

# Plotta fel mot n (eller h = D/n)
h_list = [D/n for n in n_list]

plt.figure(figsize=(7,5))
plt.loglog(h_list, errors, '-o', label="Simpsons metod")
plt.loglog(h_list, [errors[0]*(h/h_list[0])**4 for h in h_list], '--', label="Referens O(h^4)")
plt.xlabel("Steglängd")
plt.ylabel("Fel")
plt.title("Konvergensstudie för Simpsons metod")
plt.legend()
plt.grid(True)
plt.show()