# Azul

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def Funcion(v, a, b, c):
    i = a* (np.exp(b*(v+c))-0.0372)
    return i

def Raiz(b, c):
    v0 = (np.log(0.0372)/b) -c
    return v0

v = np.linspace (-3,0,27)
a=  8.199802068631756e-12
b=  4.9749112820496695
c=  0.5686002548151077

iplot = Funcion(v, a, b, c)
plt.plot(v, iplot, '--', color='blue')

v0 = Raiz(b,c)

print()
print("A: ", a) 
print("B: ",b)
print("C: ",c)
print("V0: ",v0)
print()

plt.xlabel('v')
plt.ylabel('i')
plt.grid()
plt.show()