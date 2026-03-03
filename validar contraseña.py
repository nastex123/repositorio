valido = False
while not valido:
 Contraseña = input("Digite una contraseña valida: ")

 validar_longitud= 8
 if len(Contraseña) >= validar_longitud:
    print("Longitud minima aceptada")
 else: 
    print("Longitud minima es de 8, ingrese una nueva.")
    continue
    
 validar_mayuscula= any(c.isupper()for c in Contraseña)
 if validar_mayuscula == False:
   print("no tiene mayuscula")
   continue  
 else: print("tiene mayuscula")  
 
 validar_numero= any(c.isdigit()for c in Contraseña)
 if validar_numero == False:
   print("no tiene numero")
   continue 
 else: print("tiene numero")
    

 caracteres = "ñ@/-"
 validar_caracter_especial= any(c in caracteres for c in Contraseña)
 if validar_caracter_especial == False:
   print("no tiene caracter especial")
   continue
 else: print("tiene caracter especial")


