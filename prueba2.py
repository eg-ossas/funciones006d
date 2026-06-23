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
        "noches": int(noches),
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

def confirmar_reserva(lista_a):
    for i in lista_a:
        if i["noches"] >= 2:
            i["confirmacion"] = True
        else:
            i["confirmacion"] = False

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
        posicion = buscar_reserva(nom, datos_habitaciones)
        if posicion != -1:
            huesped = datos_habitaciones[posicion]
            print(f"Habitación reservada: {posicion}")
            print(f"Nombre del huesped: {huesped["nombre"]}")
            print(f"Cantidad de noches: {huesped["noches"]}")
            print(f"Reservas Confirmadas: {huesped["confirmacion"]}")
        else:
            print(f"No se ha encontrado ninguna reserva al nombre de: {nom}")
    elif op == 3:
        print("***** Eliminar Reserva *****")
        nom = input("Ingrese el nombre del huesped para eliminar su reserva: ")
        posicion = buscar_reserva(nom, datos_habitaciones)
        if posicion != -1:
            datos_habitaciones.pop(posicion)
            print("Reserva eliminada correctamente")
        else:
            print(f"No se registra ninguna reserva realizada por el huespues: {nom}")
    elif op == 4:
        confirmar_reserva(datos_habitaciones)
        print("Datos actualizados correctamente")
    elif op == 5:
        confirmar_reserva(datos_habitaciones)
        if len(datos_habitaciones) == 0:
            print("No se a realizado ninguna reserva")
        else:
            print("*** Datos de Reserva ***")
            for i in datos_habitaciones:
                print(f"Nombre del huesped: {i["nombre"]}")
                print(f"Numero de habitacion reservada: {i["habitacion"]}")
                print(f"Cantidad de noches: {i["noches"]}")
                confirmada = "RESERVA CONFIRMADA" if i["confirmacion"] else "PENDIENTE"
                print(f"Confirmacion de reserva: {confirmada}")
    elif op == 6:
        print("Gracias por usar el sistema. \nVuelva pronto")