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

    goles_favor = random.randint(0,5)
    goles_contra = random.randint(0,5)

    PJ += 1 
    GF += goles_favor
    GC += goles_contra

    if goles_favor < goles_contra:
        PG += 1
    elif goles_favor == goles_contra:
        PE += 1
    else:
        PP += 1

puntos = PG*3 + PE
DG = GF - GC

print("Detallito melocoton")
print(f" PJ: {PJ}\n PG: {PG}\n PE: {PE}\n PP: {PP}\n GF {GF}\n GC: {GC} \n DG: {DG}\n Puntos: {puntos}")