vueltas = 0
final = 5 

while vueltas != final:
    vueltas = vueltas +1
    if vueltas % 2 == 1:
        print (str(vueltas) + "--> corriendo")
    else:
        print(str(vueltas) + "--> saltando")
    
    
# saltando pares , impares corriendo , 
# ejemplo de output: 
# 1--> corriendo 
# 2--> saltando


vueltas = 0
final = 5 
is_running = True

while vueltas != final:
    vueltas = vueltas +1
    if is_running:
        print (str(vueltas) + "--> corriendo")
    else:
        print(str(vueltas) + "--> saltando")
    is_running = not is_running
    