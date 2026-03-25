import csv

# Guardar inventario en CSV
def guardar_csv(inventario, ruta, incluir_header=True):
    # Verifica si hay datos
    if not inventario:
        print("No hay datos para guardar.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            # Escribe encabezado
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # Escribe productos
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Guardado en: {ruta}")

    except PermissionError:
        print("Sin permisos para guardar.")
    except Exception as e:
        print("Error:", e)


# Cargar inventario desde CSV
def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            encabezado = next(reader, None)

            # Verifica encabezado
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado incorrecto.")
                return []

            for fila in reader:
                try:
                    # Verifica formato
                    if len(fila) != 3:
                        raise ValueError

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Verifica valores negativos
                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"{len(inventario)} productos cargados.")
        if errores > 0:
            print(f"{errores} filas inválidas.")

        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de lectura.")
    except Exception as e:
        print("Error:", e)

    return []