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