from scipy.odr import*
import matplotlib.pyplot as plt
import numpy as np

def f(B, x):
  return B[0]*x

k = 6.924e-4
y = np.array([40,90,150,245])
x0 = np.array([0.02,0.03,0.04,0.05])
x = x0**2
dy = np.array([5,5,5,5])
dx = np.array([0.002,0.002,0.002,0.002])

linear = Model(f)
mydata = RealData(x, y, sx = dx, sy = dy)
myodr = ODR(mydata, linear, beta0 = [0., ])
myoutput = myodr.run()

Pendiente = (myoutput.beta[0]*2)/((k**2)*(1.5**2))
Error = Pendiente - (1.76e11)
print("(e/m) = ",round(Pendiente,4))
print("Error en (e/m) = ±",round(Error,4))