#Funciones
def mostrar_menu ():
    print("=" *35)
    print("MENÚ PRINCIPAL")
    print("=" *35)
    print("|| 1. Agregar Reserva    ||")
    print("|| 2. Buscar Reserva     ||")
    print("|| 3. Eliminar Reserva   ||")
    print("|| 4. Confirmar Reservas ||")
    print("|| 5. Mostrar Reservas   ||")
    print("|| 6. Salir              ||")

def solicitar_opciones():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Debe elegir una opción válida del 1-6")
    return opcion

#Opcion 1
def agregar_reserva(lista_habitaciones):
    nombre= input("Ingrese el nombre del huesped: ")
    correcta = validacion_nombre(nombre)
    if not correcta:
        print("El nombre no puede estar en blanco")
        return
    habitacion = input("Ingrese la habitacion a reservar: ")
    correcta = validacion_habitacion(habitacion)
    if not correcta:
        print("Solo se puede reservar entre 1 a 200 habitaciones")
        return
    noches = input("Ingrese la cantidad de noches: ")
    correcta = validacion_noches(noches)
    if not correcta:
        print("Debe al menos reservar 1 noche")
        return
    habitaciones = {
        "nombre": nombre.strip(),
        "habitacion": habitacion,
        "noches": noches,
        "confirmacion": False
    }
    datos_habitaciones.append(habitaciones)

#Validaciones Opcion 1

def validacion_nombre(nombre):
    return nombre.strip().title() != "" #Se eliminan los espacios en blanco al inicio y final, si no es solo espacios no retorna nada

def validacion_habitacion(habitacion):
    return habitacion.isdigit() and int(habitacion) > 0 and int(habitacion) < 200

def validacion_noches(noches):
    return noches.isdigit() and int(noches) > 0

#Opcion 2
def buscar_reserva(lista_a, nombre):
    for i in range(len(lista_a)):
        if lista_a[i]["nombre"]:
            return i
    return -1


#Codigo principal
datos_habitaciones = []

op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()
    if op == 1:
        agregar_reserva(datos_habitaciones)
    elif op == 2:
        print("***** Buscar Reserva *****")
        nom = input("Ingrese el nombre del huesped a buscar: ")
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema. \nVuelva pronto")