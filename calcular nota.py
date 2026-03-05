n_cantidad= int(input("ingrese la cantidad de estudiantes: "))
concatenacion = ""
estado = ""
contador_ganador= 0
contador_perdedor= 0
suma_promedio_general= 0

for c in range(n_cantidad):
    nombre=input("ingresar nombre: ")
    
    nota1= float(input("Primera nota: "))
    while nota1 < 1 or nota1 > 5:
        print("valor invalido")
        nota1= float(input("Primera nota: "))
    
    nota2= float(input("segunda nota: "))
    while nota2 < 1 or nota2 > 5:
        print("valor invalido")
        nota2= float(input("segunda nota: "))
    
    nota3= float(input("tercera nota: "))
    while nota3 < 1 or nota3 > 5:
        print("valor invalido")
        nota3= float(input("tercera nota: "))

    promedio=(nota1+nota2+nota3)/3

    suma_promedio_general += promedio

    if promedio >= 3:
        estado = "aprobado"
        contador_ganador = +1
    elif promedio < 3: 
        estado = "reprobado"
        contador_perdedor= +1

    concatenacion += nombre + " - promedio: " + str(round(promedio,2)) + " - estado: " + estado + "\n"

promedio_general=suma_promedio_general/n_cantidad

print("\nNombre estudiante y Promedio")
print(concatenacion)
print(f"cantidad de estudaintes aprobados: {contador_ganador}")
print(f"cantidad de estudiantes reprobados: {contador_perdedor}")
print(f"el promedio general es: {round(promedio_general,2)}")

    