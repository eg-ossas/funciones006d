#Funciones
def convertir_nota(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) +1
    return round(nota, 1)

#Codigo principal
while True:
    try:
        p = int(input("Ingrese el puntaje obtenido: "))
        if p < 0:
            print("El puntaje no puede ser menor a 0")
        else:
            break
    except ValueError:
        print("Debe ingresar un puntaje valido")
while True:
    try:
        pt = int(input("Ingrese el puntaje total de la prueba: "))
        if pt <= 0:
            print("El puntaje total no puede ser menor a 0")
        else:
            break
    except ValueError:
        print("Debe ingresar un puntaje valido")

#llamar a la funcion

calif = convertir_nota(p, pt)
print(f"La nota en escala Chilena es: {calif}")