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
    nombre_masc = input("Ingrese el nombre de la mascota: ")
    if " " not in nombre_masc:
        especie = input("Ingrese la especie de su mascota: (Perro, Gato, Ave)\n").lower()
        if especie in ("perro", "gato", "ave"):
            while True:
                try:
                    edad

#Codigo Principal
#Declarar lista mascotas
datos_mascotas = []


op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()
