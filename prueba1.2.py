#Funciones
def mostrar_menu():
    print("=" *35)
    print("MENÚ PRINCIPAL")
    print("=" *35)
    print("1. Agregar una Mascota")
    print("2. Buscar Mascota")
    print("3. Eliminar Mascota")
    print("4. Marcar como Vacunada")
    print("5. Mostrar Mascotas")
    print("6. Salir")
    print("=" *35)

def solicitar_opciones():
    while True:
        try:
            opcion = int(input("Ingrese la opción a elegir: "))
            if opcion <= 0 or opcion > 6:
                raise ValueError
            else:
                break
        except ValueError:
            print("Debe elegir una opcion valida")
    return opcion

def opcion_1(datos_mascotas):
    mascota = {}
    mascota["nombre_masc"] = input("Ingrese el nombre de la mascota: ")
    if " " not in mascota["nombre_masc"]:
        mascota["especie"] = input("Ingrese la especie de su mascota: (Perro, Gato, Ave)\n").lower()
        if mascota["especie"] in ("perro", "gato", "ave"):
            while True:
                try:
                    mascota["edad"] = int(input("Ingrese la edad de su mascota: "))
                    if mascota["edad"] <= 0:
                        print("Su mascota debe tener al menos 1 año de edad")
                    else:
                        break
                except ValueError:
                    print("Debe introducir una edad valida")
    datos_mascotas.append(mascota)
    return datos_mascotas

def opcion_2(datos_mascotas, mascotas["nombre_masc"]):
    for i in datos_mascotas():


def opcion_3():

def opcion_4():

def opcion_5():

#Codigo Principal
#Declarar lista mascotas
datos_mascotas = []


op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()
    lista = opcion_1(datos_mascotas)