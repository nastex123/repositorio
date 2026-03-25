from servicios import *
from archivos import *

inventario = []


# Pedir número decimal válido
def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except:
            print("Valor inválido. Intente nuevamente.")


# Pedir número entero válido
def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except:
            print("Valor inválido. Intente nuevamente.")


salir = False

while not salir:
    print("\n=== MENÚ ===")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    print("============")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = pedir_float("Precio: ")
            cantidad = pedir_int("Cantidad: ")
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre: ")
            p = buscar_producto(inventario, nombre)
            print(p if p else "Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre: ")
            precio = pedir_float("Nuevo precio: ")
            cantidad = pedir_int("Nueva cantidad: ")

            if not actualizar_producto(inventario, nombre, precio, cantidad):
                print("Producto no encontrado.")

        elif opcion == "5":
            nombre = input("Nombre: ")
            if not eliminar_producto(inventario, nombre):
                print("Producto no encontrado.")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print("\n--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total: {stats['valor_total']}")
                print(f"Producto más caro: {stats['producto_mas_caro']}")
                print(f"Mayor stock: {stats['producto_mayor_stock']}")
            else:
                print("No hay datos en el inventario.")

        elif opcion == "7":
            ruta = input("Ruta del archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta del archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                decision = input("¿Sobrescribir inventario actual? (S/N): ").lower()

                if decision == "s":
                    inventario = nuevos
                    print("Inventario reemplazado.")
                else:
                    # Fusión
                    for nuevo in nuevos:
                        existente = buscar_producto(inventario, nuevo["nombre"])

                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)

                    print("Inventario fusionado correctamente.")

        elif opcion == "9":
            print("Saliendo del sistema...")
            salir = True

        else:
            print("Opción inválida. Intente nuevamente.")

    except Exception as e:
        print("Error en la operación:", e)