
products = ["tomate", "patata", "axe ligoteo"]


def add_product_func():
        print("Que producto deseas añadir?")
        add_product = input()
        products.append(add_product)
        how_many = len(products)
        print(str(add_product) + " se agregó a la lista de la compra. Hay " + str(how_many) + " productos\n")
        return products

add_product_func()      


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
    elif choose == 2:
        add_product_func = input()
        products = add_product_func(products)

    elif choose == 3:
        print("Estos son los productos que hay en la lista. Cuál quieres modificar?")
        for (i, item) in enumerate(products):
            print(i,item)
        select_product = input()
        select_product = int(select_product)


        print("Cual es su nuevo valor?")
        modify_product = input()
        old_product = products[select_product]
        products[select_product] = modify_product
        print(str(old_product) + " se ha modificado por " + str(modify_product) + "\n" )

    elif choose == 4:
        for (i, item) in enumerate(products):
            print(i,item)
        print ("Escriba el articulo que desea quitar?")
        try:
            borrar = input()
            products.remove(borrar)
            how_many = len(products)
            print(str(borrar) +  " ha sido eliminado de la lista. Quedan " + str(how_many)  + " productos\n")
        except ValueError:
            print("El producte `" + str(borrar) + "´ no esta en la lista")
        
        
    
    elif choose == 0:
        print("Estas seguro que deseas salir? si o no")
        want_to_exit = input()
        
        if want_to_exit == "si":
            break
    
    else:
        print("Opcion invalida")

        
            
        
        
        

    