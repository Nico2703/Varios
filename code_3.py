import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from scipy.optimize import curve_fit

g = 9.8
t = [n*0.25 for n in range (20)]

print ("Ingrese posición inicial: ")
yi = float(input())
print ("Ingrese velocidad inicial: ")
vi = float(input())
print()

print ("{:<15} {:<20} {:<25} {:<30}".format('Tiempo [s]','Posición [m]','Posición inicial [m]','Velocidad inicial [m/s]'))
for i in range(0,20):
  y = yi + vi*t[i] - 0.5*g*(t[i]**2)
  print ("{:<15} {:<20} {:<25} {:<30}".format("{0:.2f}".format(t[i]),"{0:.3f}".format(y),"{0:.3f}".format(yi),"{0:.3f}".format(vi))) 

print()

def Funcion(x,a,b):
  y = a + b*x - 0.5*9.8*(x**2)
  return y

x = np.linspace(0, 5, 20)
y = yi + vi*x - 0.5*g*(x**2)

popt, _ = curve_fit(Funcion, x, y)
a, b = popt

yplot = Funcion(x,a, b)
plt.plot(x, y, 'o', color='red')
plt.plot(x, yplot, '--', color='blue')

plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m]')
plt.grid()
plt.show()
