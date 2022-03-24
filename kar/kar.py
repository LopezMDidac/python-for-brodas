# Agregar menu: 0. Salir 1. Ver Personaje
# Cambiar de variables a Diccionario
# Trabajarlo en funciones
# [Extra] 2. Agregar personaje



#Saludo inicial, pedimos input del nombre y lo recogemos en el segundo print.
#print("Hola como te llamas?")
#nombre = input()
#print("Bienvenido " + nombre)  

apodo = "kar"
edad = 20
altura_m = 1.75
clase = "clerigo"
soltero = False
pareja = soltero


entrada_apodo = None
while entrada_apodo != apodo:
    print("Hola, cual es tu apodo?")
    entrada_apodo = input()
    if entrada_apodo == apodo:    
        print("Datos personales del aventurero:")
        print("******** Apodo : " + apodo)
        print("******** Edad : " + str(edad))
        print("******** Altura : " + str(altura_m))
        print("******** Clase : " + clase) 
        if soltero is True:
            print("Married : No")
        if soltero is False:
            print("******** Tiene pareja ? : Si")
        
    elif  entrada_apodo == "Q" or entrada_apodo == "q":
        break
    else:
         print("No eres el elegido")

 



#if soltero = True: 
#    print("Si")
#    if False:
#       print("no")

#print("Datos personales del aventurero:")
#print("******** Apodo : " + apodo)
#print("******** Edad : " + str(edad))
#print("******** Altura : " + str(altura_m))
#print("******** Clase : " + clase)
#print("******** Tiene pareja ? : " + str(soltero))
#if soltero is True:
    #print("Married : No")
#if soltero is False:
    #print("******** Tiene pareja ? : Si")

#if 