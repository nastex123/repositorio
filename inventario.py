# -------------------------------------------
# Sistema básico de gestión de inventario
# -------------------------------------------

# Lista donde se guardarán los productos
inventario = []

# Variable de control del menú
opcion = ""

# Bucle principal del programa (se ejecuta hasta que el usuario elija salir)
while opcion != "4":

    # Menú principal
    print("\n===== MENÚ INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # -------------------------------------------
    # Opción 1: Agregar producto
    # -------------------------------------------
    if opcion == "1":

        print("\n--- Agregar Producto ---")

        nombre = input("Ingrese el nombre del producto: ")

        # Validación del precio
        precio_valido = False
        while precio_valido == False:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                precio_valido = True
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        # Validación de la cantidad
        cantidad_valida = False
        while cantidad_valida == False:
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

        # Guardar producto en la lista
        inventario.append(producto)

        print("Producto agregado correctamente.")

    # -------------------------------------------
    # Opción 2: Mostrar inventario
    # -------------------------------------------
    elif opcion == "2":

        print("\n--- Inventario ---")

        # Verificar si el inventario está vacío
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            # Recorrer el inventario con for
            for producto in inventario:
                print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

    # -------------------------------------------
    # Opción 3: Calcular estadísticas
    # -------------------------------------------
    elif opcion == "3":

        print("\n--- Estadísticas ---")

        if len(inventario) == 0:
            print("No hay productos registrados.")
        else:

            valor_total = 0
            total_productos = 0

            # Recorrer inventario para calcular estadísticas
            for producto in inventario:
                valor_total = valor_total + (producto["precio"] * producto["cantidad"])
                total_productos = total_productos + producto["cantidad"]

            print("Valor total del inventario:", valor_total)
            print("Cantidad total de productos:", total_productos)

    # -------------------------------------------
    # Opción 4: Salir del programa
    # -------------------------------------------
    elif opcion == "4":
        print("Saliendo del sistema...")

    # -------------------------------------------
    # Opción inválida
    # -------------------------------------------
    else:
        print("Error: opción inválida. Intente nuevamente.")


# -------------------------------------------
# Comentario final
# -------------------------------------------
# Este programa permite gestionar un inventario simple usando listas
# y diccionarios en Python. Se aplican estructuras condicionales
# (if, elif, else) y bucles (while y for) para validar datos,
# registrar múltiples productos y calcular estadísticas básicas
# como el valor total del inventario y la cantidad total de productos.