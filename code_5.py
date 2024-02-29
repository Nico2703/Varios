import ast
import sys
import re

def tres (cadena):
  return cadena[2:3]

def div (cadena):
  return int(cadena%2)

entrada=[]
list=[]
while entrada != "Sale":
  print()
  print("Ingresar 'Sale' para terminar")
  entrada = input("Ingrese texto: ")
  if entrada == "Sale":
    print("Programa terminado")
    break
  list=entrada.split(" ")

  print("Lista ingresada: ",list)
  print()
  list.sort()
  print("Lista ordenada: ",list)
  print()

  for x in list:
    print("Tercer carácter: ",tres(x))

  numb=[] 
  numb=[float(s) for s in re.findall(r'-?\d+\.?\d*', entrada)]
  print()
  print("Números encontrados: ",numb)

  for x in numb:
    div(x)
    if div(x)>0:
      sys.stdout.write("Valor flotante  ")
    else:
      sys.stdout.write("Valor entero  ")
  print()