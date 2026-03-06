import random

numero_partido =int(input("Ingrese la cantidad de partido"))

PJ = 0
PG = 0
PE = 0
PP = 0
GF = 0
GC = 0
DG = 0

for i in range(1, numero_partido+1):

    resultado = random.choice([0,1,2])

    goles_favor = random.randint(0,5)
    goles_contra = random.randint(0,5)

    PJ += 1 
    GF += goles_favor
    GC += goles_contra

    if resultado == 2:
        PG += 1
    elif resultado == 1:
        PE += 1
    else:
        PP += 1

puntos = PG*3 + PE*1
DG = abs(GF - GC)

print("Detallito melocoton")
print(f" PJ: {PJ}\n PG: {PG}\n PE: {PE}\n PP: {PP}\n GF {GF}\n GC: {GC} \n DG: {DG}\n Puntos: {puntos}")