import matplotlib.pyplot as plt 
import numpy as np 
 
# Data experimental 
x = np.array([-55, -10, 25, 100, 150]) 
y = np.array([-528,-119, 252, 972, 1507]) 

# Devuelve la pendiente y la ordenada al origen del ajuste lineal al dataset
def linefit(x, y): 
   x_prom = x.mean() 
   pend = (y * (x - x_prom)).sum() / (x * (x - x_prom)).sum() 
   yint = y.mean() - pend * x_prom 
   return pend, yint 

# Calcula el r-squared de la funcion
def r2(pend, yint, x, y):
   yhat = pend * x + yint
   ybar = y.mean()
   ssreg = np.sum((yhat - ybar) ** 2)
   sstot = np.sum((y - ybar) ** 2)
   return ssreg / sstot 

# Calcula los errores en los coeficientes
def err_parametros(pend, yint, x, y):
   n = len(x)
   sig = np.sqrt(np.sum((y - pend * x - yint) ** 2) / (n - 2))
   d_pend = (np.sqrt(n) * sig) / np.sqrt(n * np.sum(x ** 2) - (np.sum(x)) ** 2)
   d_yint = d_pend * np.sqrt(np.sum(x ** 2) / n)
   return d_pend, d_yint

# Imprime una línea en base a una pendiente y una ordenada al origen 
def abline(pend, yint, x, y, d_pend, d_yint, r_2):
   print('Pendiente: ', pend)
   print('Ordenada: ', yint)
   print('Error en la pendiente: ', d_pend)
   print('Error en la ordenada: ', d_yint)
   print('Calidad del ajuste R^2: ', r_2)
   print ()
   
# Crea el grafico
   y_vals = yint + pend * x
   plt.figure(1, figsize = (6, 4))
   plt.plot(x, y, 'o', color = 'red')
   plt.plot(x, y_vals, '--')
   plt.xlabel('Temperatura [°C]')
   plt.ylabel('Voltaje [mV]')
   plt.grid()
   plt.show()

pend, yint = linefit(x,y)
r_2 = r2(pend, yint, x, y)
d_pend, d_yint = err_parametros(pend, yint, x, y)
abline(pend, yint, x, y, d_pend, d_yint, r_2)
