class Vehiculo:
  #Atributo de clase
  num_vehiculos = 0
  #Constructor
  def __init__(self, modelo, motor, rendimiento, autom=False):
    #Atributos de instancia
    self.modelo = modelo
    self.motor = motor
    self.rendimiento = rendimiento
    self.automatico = autom
    Vehiculo.num_vehiculos += 1
    
  def get_consumo (self, kms):
    #Dada una cantidad de kms, me calcula litros de combustible que necesito
    consumo = kms / self.rendimiento
    return consumo

  def tocar_bocina (self):
    print('BIP HOOOOOONCK!!!')

  def calcular_gasto (self, kms , precio_lt_combustible):
    litros_consumidos = self.get_consumo(kms)
    return litros_consumidos * precio_lt_combustible


yamaha =  Vehiculo('Yamaha enticer', 125, 35)
palio = Vehiculo('Fiat Palio Fire', 1300, 16)
suzuki = Vehiculo('Suzuki DZire', 1200, 20,  True)

#Imprimir un atributo de instancia
print('El modelo del 3° vehiculo es ' + suzuki.modelo)

#imprimir un atributo de clase
print(f'En total existen {Vehiculo.num_vehiculos} vehículos')

dist_vina_ptomontt = 1000 + 120
print(suzuki.get_consumo(dist_vina_ptomontt))

suzuki.tocar_bocina()

print(f'De viña a Pto Montt en un {suzuki.modelo} vamos a gastar: ')
print(suzuki.calcular_gasto(1120, 1400))