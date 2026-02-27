#en este ambito se ha de mejorar la calculadora, indicando al usuario su promedio de notas (Rango entre 1 a 5), posteriormente le indica al usuario si paso o no su nota, indicando su nota minima para pasar.

notas=[]
while True:
    print("#########################")
    nota=float(input("Digite a nota de alumno (digite -1 para terminar): "))
    print("#########################")
    if nota== -1:
        break
    notas.append(nota)
    promedio=sum(notas)/len(notas)

minima= float(input("Digite la nota minima para pasar: "))

print(f"El promedio de las notas es: {promedio:.2f}")

if promedio >= minima:
    print("¡Felicidades! Has pasado.")
else:    print("Lo siento, no has pasado.")

#nota