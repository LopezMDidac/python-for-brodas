
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

#if soltero = True: 
#    print("Si")
#    if False:
#       print("no")

print("Datos personales del aventurero:")
print("******** Apodo : " + apodo)
print("******** Edad : " + str(edad))
print("******** Altura : " + str(altura_m))
print("******** Clase : " + clase)
print("******** Tiene pareja ? : " + str(soltero))
if soltero is True:
    print("Married : NO")
if soltero is False:
    print("Married : YES")