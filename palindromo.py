texto= input(" Ingrese una palabra palindroma: ")
"""
if texto == texto[::-1]:
    print("\n palindroma")
else: print("\n huh")"""

inverso = ""
for i in texto:
    inverso = i + inverso
    print(inverso)

if texto == inverso:
    print("es palindromo")
else:
    print("no es")