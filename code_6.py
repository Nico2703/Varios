import csv
import json
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

with open('/content/drive/MyDrive/3° 11 Ferrand, Nicolás Física Electrónica/Colab Notebooks/particle_data.json') as file:
    data = json.load(file)
    print()

data_string = json.dumps(data)
datos = json.loads(data_string)
print('Datos:', datos)

valores=datos.values()

energia=[]
momento=[]

for i,j,k in datos.values(): 
  energia.append(i)
  momento.append(j)

print("Valores de energía: ",energia)
print("Valores de momento: ",momento)      
print()

plt.plot(momento, energia, 'o', color='red')
plt.xlabel('Momento')
plt.ylabel('Energía')
plt.grid()
plt.show()

tabla=[]
for m in range (31):
    tabla.append([energia[m],momento[m]])
print(tabla)

headers = ('Energia ', ' Momento ')

with open('datos-tabla.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(tabla)
