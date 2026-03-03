import string

valido = False

while not valido:
    especiales = ".-@ñ" 
    
    correoValido = False
    arroba = False
    punto = False

    while not correoValido:
     
     correo = input("ingrese correo: ")
     
     posArroba = -1
     posPunto = -1
     for i, caracter in enumerate(correo):
       if caracter == "@":
           arroba = True
           posArroba = i
       elif caracter == ".":
           punto = True
           posPunto = i

     if not arroba:
      print("El correo ha de tener un arroba")
     elif not punto:
      print("ha de tener un punto")
     else:
      print("Correo valido")
    
    correoValido == True

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
