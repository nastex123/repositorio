# Sistema de Inventario en Python

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión de inventario en Python que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar), calcular estadísticas y manejar persistencia de datos mediante archivos CSV.

El sistema está diseñado para trabajar completamente en consola, utilizando estructuras de datos como listas y diccionarios, así como una arquitectura modular basada en funciones.

## Objetivos

- Implementar un sistema de inventario funcional en Python
- Aplicar estructuras de datos (listas y diccionarios)
- Modularizar el código en múltiples archivos
- Gestionar persistencia mediante archivos CSV
- Manejar errores y validaciones de entrada

## Características

- Agregar productos al inventario
- Mostrar inventario completo
- Buscar productos por nombre
- Actualizar precio y cantidad
- Eliminar productos
- Calcular estadísticas del inventario
- Guardar datos en archivo CSV
- Cargar datos desde archivo CSV
- Fusión o sobrescritura de datos al importar

## Estructura del Proyecto
├── app.py # Archivo principal (menú y control del sistema)
├── servicios.py # Lógica del inventario (CRUD y estadísticas)
├── archivos.py # Manejo de archivos CSV

## Estructura de Datos

El inventario se maneja como una lista de diccionarios con la siguiente estructura:

```python
{
    "nombre": str,
    "precio": float,
    "cantidad": int
}
```
Uso del Sistema
1. Ejecutar el archivo principal:
python app.py

2. Seleccionar una opción del menú:
1: Agregar producto
2: Mostrar inventario
3: Buscar producto
4: Actualizar producto
5: Eliminar producto
6: Ver estadísticas
7: Guardar en CSV
8: Cargar desde CSV
9: Salir

Persistencia con CSV
El sistema permite guardar y cargar el inventario usando archivos CSV, un formato ampliamente utilizado para almacenar datos tabulares de forma simple y compatible entre aplicaciones

Formato del archivo:
nombre,precio,cantidad
Producto1,1000,5
Producto2,2000,3

Manejo de Errores

El sistema incluye:

Validación de entradas (números positivos)
Manejo de excepciones con try/except
Control de archivos inexistentes o corruptos
Omisión de filas inválidas en CSV
Repositorio

El código completo del proyecto se encuentra disponible en:

https://github.com/nastex123/repositorio/tree/historia3

Requisitos
Python 3.x
No requiere librerías externas
