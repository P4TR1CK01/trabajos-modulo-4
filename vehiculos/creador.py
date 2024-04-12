  '''
from vehiculos import  Vehiculo
#crear una lista de instancia/objetos de clase

mis_vehiculos = []
#1. Ciclo infinito para ir llenando la lista

while True:
  modelo = input('Ingrese modelo: ') 
  if modelo == '0':
    break
  else:
    motor = int(input('Ingrese cilindrada: '))
    rendimiento  = int(input('Ingrese el rendimiento en kms por litro: '))
    automatico = None
    pregunta = input('¿Es de transmision automatica o manual(A/M): ?')
    if pregunta == 'A':
      automatico = True
    else:
      automatico = False
  nuevo_vehiculo = Vehiculo(modelo, motor, rendimiento, automatico)
  mis_vehiculos.append(nuevo_vehiculo)
#2. Una vez terminado el ciclo, imprimir todos los modelos#

for v in mis_vehiculos:
  print(f'{v.modelo} - {v.motor} - {v.rendimiento}')
  

  # Ocupar un ciclo infinito (con "0" para salir) para crear Vehiculos)
from vehiculos import Vehiculo
#lista de instancias 
mis_vehiculos = []

# 1.Ciclo infinito para ir llenado una lista
while True:
    print('\nIngrese datos del vehículo:')
    modelo = input('Ingrese modelo: ')
    if modelo == '0':
        break
    motor = int(input('Ingrese motor: '))
    rendimiento = int(input('Ingrese rendimiento: '))
    automatico = input('Es automático (si/no): ')
    if automatico == 'si':
        automatico = True
    else:
        automatico = False
    
    nombre = Vehiculo(modelo, motor, rendimiento, automatico)
    mis_vehiculos.append(nombre)

#2. Una vez terminado el ciclo, imprimir todos los modelos.

for vehiculo in mis_vehiculos:
    print(f'El modelo es: {vehiculo.modelo}')
    print(f'El motor es: {vehiculo.motor}')
    print(f'El rendimiento es: {vehiculo.rendimiento}')
    print(f'Es antomático: {"SI" if vehiculo.automatico else "NO"}')

  '''
  
from vehiculos import  Vehiculo

mis_vehiculos = []

while True:
  modelo = input('Ingrese el modelo: ')
  if modelo == '0':
    break
  motor = float(input('Ingrese la cilindrada del motor: '))
  
  rendimiento = float(input('Ingrese el rendimiento de su vehiculo (Kms/Lt): '))
  
  autom = input('¿es automatico? (S/N): ')
  #Transformamos la variable autom
  autom = True if autom == 'si' else False
  #creamos la instancia
  auto_nuevo = Vehiculo(modelo, motor, rendimiento, autom)
  #Lo agregamos a la lista
  mis_vehiculos.append(auto_nuevo)

for auto in mis_vehiculos:
  auto_automatico
  print(auto.modelo)
  