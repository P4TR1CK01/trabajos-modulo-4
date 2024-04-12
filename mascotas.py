print('bienvenido ADMIN')
def tiendas ():
    mascotas=[]
    
    while True:
        #1.pedimos los datos
        especie = input('ingrese especie: ')
        if especie == '0':
            break
        precio = input ('Ingrese precio: ')
        cantidad=input('ingrese cantidad: ')
        #2.armamos diccionario
        nueva_mascota={
            'especie': especie,
            'precio': precio,
            'cantidad': cantidad
        }
        #3.agregamos diccionario a lista
        mascotas.append(nueva_mascota)
        
    print(mascotas)
    
    total = 0
    for mascota in mascotas:
        total+=mascota['precio']*mascota['cantidad']
        
    print=(f' en la tienda hay $ {total} en especie')
tiendas()