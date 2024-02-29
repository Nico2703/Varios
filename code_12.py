# Valores obtenidos - Code 8 9 10 11 

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def Funcion(f, a, b):
    v = a* f + b
    return v

def Raiz(a, b):
    f0 = -b/a
    return f0

def Error(a, b, f, v):
   n = len(f)
   sig = np.sqrt(np.sum((v - a * f - b) ** 2) / (n - 2))
   d_a = (np.sqrt(n) * sig) / np.sqrt(n * np.sum(f ** 2) - (np.sum(f)) ** 2)
   return d_a

def r2(a, b, f, v):
   vhat = a * f + b
   vbar = v.mean()
   ssreg = np.sum((vhat - vbar) ** 2)
   sstot = np.sum((v - vbar) ** 2)
   return ssreg / sstot

f1 = np.array([519.031, 549.450 , 688.073 , 740.740])
f = f1*(10**12)
v = np.array([0.5900025628553349, 0.7000064530646916, 1.2302093431176746, 1.3806285255712283])
          
popt, _ = curve_fit(Funcion, f, v)
a, b = popt
vplot = Funcion(f, a, b)
d_a = Error(a, b, f, v)
r_2 = r2(a, b, f, v)
plt.scatter (f, v)
plt.plot(f, vplot, '--', color='blue')
plt.errorbar(f, v, fmt = 'ro', xerr = 0, yerr = 0.1, ecolor = 'black')

f0 = Raiz(a,b)
q= 1.6*(10**-19)
planck= a*q
d_planck= d_a*q

print()
print("Pendiente= ", a)
print("Error pendiente= ±", d_a)
print("Ordenada al origen= ", b)
print()
print("F0= ", f0,"[Hz]")
print("Calidad del ajuste R^2: ", r_2)
print()
print("Constante de Planck= ",planck,"[J.s]")
print("Error constante de Planck= ±",d_planck)
print()

plt.xlabel('F')
plt.ylabel('V')
plt.grid()
plt.show()