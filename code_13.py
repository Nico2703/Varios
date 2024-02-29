import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2

def Funcion(r, g, m):
    u = -((g**2) / (np.exp( r*m / 197.3) *r))
    return u

def Gof(g, m, r, u, du):
    chisqr = sum((u - (Funcion(r, g, m)))**2 / du**2)
    DOF = len(u)-2  
    chisqr_red = chisqr/DOF
    GOF = 1 - chi2.cdf(chisqr, DOF) 
    return chisqr_red, GOF

r = np.array([2.9019, 3.26463, 3.62737, 3.99011, 4.35285]) 
u = np.array([-145.299, -111.289, -62.1917, -46.7048, -32.3581]) 
du = np.array([7.73623, 8.5017, 7.88238, 7.46152, 8.21121]) 

popt, pcov = curve_fit(Funcion, r, u)
g, m = popt
perr = np.sqrt(np.diag(pcov))
dg = perr[0]
dm = perr[1]

chisqr_red, GOF = Gof(g, m, r, u, du)

uplot = Funcion(r, g, m)
plt.scatter (r, u)
plt.plot(r, uplot, '--', color='blue')
plt.errorbar(r, u, fmt = 'ro', xerr = 0, yerr = du, ecolor = 'black')

print()
print("Gravedad: -", g, "[(MeV.fm)^1/2]") 
print("Delta gravedad: ±", dg, "[(MeV.fm)^1/2]")
print()
print("Masa: ", m, "[MeV/c^2]") 
print("Delta masa: ±", dm, "[MeV/c^2]")
print()
print("Chi cuadrado reducido: ", chisqr_red)
print("GOF: ", GOF)
print()

plt.xlabel('r')
plt.ylabel('U')
plt.grid()
plt.show()