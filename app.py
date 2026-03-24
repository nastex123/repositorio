from servicios import *
from archivos import *

inventario=[]

def pedir_float(mensaje):
    validar1= False
    while validar1 != True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except: print("Valor invalido")

def pedir_int(mensaje):
    validar2 = False
    while validar2 != True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except: print("Valor invalido")
salir = False

while salir != True:
    print("===MENU===")
    print(" 1. Agregar\n 2. Mostrar\n 3. Buscar\n 4. Actualizar\n 5. Eliminar\n 6. Estadisticas\n 7. Guardar CSV\n 8. Cargar CSV\n 9. Salir")
    print("==========")

    opcion = input("Seleccione: ")
    try:
        if opcion == 1:
            nombre = input("Nombre: ")
            precio = pedir_float("Precio: ")
            cantidad = pedir_int("Cantidad: ")
            agregar_producto(inventario, nombre, precio, cantidad)
        elif opcion == 2:
            mostrar_inventario(inventario)
        elif opcion == 3:
            nombre = input("Nombre: ")
            p= buscar_producto(inventario, nombre)
            print(p if p else "No encontrado")
        elif opcion == 4:
            nombre = input("Nombre: ")
            precio = pedir_float("Nuevo Precio: ")
            cantidad = pedir_int("Nueva Cantidad: ")
            if not actualizar_producto(inventario, nombre, precio, cantidad):
                print("producto no encontrado")
        elif opcion == 5:
            nombre = input("Nombre: ")
            if not eliminar_producto(inventario, nombre):
                print("producto no encontrado")
        elif opcion == 6:
            stats = calcular_estadisticas(inventario)
            if stats:
                print(stats)
            else: print("No hay na")
        elif opcion == 7:
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)
        elif opcion == 8:
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                decision = input("Sobre escribir? S/N").lower()

                if decision == "s":
                  inventario = nuevos
                else:
                    for nuevo in nuevos:
                        existente = buscar_producto(inventario, nuevo["Nombre"])
                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)
        elif opcion == 9:
            print("Te sales de esta verga")
            salir = True
    except Exception as e:
        print("ndeah")