#Funciones
def mostrar_menu():
    print("=" *35)
    print("MENÚ PRINCIPAL")
    print("=" *35)
    print("1. Agregar Libro")
    print("2. Buscar Libro")
    print("3. Eliminar Libro")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Libros")
    print("6. Salir")

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opcion a utilizar: "))
            if opcion > 0 and opcion <= 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("Debe ser una opcion entre el 1 al 6")
    return opcion

#Opcion 1
def agregar_libro(lista_l):
    nom = input("Ingrese el titulo del libro: ")
    validacion = validar_nombre(nom)
    if not validacion:
        print("El nombre no puede estar en blanco")
    cop = input("Ingrese la cantidad de copias disponibles: ")
    validacion = validar_copias(cop)
    if not validacion:
        print("Las copias deben ser un numero mayor o igual a 0")
    pres = input("Ingrese el periodo de prestamo: ")
    validacion = validar_prestamo(pres)
    if not validacion:
        print("El periodo de prestamo debe ser un numero mayor a 0")

    coleccion = {
        "nombre":nom,
        "copias": int(cop),
        "prestamo": int(pres),
        "disponible": False
    }
    lista_l.append(coleccion)

#Validaciones Opcion 1
def validar_nombre(name):
    return name.strip().lower() != ""

def validar_copias(copy):
    return copy.isdigit() and int(copy) >= 0

def validar_prestamo(prestamo):
    return prestamo.isdigit() and int(prestamo) > 0

#Opcion 2 y 3
def buscar_libro(lista_l, nombre):
    for i in range(len(lista_l)):
        if lista_l[i]["nombre"]:
            return i
    return -1

#Opcion 4
def actualizar_dispo(lista_l):
    for i in lista_l:
        if i["copias"] > 1:
            i["disponible"] = True
        else:
            i["disponible"] = False

#Codigo Principal

datos_libros=[]

op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()
    if op == 1:
        agregar_libro(datos_libros)
    elif op == 2:
        print("**** Buscar Libro ****")
        nom = input("Ingrese el titulo del libro a buscar: ")
        posicion = buscar_libro(datos_libros, nom)
        if posicion != -1:
            print(f"El libro {nom}")
            print(f"Hay {datos_libros[posicion]["copias"]} copias del libro")
            print(f"Se encuentra en prestamo durante {datos_libros[posicion]["prestamo"]} dias")
            estado = "DISPONIBLE" if datos_libros[posicion]["disponible"] else "NO DISPONIBLE"
            print(f"Se encuentra {estado}")
            print("=" *35)
        else:
            print(f"El libro por el nombre {nom} no se pudo encontrar")
    elif op == 3:
        print("**** Eliminar Libro ****")
        nom = input("Ingrese el titulo del libro a eliminar: ")
        posicion = buscar_libro(datos_libros, nom)
        if posicion != -1:
            datos_libros.pop()
        else:
            print(f"Libro con nombre {nom} no encontrado")
    elif op == 4:
        actualizar_dispo(datos_libros)
        print("Disponibilidad de libros actualizada")
    elif op == 5:
        actualizar_dispo(datos_libros)
        print("=== LISTA DE LIBROS ===")
        for i in datos_libros:
            print(f"Título: {i["nombre"]}")
            print(f"Copias: {i["copias"]}")
            print(f"Préstamo: {i["prestamo"]}")
            estado = "DISPONIBLE" if i["disponible"] else "SIN COPIAS"
            print(f"Estado: {estado}")
            print("=" *35)
    elif op == 6:
        print("Gracias por usar el sistema.\nVuelva Pronto")