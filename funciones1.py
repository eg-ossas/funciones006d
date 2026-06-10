#Funciones
def datos_producto(nombre, precio, stock):
    print("=" *25)
    print(f"||Nombre del producto: {nombre} ||")
    print(f"||Precio del producto: {precio} ||")
    print(f"||Stock del producto: {stock} ||")
    print("=" *25)


#Código Principal
nombre = input("Ingrese el nombre del producto: \n")
while True:
    try:
        precio = int(input("Ingrese el precio del producto: \n"))
        if precio <= 0:
            print("¡ERROR! Debe Ingresar un precio valido")
            raise ValueError
        else:
            break
    except ValueError:
        print("Debe escribir números")

while True:
    try:
        stock = int(input("Ingrese el stock del producto: \n"))
        if stock < 0:
            print("¡ERROR! Debe Ingresar un stock valido")
        else: 
            break
    except ValueError:
        print("Debe escibir números")

#Llamar a la funcion
datos_producto(nombre, precio, stock) #Se deben enviar los parametros en el orden exacto que los declare al crear la funcion
