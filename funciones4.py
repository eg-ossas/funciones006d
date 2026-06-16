#funciones
def precio_total(subtotal, propina):
    total = propina + subtotal
    return total

def calcular_propina(subtotal, porcentaje):
    propina =subtotal * (porcentaje /100)
    return propina

def mostrar_resultados(total, propina, subtotal):
    print("=" *35)
    print(f"Subtotal: ${subtotal}")
    print(f"Monto de propina: ${propina}")
    print(f"Total a pagar: ${total}")

def solicitar_subtotal():
    while True:
        try:
            st = int(input("Ingrese el subtotal: "))
            if st < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Debe ser un numero entero mayor a 0")
    return st

def solicitar_porcentaje():
    print("=" *15)
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. Ninguna")
    while True:
        try:
            opcion = int(input("Que porcentaje de propina desea agregar?: "))
            if opcion == 1:
                porcentaje = 10
            elif opcion == 2:
                porcentaje = 15
            elif opcion == 3:
                porcentaje = 20
            elif opcion == 4:
                porcentaje = 0
            else:
                raise ValueError
            break
        except ValueError:
            print("Debe ser una opcion entre el 1-4")
    return porcentaje
    
#codigo principal

subt = solicitar_subtotal()
porc = solicitar_porcentaje()
prop = calcular_propina(subt, porc)
total = precio_total(subt, prop)
mostrar_resultados(total, prop, subt)
