
products = ["tomate", "patata", "axe ligoteo"]



def intro():
    print("Bienvenid@ a la lista de la compra. Que quieres hacer:")
    print("""
     0. Salir
     1. Ver lista de la compra
     2. Agregar producto a la lista
     3. Modificar producto de la lista
     4. Quitar producto de la lista""")
    choose = input()
    #except ValueError (este cambio de tipo es inseguro, un value error evitaria)
    choose = int(choose)
    return choose


def show_list():
        for (i, item) in enumerate(products):
                print(i,item)

def add_product_func():
        print("Que producto deseas añadir?")
        add_product = input()
        products.append(add_product)
        how_many = len(products)
        print(str(add_product) + " se agregó a la lista de la compra. Hay " + str(how_many) + " productos\n")
        return products

def modify_products():
    print("Estos son los productos que hay en la lista. Cuál quieres modificar?")
    show_list()
    select_product = input()
    select_product = int(select_product)

    print("Cual es su nuevo valor?")
    modify_product = input()
    old_product = products[select_product]
    products[select_product] = modify_product
    print(str(old_product) + " se ha modificado por " + str(modify_product) + "\n" )

def remove_product():
    show_list()
    print ("Escriba el articulo que desea quitar?")
    try:
            borrar = input()
            products.remove(borrar)
            how_many = len(products)
            print(str(borrar) +  " ha sido eliminado de la lista. Quedan " + str(how_many)  + " productos\n")
    except ValueError:
            print("El producte `" + str(borrar) + "´ no esta en la lista")

def exit_list():
    while True:
        print("Estas seguro que deseas salir? si o no")
        want_to_exit = input()
    
        if want_to_exit == "si":
            return True

        if want_to_exit == "no":
            return False

while True:
    
    choose = intro()
    if choose == 1:
        show_list()
    elif choose == 2:
        add_product_func()
    elif choose == 3:
        modify_products()
    elif choose == 4:
        remove_product()
    elif choose == 0:
        the_choose = exit_list()
        if the_choose == True:
            break
        if the_choose == False:
            continue
    else: 
        print("Opcion invalida")
    



