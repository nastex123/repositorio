# Sistema de Gestión de Inventario en Python

## Descripción

Este proyecto consiste en un sistema de gestión de inventario desarrollado en Python. Permite al usuario agregar productos, visualizar el inventario y calcular estadísticas básicas mediante un menú interactivo.

El programa utiliza estructuras fundamentales como listas, diccionarios, condicionales y bucles, cumpliendo con los requisitos establecidos en la actividad.

---

## Objetivo

Gestionar múltiples productos en un inventario utilizando un menú interactivo, validando los datos de entrada y calculando estadísticas básicas de forma eficiente.

---

## Funcionalidades

* Agregar producto
  Permite ingresar el nombre, precio y cantidad de un producto con validación de datos.

* Mostrar inventario
  Muestra todos los productos registrados en un formato claro.

* Calcular estadísticas

  * Valor total del inventario (precio × cantidad)
  * Cantidad total de productos

* Salir del sistema
  Finaliza la ejecución del programa.

---

## Estructura del programa

El código está organizado en las siguientes funciones:

* `agregar_producto()`
* `mostrar_inventario()`
* `calcular_estadisticas()`

Los productos se almacenan en una lista de diccionarios con la siguiente estructura:

```python
{
  "nombre": "Producto",
  "precio": 1000,
  "cantidad": 5
}
```

---

## Flujo del programa

1. Se muestra el menú principal.
2. El usuario selecciona una opción.
3. El sistema ejecuta la acción correspondiente.
4. El menú se repite hasta que el usuario decide salir.

---

## Validación de datos

El sistema valida:

* Que el precio sea un número decimal válido.
* Que la cantidad sea un número entero válido.
* Que la opción del menú sea correcta.

---

## Ejemplo de uso

```python
===== MENÚ INVENTARIO =====
1. Agregar producto
2. Mostrar inventario
3. Calcular estadísticas
4. Salir
Seleccione una opción: 1

Ingrese el nombre del producto: Lápiz
Ingrese el precio del producto: 500
Ingrese la cantidad del producto: 3

Producto agregado correctamente.
```

---

## Tecnologías utilizadas

* Python 3
* Consola / Terminal