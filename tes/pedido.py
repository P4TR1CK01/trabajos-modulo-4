from Te import Te

def pedido():
  print ("Elija una clase de Té")
  tipo_te = input('Ingrese 1 para Té negro, 2 para Té verde  o 3 para Infusión de hierbas: ')
  
tiempo_preparacion, recomendacion = Te.instrucciones(eleccion)

print (f'La preparacion de su té tomará {tiempo_preparacion}, y se {recomendacion}')