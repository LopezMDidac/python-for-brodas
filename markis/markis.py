
nombre = None
aka = "hulk"
edad = 15
altura_m = 1.78
clase = "media"
es_soltero = False
if es_soltero:
    marriage = "NO"
else:
    marriage = "YES"

while nombre != aka:
    print("Hola humano, Como te llamas??")
    nombre = input()
    if nombre == aka:
        print("Encatado de conocerte " + nombre)
        print("Name: " + aka)
        print("Age: " + str(edad))
        print("Heigh: " + str(altura_m))
        print("Social estatus: " + clase)
        print("Married : " + marriage)
    elif nombre == "Q" or nombre =="q":
        break
    else:
        print("no compatible")
    














#print("Encatado de conocerte " + nombre)












