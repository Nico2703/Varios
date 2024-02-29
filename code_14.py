import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def Funcion(x,a,b):
  y = a*np.sin(b*x) 
  return y

x=np.array([0,1,2,3,4,5,6,7,8])
y=np.array([0.2,7,9.5,6.8,-0.1,-7.1,-10.4,-6.7,0.1])

popt, _ = curve_fit(Funcion, x, y)
a, b = popt
plt.scatter(x,y)

xplot = np.linspace(0, 8, 1000)
yplot = Funcion(xplot,a, b)
plt.plot(xplot, yplot, '--', color='red')

maximo=yplot.max()
minimo=yplot.min()
print ('Máximo:',maximo)
print ('Mínimo:',minimo)

plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
