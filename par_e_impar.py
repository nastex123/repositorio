def par_e_impar(numero):
    if numero % 2 == 0:
        return "el numero es par"
    else:
        return "el numero es impar"
def main():
    num = int(input("Ingrese un numero: "))
    resultado = par_e_impar(num)
    print(f"el resultado es: {resultado}")
    
main()