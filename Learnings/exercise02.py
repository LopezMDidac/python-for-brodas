# Lista de la compra.
# 
# Este ejercicio consiste en la digitalización de una lista de la compra totalmente funcional.
# Esta lista de la compra será una aplicación de consola basada en menus.
#
# En caso que el usuario de una opcion no valida, se debera informar que la opción no es valida
# y volver a mostrar actual.
# 
# Ejemplo Menu principal.
#
# > Bienvenid@ a la lista de la compra. Que quieres hacer:
# > 0. Salir
# > 1. Ver lista de la compra
# > 2. Agregar producto a la lista
# > 3. Modificar producto de la lista
# > 4. Quitar producto de la lista
# <
#
# El usuario podrá introducir el numero correspondiente a la acción que quiera realizar.
#
# Funcionalidades:
## 0. Salir
### Si el usuario elige salir la aplicación debe preguntar si esta seguro que desea salir. 
### En caso que diga que si, debe cerrarse
### Ejemplo:
### > Esta seguro que desea salir?
### > 0. Si
### > 1. No
### <
##
## 1. Ver lista de la compra
### Si el usuario selecciona esta opcion se deben mostrar todos los productos que haya introducido
### o modificado previamente seguido del menu principal
###
### Ejemplo:
### < 1
### > Tomates
### > Patatas
### > Pañales
### > 
### > ...Bienvenid@ a la ...
### <
##
## 2. Agregar producto a la lista
### Cuando el usuario seleccione esta opcion, la aplicación le pedirá el producto a añadir
### Despues de que el usuario introduzca un producto le notificara que ha sido agregado y el 
### numero de productos que hay en la lista
### Despues del mensaje se vuelve a mostrar el menu principal
###
### Ejemplo:
### < 2
### > Que producto deseas añadir?
### < Sangre de unicornio
### > 'Sangre de unicornio' se agregó a la lista de la compra. hay 4 productos.
### > Bienvenid@ a la ...
### > ...
### <
##
## 3. Modificar producto de la lista
### Cuando El usuario utiliza esta opción. Ve todos los productos que hay en la lista,
### elige cual quiere modificar, y introduce un valor en su lugar.
### Despues de la operación de modificado se muestra el menu principal
### 
### Ejemplo:
### < 3
### > Estos son los productos que hay en la lista. Cuál quieres modificar?
### > 0. Tomates
### > 1. Patatas
### > 2. Pañales
### > 3. Sangre de unicornio
### < 1
### > Cual es su nuevo valor?
### < Mana del bueno
### > 'Patatas' Se ha modificado por 'Mana del bueno'
### > Bienvenid@ a la ...
### > ...
### <
##
## 4. Quitar producto de la lista
### Cuando El usuario utiliza esta opción. Ve todos los productos que hay en la lista,
### elige cual quiere eliminar.
### Despues de la operación de modificado se muestra el menu principal
### 
### Ejemplo:
### < 4
### > Estos son los productos que hay en la lista. Cuál quieres eliminar?
### > 0. Tomates
### > 1. Mana del bueno
### > 2. Pañales
### > 3. Sangre de unicornio
### < 0
### > 'Tomates'ha sido eliminado de la lista. Quedan 3 productos.
### > Bienvenid@ a la ...
### > ...
### <


print("unica linea")
print()
print("prints separados")
print("linea uno")
print("linea dos")
print ("linea tres")
print()
print("triple comilla")
print("""linea uno
linea dos
    linea tres
""")
print()
print("special char ")
print("linea uno \nlinea dos\nlinea tres")
print()
print("playing with special chars")
print("text with \" quote")
print("mi headline\n\tsubhedline1\n\tsubheadline2")
print("string with bars \\")