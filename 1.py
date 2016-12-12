from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math as m

f = lambda x, y: x**3 + y*x
u = lambda x: 7*m.e**((x**2)/2) - x**2 - 2
a = 0.1
b = 1.0
n = 10
h = (b - a)/(n - 1)

u0 = u(a)
u1 = u(a + h)
u2 = u(a + h*2)
u3 = u(a + h*3)

U = np.zeros(n)
X = [a + i*h for i in range(n)]
U_real = [u(x) for x in X]
U[0] = u0
get_f = lambda i: f(X[i], U[i])
for i in range(1, 4):
    k1 = h*get_f(i-1)
    k2 = h*f(X[i-1] + h/2, U[i-1] + k1/2)
    k3 = h*f(X[i-1] + h/2, U[i-1] + k2/2)
    k4 = h*f(X[i-1] + h, U[i-1] + k3)
    U[i] = U[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6
print(h**2)
for i in range(4, n):
    U[i] = U[i-1] + h*(55*get_f(i-1) - 59*get_f(i-2) + 37*get_f(i-3) - 9*get_f(i-4))/24
print(h**5)
plt.plot(X, U, X, U_real)
plt.show()
