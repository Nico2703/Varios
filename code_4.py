import matplotlib.pyplot as plt
import numpy as np
import math
from tabulate import tabulate
from scipy.optimize import curve_fit

''' l2 = 2l1 ; l3 = 4l1 '''

h0 = 4.135**-15
h = h0/(2*math.pi)
m = l1 = 1

n1 = np.array([1,1,1,1,1,1,1,1,1,1])
n2 = np.array([1,1,1,1,2,2,2,2,3,3])
n3 = np.array([1,2,3,4,1,2,3,4,1,2])
En = np.empty([10])
Array = []

for i in range(0,10):
  E0 = ((h**2)*(math.pi**2)/2*m)*((n1[i]**2/l1**2)+(n2[i]**2/(2*l1)**2)+(n3[i]**2/(4*l1)**2))
  E = E0*(10**19)
  En[i] = E
  
Listan1 = n1.tolist()
Listan2 = n2.tolist()
Listan3 = n3.tolist()
ListaEn = En.tolist()

for i in range(0,10):
  Array.append([Listan1[i],Listan2[i],Listan3[i],ListaEn[i]])

print("ORDENADO POR NIVEL")
print("{:<5} {:<5} {:<15} {:<0}".format('n1','n2','n3','Energía'))
for i in range(0,10):
  print ("{:<5} {:<5} {:<5} {:<5} {:<0}  ".format("{0:.0f}".format(Array[i][0]),"{0:.0f}".format(Array[i][1]),"{0:.0f}".format(Array[i][2]),"{0:.6f}".format(Array[i][3]),"*(1/(m*l1) x10^-19 [eV]"))

Array=sorted(Array, key = lambda x:x[3])
print()

print("ORDENADO POR ENERGÍA")
print("{:<5} {:<5} {:<15} {:<0}".format('n1','n2','n3','Energía'))
for i in range(0,10):
  print ("{:<5} {:<5} {:<5} {:<5} {:<0}  ".format("{0:.0f}".format(Array[i][0]),"{0:.0f}".format(Array[i][1]),"{0:.0f}".format(Array[i][2]),"{0:.6f}".format(Array[i][3]),"*(1/(m*l1) x10^-19 [eV]"))
