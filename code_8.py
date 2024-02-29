# Amarillo

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def Funcion(v, a, b, c):
    i = a* (np.exp(b*(v+c))-0.899)
    return i

def Raiz(b, c):
    v0 = (np.log(0.899)/b) -c
    return v0

v = np.array([-3.00000, -2.73333, -2.46667, -2.20000, -1.93333, -1.66667, -1.40000, -1.13333, -0.86667, -0.60000, -0.59444, -0.58889, -0.58333, -0.57778, -0.57222, -0.56667, -0.56111, -0.55556, -0.55000, -0.48889, -0.42778, -0.36667, -0.30556, -0.24444, -0.18333, -0.12222, -0.06111]) 
i0 = np.array([-7.37166, -7.37154, -7.37106, -7.36926, -7.36248, -7.33693, -7.24064, -6.87778, -5.51042, -0.35770, -0.16114, 0.04093, 0.24866, 0.46221, 0.68175, 0.90744, 1.13945, 1.37797, 1.62317, 4.81903, 9.15038, 15.02066, 22.97663, 33.75934, 48.37314, 68.17920, 95.02232 ]) 
i = i0*(10**-12)         
        
popt, _ = curve_fit(Funcion, v, i)
a, b, c = popt
iplot = Funcion(v, a, b, c)
plt.scatter (v, i)
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