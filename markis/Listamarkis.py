# Ejemplo Menu principal.
#
# > Bienvenid@ a la lista de la compra. Que quieres hacer:
# > 0. Salir
# > 1. Ver lista de la compra
# > 2. Agregar producto a la lista
# > 3. Modificar producto de la lista
# > 4. Quitar producto de la lista
# <

def dummy(name:str, num:int)->int:
    print("holaaa")
    print(name)
    print(num)
    print(num * 3)
    print("--------------------------------------------------------------------------")
    return num * 3
dummy("tomaa", 6)
resultado = dummy("yaaa", 5 )
print(resultado)

compra = []
#error linia 30
while True:
    print("0. Salir")
    print("1. Ver lista de la compra")
    print("2. Agregar producto a la lista")
    print("3. Modificar producto de la lista")
    print("4. Quitar producto de la lista")
    try:
        elegir_opcion = input()
        elegir_opcion= int(elegir_opcion)
    except ValueError:
        print("seleccion escribiendo el numero")
    if elegir_opcion == 0:
        print("Has elegido: Salir " + " Que tenga un buen dia")
        break
    elif elegir_opcion == 1:
        print(compra)
        print("Que desea hacer?")
    elif elegir_opcion == 2:
        agregar_producto = input()
        compra.append(agregar_producto)
    elif elegir_opcion == 3:
        print(compra)
        modificar_producto = input()
        print ("Por que producto desea cambiarlo")
        cambiar_producto = input()
        for producto in compra:
            if modificar_producto == producto:
                compra.remove(modificar_producto)
                compra.append(cambiar_producto)
                print("Has modificado " + modificar_producto + "por" +  cambiar_producto)
                print(compra)
                break
            

    elif elegir_opcion == 4:
        print(compra)
        print ("Que articulo desea quitar de la lista?")
        print ("Escriba el articulo que desea quitar?")
        try:
            borrar = input()
            compra.remove(borrar)
            print("El producto '" + borrar + "' ha sido eliminado de la lista, quedan: ", len(compra))
        except ValueError:
            print("el producto '"  + borrar +  "' no esta en la lista")

    else:
        print("opcion no valida")









    


        
    




    