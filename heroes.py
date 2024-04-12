class Hero:
  num_heroes = 0 # Estatico, pertenece a la clase
  def __init__ (self, name: str, health: int, power: int): # Constructor
    self.name = name
    self.health = health
    self.power = power
    self.hp = health 
    self.bag = []
    Hero.num_heroes += 1
    
  @staticmethod   #Son como metodos generales. Son como una funcion, no requieren instancia
  def print_num_heroes():
    print(f'En este momento hay {Hero.num_heroes} heroes')
    
  def gritar (self):
    print(f'BANZAAAAAAAAYYYY yo {self.name} te matare!!!')
    
  def atacar(self, victim):
    victim.hp -=  self.power
    
  @staticmethod
  def is_dead(person_hp):
    if person_hp <= 0 :
      return True
    else:
      return False
    
    
aragorn = Hero('Aragorn', 100, 10) #Primera instancia
rayhar = Hero('Rayhar', 100, 12)
yamcha = Hero('Yamcha', 10, 2)

gohan = Hero('Gohan', 100, 10)

aragorn.gritar()  #es una instancia de la clase Hero

Hero.print_num_heroes()
Hero.is_dead(aragorn.hp)

aragorn.atacar(rayhar)
print(f'{rayhar.name} tiene {rayhar.hp} puntos de vida')

rayhar.atacar(yamcha)
print(Hero.is_dead(yamcha.hp))