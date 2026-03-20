# Lista para almacenar los productos
inventario = []

# Función para agregar producto

def agregar_producto():
    print("\n--- Agregar Producto ---")

    nombre = input("Ingrese el nombre del producto: ")

    # Validar precio
    precio_valido = False
    while not precio_valido:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            precio_valido = True
        except ValueError:
            print("Error: Debe ingresar un número válido.")

    # Validar cantidad
    cantidad_valida = False
    while not cantidad_valida:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            cantidad_valida = True
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # Crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto agregado correctamente.")



# Función para mostrar inventario

def mostrar_inventario():
    print("\n--- Inventario ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")



# Función para calcular estadísticas

def calcular_estadisticas():
    print("\n--- Estadísticas ---")

    if len(inventario) == 0:
        print("No hay productos registrados.")
    else:
        valor_total = 0
        total_productos = 0

        for producto in inventario:
            valor_total += producto["precio"] * producto["cantidad"]
            total_productos += producto["cantidad"]

        print("Valor total del inventario:", valor_total)
        print("Cantidad total de productos:", total_productos)



# Menú principal

opcion = ""

while opcion != "4":

    print("\n===== MENÚ INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        calcular_estadisticas()

    elif opcion == "4":
        print("Saliendo del sistema...")

    else:
        print("Error: opción inválida. Intente nuevamente.")


# Comentario final

# Este programa permite gestionar un inventario de productos mediante un menú interactivo.
# Se aplican estructuras condicionales, bucles, listas y diccionarios para almacenar datos,
# validar entradas y calcular estadísticas básicas del inventario.