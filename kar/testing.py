intro_soltero = "En tu aventura te esposaste con alguna belleza? si o no"
soltero = None

while soltero is None:   
    print(intro_soltero)
    is_soltero = input()
    if is_soltero == "si":
        soltero = True
        print("Afortunado aventurero")
        
    
    if is_soltero == "no":
        soltero = False
        print("Mejor solo que mal acompañado")
        
    
    else:
        print("Contesta unicamente con si o no")

def dummy(name:str, num:int)->int:
    print("hola mundo")
    print(name)
    print(num)
    print(num * 3)
    print("---------------------------------------------------------------")
    return num * 3
dummy("paper", 20)
resulatdo = dummy(15, 12)
print(resulatdo)