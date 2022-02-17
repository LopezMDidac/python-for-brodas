#Control de acceso de una puerta en la que el portero le va a pedir al usiario por la contraseña, si acierta le abrira la puerta si no no se la abre. 
# Tiene 3 intentos.
#Listas: Son objetos iterables(recorrer), mutables(cambiar), ordenados(elemento 1 , 2 , 3).
#list.count("cabraloca")
#contraseñas y input todo en mayusculas




passwords = ["cabraloca","MarkisPyton","dartlalia"]

for item in passwords:
    print(item.upper())

print(passwords)




passwordtwo = "MarkisPyton"
max_intentos = 3 
trys = 0
portero = "Bienvenido aventurero, necesito la contraseña para dejarte pasar si fallas" +  str(max_intentos)  + "tendras" 
door = "Se abrio la puerta  pero el guardia te mira con mala cara"



print(portero)

while trys != max_intentos: 
    respuesta = str(input())
    if respuesta in passwords:
       print(door)
       break
    else:
        trys = trys + 1
         
