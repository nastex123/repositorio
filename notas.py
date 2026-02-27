notas=[]
while True:
    nota=float(input("Digite a nota de alumno: "))
    if nota== -1:
        break
    notas.append(nota)
    promedio=sum(notas)/len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")