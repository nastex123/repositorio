print("---------------------")
print("Bienvenido")
print("---------------------")

#opcion_silla=int(input("Elige un asiento libre: "))

sillas = [
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"], 
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
]

valido = ""
while valido != "si" :
 for asiento in sillas:
    print("   ".join(asiento) )
 
 
 fila= int(input("ELige la fila del 0 al 7: "))
 if fila < 0 or fila > 7:
    print("Elige un valor dentro del rango")
    fila= int(input("ELige la fila del 0 al 7: "))

 else: print("Fila registrada")

 columna = int(input("Elige la columna del 0 al 9: "))
 if columna < 0 & columna > 9:
    print("Elige un valor dentro del rango")
    columna = int(input("Elige la columna del 0 al 9: "))

 else: print("Columna registrada")

 if sillas [fila][columna] == "O":
  sillas [fila][columna] = "x"
 elif sillas [fila][columna] == "x":
    print("Asiento reservado")
    continue
 
 for asiento in sillas:
    print("   ".join(asiento) )

 valido=input("Presiona ENTER para ingresar otro asiento O Escribe si para salir: ")
 


