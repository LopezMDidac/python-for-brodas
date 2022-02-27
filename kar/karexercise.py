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
intro_edad = "Introduce la edad de tu psersonaje"
print(intro_edad)
age = input()

try:
    age = int(age)
except ValueError:
    age = input()





# altura. (en metros)
#     Validar que la entrada tiene es un float valido
#     Guardar el valor con decimal redondeado a 2 decimales justos

intro_altura = "Introduce la altura deseada para tu personaje en metros "


print(intro_altura)
altura_char = input()

try:
    altura_char = float(altura_char)
except ValueError:
    print("La altura de tu personaje tiene que ser un numero ej: 1.85")
    altura_char = (input())

altura_char = round(altura_char, 2)
#print de comprobación redondeo
print("Tu personaje mide: " + str(altura_char) + " metros")






# clase. (crear una lista de clases con validación)
#     Validar que la clase es una clase valida





clase = ["guerrero", "mago", "arquero"]
intro_clase = "Elige una clase para empezar tu aventura" + str(clase)


print(intro_clase)
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

intro_soltero = "En tu aventura te esposaste con alguna belleza? si o no"
soltero = None

print(intro_soltero)
is_soltero = input()
while is_soltero != "si" or is_soltero != "no":   
    if is_soltero == "si":
        soltero = True
        print("Afortunado aventurero")
        break
    
    if is_soltero == "no":
        soltero = False
        print("Mejor solo que mal acompañado")
        break
    
    else:
        print("Contesta unicamente con si o no")
        is_soltero = input()

