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

#Opcion 2: Buscar Mascota
def buscar_mascota(lista_m, nombre_m):
    #recorrer y devolver la posicion
    for i in range(len(lista_m)):
        if lista_m[i]["nombre"] == nombre_m:
            return i #retorno la posición 
            """
            lista_m[i]["nombre"] hace que en el primer parametro se ubique en una posicion en la lista
            cuando entre a la casilla con el segundo parametro hace que busque la clave del diccionario
            que esta dentro de la lista
            """
    return -1 #se termino el ciclo por tanto no se encontró

def actualizar_vacunas(lista_m):
    #recorre la lista completa
    for m in lista_m:
        #preguntamos por la edad para validar
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False

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
        print("**** Buscar Mascota *****")
        nom = input("Ingrese el nombre de la mascota a buscar: ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            #guardar en una variable el diccionario de la mascota en la posicion de la lista
            m = datos_mascotas[posicion]
            print(f"Mascota encontrada en la posición: {posicion}")
            print(f"Nombre mascota: {m["nombre"]}")
            print(f"Especie mascota: {m["especie"]}")
            print(f"Edad mascota: {m["edad"]}")
            print(f"Vacunada: {m["vacunada"]}")
        else:
            print(f"No se encontro la mascota con el nombre: {nom}")
    elif op == 3:
        print("**** Eliminar Mascota *****")
        nom = input("Ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            #procedemos a eliminarla
            datos_mascotas.pop(posicion)
            print("Mascota eliminada correctamente")
        else:
            print(f"La mascota '{nom}' no se encuentra registrada")
    elif op == 4:
        actualizar_vacunas(datos_mascotas)
        print("Estado de vacunas actualizadas")
    elif op == 5:
        #actualizar el estado de las vacunas
        actualizar_vacunas(datos_mascotas)
        #mostrar sus datos
        #si la lista esta vacia
        if len(datos_mascotas) == 0:
            print("No hay mascotas registradas")
        else:
            print("== Lista de Mascotas ==")
            for m in datos_mascotas:
                print(f"Nombre mascota: {m["nombre"]}")
                print(f"Especie mascota: {m["especie"]}")
                print(f"Edad mascota: {m["edad"]}")
                #variable para cambiar el valor de vacunada
                estado = "AL DÍA" if m["vacunada"] else "PENDIENTE"
                print(f"Estado de vacuna: {estado}")
                print("===================================")
    elif op == 6:
        print("Gracias por usar el sistema. Vuelva Pronto :D")
