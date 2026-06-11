#funciones
def mostrar_encabezado():
    print("=" *33)
    print("|| Sistema de Registro Escolar ||")
    print("=" *33)

def datos_estudiantes():
    estudiante = {}
    estudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            estudiante["semestre"] = int(input("Ingrese el semestre que cursa: "))
            if estudiante["semestre"] < 1 or estudiante["semestre"] > 5:
                print("Debe ingresar un semestre del 1 al 5")
            else:
                break
        except ValueError:
            print("Debe ingresar números")
    estudiante["carrera"] = input("Ingrese la carrera que estudia: ")
    estudiante["rut"] = input("Ingrese su rut: ")
    return estudiante

def mostrar_ficha(estudiante):
    print(F"Nombre estudiante: {estudiante["nombre"]}")
    print(F"Rut estudiante: {estudiante["rut"]}")
    print(F"Carrera estudiante: {estudiante["carrera"]}")
    print(F"Semestre estudiante: {estudiante["semestre"]}")

#codigo principal
datos = datos_estudiantes()
mostrar_encabezado()
mostrar_ficha(datos)
