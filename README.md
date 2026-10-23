#  Buscador de Rutas Óptimas en Grafos (DFS)

Este proyecto es un script interactivo en Python que calcula y muestra las mejores rutas posibles entre dos puntos dentro de un grafo ponderado. Utiliza el algoritmo de **Búsqueda en Profundidad (DFS)** para explorar los caminos, evitando ciclos cerrados y ordenando los resultados del menor al mayor costo.

##  Requerimientos

Para ejecutar esta aplicación, necesitas lo siguiente:

*   **Lenguaje:** Python 3.6 o superior.
*   **Librerías:** Ninguna externa. El script utiliza únicamente funciones nativas de la biblioteca estándar de Python (no necesitas usar `pip install`).
*   **Servicios de terceros:** No requiere conexión a internet, APIs, ni bases de datos externas. Todo se ejecuta de manera local.

##  Cómo ejecutar la aplicación

1.  Clona o descarga este código en tu computadora.
2.  Asegúrate de guardar el código en un archivo llamado `rutas.py`.
3.  Abre una terminal o símbolo del sistema.
4.  Navega hasta la carpeta donde guardaste el archivo.
5.  Ejecuta el siguiente comando:
    ```bash
    python rutas.py
    ```

##  Datos de entrada requeridos

1.  **Grafo (Interno):** El mapa de nodos, sus conexiones y costos ya viene preconfigurado dentro del código en formato de diccionario de Python. Si deseas cambiar las rutas disponibles, debes editar la variable `grafo` directamente en el código de `rutas.py`.
2.  **Interacción en consola:** Durante la ejecución, el programa pausará y te pedirá un dato de entrada:
    *   `¿Cuántas de las mejores rutas deseas visualizar?`
    *   Debes ingresar un **número entero** (por ejemplo: `5`, `10`, `19`).

##  Datos de salida

El programa imprimirá directamente en la terminal:
1. El total de rutas válidas encontradas desde el nodo de inicio hasta el nodo destino.
2. Una lista ordenada (de menor a mayor costo) con las mejores rutas según la cantidad que solicitaste en el paso anterior.

**Ejemplo de salida:**
```text
¡Búsqueda completada! Se encontraron un total de 19 rutas posibles desde A hasta J.

¿Cuántas de las mejores rutas deseas visualizar? 3

--- Resultados (Ordenados por menor costo) ---
Ruta 1: A -> C -> E -> I -> J | Costo Total: 17
Ruta 2: A -> C -> E -> F -> I -> J | Costo Total: 17
Ruta 3: A -> C -> E -> F -> J | Costo Total: 17
