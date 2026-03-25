# Funciones del inventario

def agregar_producto(inventario, nombre, precio, cantidad):
    # Agrega producto o actualiza si ya existe
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] += cantidad
            producto["precio"] = precio
            print("Producto actualizado.")
            return

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.")


def mostrar_inventario(inventario):
    # Muestra todos los productos
    if not inventario:
        print("Inventario vacío.")
        return

    for p in inventario:
        print(f"{p['nombre']} | {p['precio']} | {p['cantidad']}")


def buscar_producto(inventario, nombre):
    # Busca producto por nombre
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    # Cambia precio y/o cantidad
    producto = buscar_producto(inventario, nombre)

    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        print("Producto actualizado.")
        return True

    return False


def eliminar_producto(inventario, nombre):
    # Elimina producto
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print("Producto eliminado.")
            return True

    return False


def calcular_estadisticas(inventario):
    # Calcula datos del inventario
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }