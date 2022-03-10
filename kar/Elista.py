



#products = [ ]
products = ["tomate", "patata", "axe ligoteo"]
while True:
   
    print("Bienvenid@ a la lista de la compra. Que quieres hacer:")
    print("""
     0. Salir
     1. Ver lista de la compra
     2. Agregar producto a la lista
     3. Modificar producto de la lista
     4. Quitar producto de la lista""")
    choose = input()
    choose = int(choose)
    if choose == 1:
        for (i, item) in enumerate(products):
            print(i,item)
    if choose == 2:
        add_product = input()
        products.append(add_product)
        
    if choose == 3:
        print("Estos son los productos que hay en la lista. Cuál quieres modificar?")
        for (i, item) in enumerate(products):
            print(i,item)
        select_product = input()
        select_product = int(select_product)
         
        print("Cual es su nuevo valor?")
        modify_product = input()
        products[select_product] = modify_product

    
    if choose == 0:
        break

    





     