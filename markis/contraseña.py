#El control de aceso de una puerta en la cual el portero le pedira una contraseña al usuario y si acierta entrara sino..no. Hay tres intentos para acertar la contraseña.
print ("La contraseña por favor..")

#Toda ka lista en mayusculas y al validar el input tiene que sean en mayusculas tambien.
password = ["osopolar", "osopardo", "osonegro", "osoblanco", "osoverde"]
for item in password:
    print(item.upper())

print(password)






contraseña  = input()
intentos = 3
intento_actual = 0

while intento_actual != intentos:
    intento_actual = intento_actual +1
    if contraseña in password:
        print("!Adelante!")
        break
    if intento_actual == intentos:
        print("Fuera y no vuelvas")
    else:
        print("No es correcto")
        input()
    
        

