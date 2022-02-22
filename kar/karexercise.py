# Creación de personaje
# 
# Hay que hacer un script que permita al usuario la creación de un personaje
# mediante preguntas y respuestas.
#
# Para cada personaje hay que pedir la siguente información:
#   nombre
#   edad 
#   altura
#   clase
#   es soltero
# 
# Para cada atributo del personaje hay que validar y procesar la la entrada del usuario.
# En caso que la respuesta del usuario no sea valida hay que volver a pedirla hasta que lo sea
# La validación se hará de la siguiente manera:
#
# nombre.
#     Validar que el nombre solo contiene texto
#     Capitalizar cada palabra (primera mayuscula resto minusculas)


# edad.
#     Validar que la entrada contiene solo numeros
#     Guardar el valor en formato int
#
# altura. (en metros)
#     Validar que la entrada tiene es un float valido
#     Guardar el valor con decimal redondeado a 2 decimales justos
#
# clase. (crear una lista de clases con validación)
#     Validar que la clase es una clase valida



clase = ["guerrero", "mago", "arquero"]
intro = "Elige una clase para empezar tu aventura" + str(clase)
print(intro)


chose_class = input()
check_class = clase.count(chose_class)

while chose_class != clase:
    if check_class > 0:
        print("Has elegido: " + str(chose_class.capitalize()))
        break
    
    else:
        print("Esta no es un clase valida")
        chose_class = input()
        check_class = clase.count(chose_class)

        

#
# es soltero
#     Preguntar si el personaje es soltero
#     Guardar un valor booleano de si lo es o no.