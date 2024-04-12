
class Pizza:
  proteina = ['pollo', 'Vacuno', 'carne vegetal']
  vegetales = ['aceitunas', 'tomates', 'champiñon']
  masas = ['tradicional', 'delgada']

  #constructor
  def __init__(self, masa, proteina, vegetal_1, vegetal_2):
    self.masa = masa
    self.proteina = proteina
    self.vegetal_1 = vegetal_1
    self.vegetal_2 = vegetal_2
    
  @staticmethod
  def esta_presente(elemento, lista): #como no tiene nada que ver se establece como metodo estatico
    '''
    for item in lista:
      if item == elemento:
        return True
    return False
    '''
    return elemento in lista
  
  def realzar_pedido():
    masa = input('Ingresa masa (Tradicional/Delgada): ').lower()
    if not Pizza.esta_presente(masa, Pizza.masas):
      print('La masa ingresada no existe')
      return    
    proteina = input('Ingrese tipo de carne (pollo/vacuno/carne vegetal): ').lower()
    if not Pizza.esta_presente(proteina, Pizza.proteina):
      print('La proteina ingresada no existe')
      return
    vegetal_1 = input('Ingrese tipo de vegetal (aceituna/tomate/champiñon): ').lower()
    if not Pizza.esta_presente(vegetal_1, Pizza.vegetales):
      print('El vegetal ingresado no existe')
      return
    vegetal_2 = input('Ingrese tipo de vegetal (aceituna/tomate/champiñon): ').lower()
    if not Pizza.esta_presente(vegetal_2, Pizza.vegetales):
      print('El vegetal ingresado no existe')
      return 
    pizza = Pizza(masa, proteina, vegetal_1, vegetal_2)
    return pizza
    
if __name__ == '__main__':
  pizza = Pizza.realzar_pedido()
  print(pizza)