import numpy as np

def Triangular(n):
  t = (n*(n+1))/2
  return int(t)

print ('Ingrese enésimo valor de la serie:')
try:
  n = int(input())
  if n >= 2:
    print ('Resultado:',Triangular(n))
  else:
    print ('Error! Ingrese número mayor a 2')
except:
  print ('Error! Ingrese un número')