# Ejemplo Menu principal.
#
# > Bienvenid@ a la lista de la compra. Que quieres hacer:
# > 0. Salir
# > 1. Ver lista de la compra
# > 2. Agregar producto a la lista
# > 3. Modificar producto de la lista
# > 4. Quitar producto de la lista
# <
compra = []

while True:
    print("0. Salir")
    print("1. Ver lista de la compra")
    print("2. Agregar producto a la lista")
    print("3. Modificar producto de la lista")
    print("4. Quitar producto de la lista")
    elegir_opcion = input()
    elegir_opcion= int(elegir_opcion)
    if elegir_opcion == 0:
        print("Has elegido: Salir" + "Que tenga un buen dia")
        break
    if elegir_opcion == 1:
        print(compra)
        print("Que desea hacer?")
    if elegir_opcion == 2:
        agregar_producto = input()
        compra.append(agregar_producto)
    if elegir_opcion == 3:
        for index, value in enumerate(compra):
            if value == compra:
                compra[index] = modificar_producto
        print(compra)
        print("Que producto queires modificar?")
        modificar_producto = input()
        
    




    