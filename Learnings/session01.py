is_staying = True
aka = "hulk"
edad = 15
altura_m = 1.78
clase = "media"
es_soltero = False
if es_soltero:
    marriage = "NO"
else:
    marriage = "YES"

while is_staying:
    print("Hola humano, Como te llamas??")
    nombre = input()
    if nombre == aka:
        print("Encatado de conocerte " + nombre)
        print("Name: " + aka)
        print("Age: " + str(edad))
        print("Heigh: " + str(altura_m))
        print("Social estatus: " + clase)
        print("Married : " + marriage)
        is_staying = False
    elif nombre.upper() == "Q":
        is_staying = False
    else:
        print("no compatible")
