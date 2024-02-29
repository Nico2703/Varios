# Verde

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def Funcion(v, a, b, c):
    i = a* (np.exp(b*(v+c))-0.5201)
    return i

def Raiz(b, c):
    v0 = (np.log(0.5201)/b) -c
    return v0

v = np.array([-3.00000, -2.75556, -2.51111, -2.26667, -2.02222, -1.77778, -1.53333, -1.28889, -1.04444, -0.80000, -0.78333, -0.76667, -0.75000, -0.73333, -0.71667, -0.70000, -0.68333, -0.66667, -0.65000, -0.57778, -0.50556, -0.43333, -0.36111, -0.28889, -0.21667, -0.14444, -0.07222, 0.00000]) 
i0 = np.array([-4.26472, -4.26461, -4.26425, -4.26301, -4.25884, -4.24476, -4.19725, -4.03696, -3.49615, -1.67147, -1.44728, -1.20371, -0.93908, -0.65158, -0.33922, 0.00014, 0.36884, 0.76941, 1.20461, 3.56916, 6.95595, 11.80693, 18.75512, 28.70717, 42.96173, 63.37888, 92.62285, 134.50970]) 
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