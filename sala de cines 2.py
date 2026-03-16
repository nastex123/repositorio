print("---------------------")
print("Bienvenido")
print("---------------------")

# Letras para las filas
letras = ["A","B","C","D","E","F","G","H"]

# Número de columnas
columnas = 10

# Llenamos la lista con asientos tipo "A1:O"
sillas = []
for letra in letras:
    for numero in range(1, columnas+1):
        sillas.append(letra + str(numero) + ":O")

valido = ""
while valido != "si":
    # Mostrar todos los asientos (10 por fila)
    for i in range(len(sillas)):
        print(sillas[i], end="   ")
        if (i+1) % columnas == 0:
            print()

    # Pedir asiento
    asiento = input("Elige un asiento (ejemplo C5): ").upper()

    # Validar que el asiento exista
    encontrado = False
    for i in range(len(sillas)):
        if sillas[i].startswith(asiento + ":"):
            encontrado = True
            pos = sillas[i].index(":")   # posición del carácter ":"
            estado = sillas[i][pos+1]    # lo que está después del ":"
            if estado == "O":
                sillas[i] = sillas[i][:pos+1] + "X"
                print("Asiento reservado correctamente.")
            else:
                print("Ese asiento ya está ocupado.")
            break

    if not encontrado:
        print("Ese asiento no existe, intenta de nuevo.")

    # Mostrar estado actualizado
    for i in range(len(sillas)):
        print(sillas[i], end="   ")
        if (i+1) % columnas == 0:
            print()

    valido = input("Presiona ENTER para ingresar otro asiento o escribe 'si' para salir: ")
