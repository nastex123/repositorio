# aqui se trabajara la calculadora completa

def menu():
    print("#########################")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("#########################")

def leer_opcion():
        while True:
            opcion = input("Seleccione una opción (1-5): ")
            if opcion in ['1', '2', '3', '4', '5']:
                return opcion
            print("Opción no válida. Por favor, intente de nuevo.")

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b        
def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
        return a / b
            #main - menu que se plazma

def main():
    while True:
        menu()
        opcion = leer_opcion()

        if opcion == "5":
            print("Saliendo")
            break
        # Leer los números
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))

        try:
            if opcion == "1":
                resultado = suma(a, b)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == "2":
                resultado = resta(a, b)
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == "3":
                resultado = multiplicacion(a, b)
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == "4":
                resultado = division(a, b)
                if resultado is not None:
                    print(f"El resultado de la división es: {resultado}")
        except Exception as e:
            print(f"Error: {e}")

main() 
