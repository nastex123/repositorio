import json

def cargar_preguntas():
    try:
        # Añadimos encoding utf-8 para que no falle con tildes o eñes
        with open("preguntas.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Error: No se encuentra el archivo 'preguntas.json' en esta carpeta.")
        return []
    except Exception:
        print("samonda tamala (error al leer el JSON)")
        return []
