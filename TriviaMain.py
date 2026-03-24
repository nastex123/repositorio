from funciones import cargar_preguntas
import random

# 1. Cargar la lista completa desde el JSON
todas_las_preguntas = cargar_preguntas()

# Verificación de seguridad
if len(todas_las_preguntas) < 5:
    print("Error: Necesitas al menos 5 preguntas en el JSON.")
    exit()

# 2. Selección única: elige 5 preguntas al azar SIN repetir
preguntas_juego = random.sample(todas_las_preguntas, 5)

nombre = ""
while nombre.strip() == "":
    nombre = input("Ingresa tu nombre, ome: ").strip()

puntaje = 0
correctas = 0

# 3. Recorrer una a una
for i, pregunt in enumerate(preguntas_juego, 1):
    print(f"\n--- Pregunta {i} de 5 ---")
    print(pregunt['pregunta'])
    
    # Mostrar opciones A, B, C, D
    for letra, opcion in pregunt["opciones"].items():
        print(f"{letra}: {opcion}")
    
    # Validación de respuesta única y válida
    respuesta = ""
    while respuesta not in ["A", "B", "C", "D"]:
        respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
    
    # Comprobar si acertó
    if respuesta == pregunt["respuesta"]:
        print("¡Epa, atinaste!")
        puntaje += 20
        correctas += 1
    else: 
        print(f"Tai mal, la respuesta correcta era: {pregunt['respuesta']}")

# 4. Final y Ranking
print("\n" + "="*20)
print(f"RESUMEN PARA: {nombre}")
print(f"Puntaje Total: {puntaje}")
print(f"Correctas: {correctas}/5")
print("="*20)

# --- GUARDAR EN RANKING ---
with open("ranking.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre},{puntaje}\n")

# --- MOSTRAR RANKING GENERAL ORDENADO ---
ver_ranking = input("\n¿Quieres ver el ranking general? (s/n): ").lower()

if ver_ranking == "s":
    try:
        # 1. Leer todas las jugadas históricas
        with open("ranking.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        lista_ranking = []
        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                nombre_jugador = partes[0]
                puntos_jugador = int(partes[1])
                lista_ranking.append([nombre_jugador, puntos_jugador])
        
        # 2. Ordenar de mayor a menor basándonos en el puntaje (posición 1 de la sublista)
        # reverse=True hace que el mayor vaya arriba
        lista_ranking.sort(key=lambda x: x[1], reverse=True)

        # 3. Mostrar el Top 10 o todos los que existan
        print("\n🏆 RANKING GENERAL (TOP 10) 🏆")
        print("-" * 30)
        for i, jugador in enumerate(lista_ranking[:10], 1):
            print(f"{i}. {jugador[0]} ---- {jugador[1]} pts")
        print("-" * 30)

    except FileNotFoundError:
        print("Aún no hay nadie en el ranking. ¡Sé el primero!")
    except Exception as e:
        print(f"No se pudo cargar el ranking: {e}")

