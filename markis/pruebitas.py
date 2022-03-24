# retocar while para que en impares la cuelta sea "corriendo" y en los pares "saltando"
# ejemplo de output:
# 1 --> corriendo
# 2 --> saltando
# 3 --> corriendo
# 4 --> saltando
# 5 --> corriendo


vueltas = 1
final = 5
is_running = True
# <> =

while vueltas != final:
    vueltas = vueltas +1
    if is_running:
        print (str(vueltas) + "--> corriendo")
    else:
        print(str(vueltas) + "--> saltando")
        is_running = not is_running



#\n - Newline.
#\t- Horizontal tab.
#\r- Carriage return.
#\b- Backspace.
#\f- Form feed.
#\'- Single Quote.
#\"- double quote.
#\\-Backslash.


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


def elegir_opcion():
    print(compra)
    print("Que desea hacer?")



def aregar_producto():
    agregar_producto = input()
    compra.append(agregar_producto)



def cambiar_producto():
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

def borrar_producto():
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

    


    