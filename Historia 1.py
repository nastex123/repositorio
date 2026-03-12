# Solicitar nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Validar precio con un ciclo controlado
precio_valido = False
while not precio_valido:
    entrada = input("Ingrese el precio del producto: ")
    if entrada.replace('.', '', 1).isdigit():  # permite números con punto decimal
        precio = float(entrada)
        precio_valido = True
    else:
        print("Error: el precio debe ser un número válido.")

# Validar cantidad con un ciclo controlado
cantidad_valida = False
while not cantidad_valida:
    entrada = input("Ingrese la cantidad del producto: ")
    if entrada.isdigit():  # solo números enteros positivos
        cantidad = int(entrada)
        cantidad_valida = True
    else:
        print("Error: la cantidad debe ser un número entero válido.")

# Calcular costo total
costo_total = precio * cantidad

# Mostrar resultados en consola
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# Este programa permite registrar un producto con su nombre, precio y cantidad,
# valida los datos ingresados mediante ciclos controlados y calcula el costo total.