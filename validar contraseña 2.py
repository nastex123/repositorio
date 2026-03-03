#este codigo esta optimizado para recorrer una sola contraseña, y no varias veces a como la primera version.
valido = False
especiales = ".-@ñ"
while not valido:
    contraseña = input("ingrese contraseña")

    validar_mayuscula = False
    validar_numero = False
    validar_especial = False

    for caracteres in contraseña:
        if caracteres.isupper():
            validar_mayuscula = True
        elif caracteres.isdigit():
            validar_numero = True
        elif caracteres in especiales:
            validar_especial = True

    if len(contraseña) < 8:
     print("La longitud minima es 8")
    elif not validar_mayuscula:
     print("No tiene mayuscula")
    elif not validar_numero:
     print("No tiene numero")
    elif not validar_especial:
     print("no tiene caracter especial")
    else:
     print("todo valido")
     valido = True
