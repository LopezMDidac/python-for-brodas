# nombre.
# Validar que el nombre solo contiene texto
# Capitalizar cada palabra (primera mayuscula resto minusculas)
#print("Cual es tu nombre?")
#char_name = input()

#if char_name




# clase.
# Validar que la clase es una clase valida. (crear lista de clasis con validado)
from ast import Or


clase = ["warrior", "rogue", "mage"]
print("Choose your class " + str(clase))

while True:
    choose_clase = input()
    class_check = clase.count(choose_clase)
    if class_check > 0:
        print("Clase selected: " + str(choose_clase.capitalize()))
        break
    else:
        print("Not valid")
        
# es soltero
#     Preguntar si el personaje es soltero
#     Guardar un valor booleano de si lo es o no.


soltero = None

while soltero  is True:
    print("Estas soltero?")
    is_soltero = input()
    if is_soltero == "si":
        soltero = True
        print("Buena compañia teneis")

    if is_soltero == "no":
        soltero = False
        print("No necessito ninguna moza")
        
    else:
        print("Solo aceptamos palabras")

# altura. (en metros)
# Validar que la entrada tiene es un float valido
# Guardar el valor con decimal redondeado a 2 decimales justos
try:
    age = int(age)
except ValueError:
    age = input


while True:
    print("Cual es tu altura")
    altura_char = input()
    try:
        altura_char = float(altura_char)
        break
    except ValueError:
        print("la altura debe ser un numero")
        

altura_char = round(altura_char, 2)    
print("Tu altura es: " + str(altura_char) + " metros")


    

        