'''class Vehiculo():
#Atributos de Clase
  num_vehiculos = 0
#Constructor
def __init__(self, moedelo, motor, rendimiento, autom=False):
#Atributos de instancia
    self.modelo = moedelo
    self.motor = motor
    self.rendimiento = rendimiento
    self.automatico = autom
    Vehiculo.num_vehiculos += 1
    
yamaha = Vehiculo('Yamaha enticer', 125, 35)
palio =  Vehiculo('Fiat Palio Fire', 1300, 16)
suzuki =  Vehiculo('Suzuki Dzire', 1200, 20,  True)
#Imprimir un  atributo de instancia
print('El modelo del 3° vehiculo es ' + suzuki.modelo)
#imprimir el atributo de clase
print(f'En total existen {vehiculo.num_vehiculos} vehículos')

'''
'''
class Character:
  def __init__(self, name, race, strenght, health):
    self.name = name
    self.race = race
    self.strength = strenght
    self.health = health
'''
'''
yamaha = {
  'modelo': 'yamaha enticer',
  'motor': 125,
  'rendimiento': 35,
  'automatico':  false
}

zuzuki = {
  'modelo': 'zuzuki dezire',
  'motor': 1200,
  'rendimiento': 20,
  'automatico':  false
  }

corsa = {
  'modelo': 'chevrolet corsa',
  'motor': 1300,
  'rendimiento': 16,
  'automatico':  true
  }
  
#vamos a inicializar un constructor para generar vehiculos
class Vehiculo:  #clases siempre debes estar capitalizada(empezar con mayuscula)(Vehiculo)
  def __init__(self, modelo, motor, rendimiento, automatico=False):
    self.modelo = modelo
    self.motor = motor
    self.rendimiento = rendimiento
    self.automatico = automatico
    
yamaha =  Vehiculo('Yamaha enticer', 125, 35) #No es necesario pasar el 4to argumento por que es un valor por defecto

zuzuki = Vehiculo('Zuzuki dezire', 1200, 20) 

corsa = Vehiculo('Chevrolet corsa', 1300, 16, True)

#print('El atributo modelo del tercer objeto es ' + corsa.modelo) 
#print (type (corsa)) 

  '''