def rango(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
def main():
    edad = int(input("Ingrese su edad: "))
    print(f"Usted es: {rango(edad)}")
main()