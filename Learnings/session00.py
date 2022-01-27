
# Variables
numero = 10 # int
decimal = 10.3 # float
boleano = True # bool
texto = "Esto es un string" # str


# funciones builtin
# https://docs.python.org/3/library/functions.html
# Es un bloque de código. se puede Invocar y Devuelve algo.
# nombre_de_la_funcion()
# -> texto = input()
# funcion_con_parametros(param1, param2)
# -> texto = str(4)
# -> print("texto")

print("texto")

# palabras reservadas
# https://realpython.com/lessons/reserved-keywords/
# El editor las pinta en lila
# indican una sentencia o operación propia del python
# if
# https://www.w3schools.com/python/python_conditions.asp
numero = 4
if numero == 4:
    print("Condicion cierta")
else:
    print("condicion no cierta")

# while
# es un bucle que ejecuta un bloque de codigo mientras su condicion sea verdadera

numero = 0
while numero < 5:
    print(numero)
    numero = numero + 1
    input()

