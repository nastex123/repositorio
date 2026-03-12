vuelos = {
    "AV101": ("Bogota", 5, 300),
    "AV202": ("Medellin", 3, 200),
    "AV303": ("Cartagena", 4, 250),
    "AV404": ("Cali", 2, 220)
}
reservas = []



salir = ""

while salir != "salir":
 print("Vuelos disponibles")

 for codigo in vuelos:
    destino, asientos, precio = vuelos[codigo]
    print(codigo, "-", destino, "- Asientos: ",asientos, "- precio: ",precio  )

 nombre = input("Nombre del pasajero: ")

 codigo = input("Codigo del vuelo: ")

 cantidad = int(input("Cantidad de asientos"))

 if codigo in vuelos:
     destino, asientos, precio = vuelos[codigo]
     if cantidad <= asientos:
        reservas.append((nombre, codigo, cantidad))
        vuelos[codigo] = (destino, asientos - cantidad, precio)
        print ("Reserva realizada")
     else: print("No hay cupo")
 else: print("El vuelo no existe")
 salir = input("Escribe salir para terminar o Enter para continuar: ")

print("reservas realizadas")
for reserva in reservas:
  print(reserva)

total = 0

for nombre, codigo, cantidad in reservas:
  destino, asientos, precio= vuelos[codigo]
  total += precio * cantidad
print("Dinero recaudado: ", total)

conteo = {}

for nombre, codigo, cantidad in reservas:
  if codigo in conteo:
    conteo[codigo] += cantidad
  else: conteo[codigo] = cantidad

mayor = 0
vuelo_mayor = ""

for codigo in conteo:
  if conteo[codigo] > mayor:
    mayor = conteo[codigo]
    vuelo_mayor = codigo

print("Vuelo con mas reservas: ", vuelo_mayor)