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
            print("Debe elegir una opcion valida del 1 al 6")
    return opcion

#Funcion para la opcion 1
def agregar_mascota(lista_m):
    #solicitamos los datos
    nombre = input("Ingrese el nombre de su mascota: ")
    correcta = validar_nombre(nombre)
    if not correcta:
        print("El nombre no puede estar en blanco")
        #El return hace que el codigo que este debajo no se ejecute y termine la funcion
        return
    especie = input("Ingrese la especie (perro, gato, ave): ")
    correcta = validar_especie(especie)
    if not correcta:
        print("La especie solo puede ser perro, gato o ave")
        return
    edad = input("Ingrese la edad de la mascota: ")
    correcta = validar_edad(edad)
    if not correcta:
        print("La edad debe ser un numero mayor a cero")
        return
    #agregar los datos al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada":False
    }
    #agrego a la lista
    lista_m.append(mascota)
    print("Mascota agregada correctamente")

#Funciones de validacion
def validar_nombre(name):
    #strip() -> Eliminar todos los espacios en blanco al inicio y al final de un string
    #Retorna true si es valido o false si no
    return name.strip() != ""

def validar_especie(especie):
    especies_validas= ["perro", "gato", "ave"]
    #Retorna True si lo consigue o False si no
    return especie.strip().lower() in especies_validas

def validar_edad(age):
    #el isdigit() se puede utilizar para no realizar el try/except y ver si un string tiene solo digitos
    return age.isdigit() and int(age) > 0


#Codigo Principal
#Declarar lista mascotas
datos_mascotas = []


op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()

    if op == 1:
        agregar_mascota(datos_mascotas)
    elif op == 2:
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema. Vuelva Pronto :D")
