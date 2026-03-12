


inventario = []

opcion = ""


while opcion != "4":

    # Menú principal
    print("\n===== MENÚ INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

   
    if opcion == "1":

        print("\n--- Agregar Producto ---")

        nombre = input("Ingrese el nombre del producto: ")

      
        precio_valido = False
        while precio_valido == False:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                precio_valido = True
            except ValueError:
                print("Error: Debe ingresar un número válido.")

       
        cantidad_valida = False
        while cantidad_valida == False:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                cantidad_valida = True
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")


        producto = (nombre, precio, cantidad)

        
        inventario.append(producto)

        print("Producto agregado correctamente.")

    
    elif opcion == "2":

        print("\n--- Inventario ---")

      
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
         
            for producto in inventario:
             print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")

    
    elif opcion == "3":

        print("\n--- Estadísticas ---")

        if len(inventario) == 0:
            print("No hay productos registrados.")
        else:

            valor_total = 0
            total_productos = 0

           
            for producto in inventario:
                valor_total = valor_total + (producto["precio"] * producto["cantidad"])
                total_productos = total_productos + producto["cantidad"]

            print("Valor total del inventario:", valor_total)
            print("Cantidad total de productos:", total_productos)

 
    elif opcion == "4":
        print("Saliendo del sistema...")

    
    else:
        print("Error: opción inválida. Intente nuevamente.")