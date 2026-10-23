def encontrar_rutas(grafo, inicio, destino):
    rutas = []
    
    # Búsqueda en profundidad (DFS)
    def dfs(actual, costo_actual, camino_actual):
        # Si llegamos al destino, guardamos la ruta y su costo
        if actual == destino:
            rutas.append((camino_actual, costo_actual))
            return
        
        # Explorar todos los nodos vecinos
        for vecino, costo in grafo[actual].items():
            # Condición para evitar ciclos (no visitar un nodo que ya visitamos en esta ruta)
            if vecino not in camino_actual:
                # Llamada recursiva sumando el costo y agregando el vecino a la ruta
                dfs(vecino, costo_actual + costo, camino_actual + [vecino])
                
    # Iniciar la búsqueda desde el nodo de inicio con costo 0
    dfs(inicio, 0, [inicio])
    
    # Ordenar las rutas de menor a mayor costo
    rutas_ordenadas = sorted(rutas, key=lambda x: x[1])
    return rutas_ordenadas

# Representación del grafo basado en tu imagen
grafo = {
    'A': {'B': 4, 'C': 3, 'K': 5},
    'B': {'A': 4, 'C': 2, 'G': 4, 'D': 5},
    'C': {'A': 3, 'B': 2, 'K': 3, 'D': 4, 'E': 6},
    'K': {'A': 5, 'C': 3, 'L': 4},
    'G': {'B': 4, 'H': 5},
    'D': {'B': 5, 'C': 4, 'H': 4, 'E': 3, 'F': 6},
    'H': {'G': 5, 'D': 4, 'I': 6},
    'E': {'C': 6, 'D': 3, 'I': 5, 'F': 2, 'L': 4},
    'F': {'D': 6, 'E': 2, 'L': 3, 'I': 3, 'J': 6},
    'L': {'K': 4, 'E': 4, 'F': 3},
    'I': {'H': 6, 'E': 5, 'F': 3, 'J': 3},
    'J': {'I': 3, 'F': 6}
}

if __name__ == "__main__":
    # Nodos de inicio y destino
    nodo_inicio = 'A'
    nodo_destino = 'J'
    
    # Calcular todas las rutas
    todas_las_rutas = encontrar_rutas(grafo, nodo_inicio, nodo_destino)
    
    print(f"¡Búsqueda completada! Se encontraron un total de {len(todas_las_rutas)} rutas posibles desde {nodo_inicio} hasta {nodo_destino}.\n")
    
    # Interacción con el usuario en la terminal
    try:
        cantidad = int(input("¿Cuántas de las rutas deseas visualizar? "))
        
        print("\n--- Resultados (Ordenados por menor costo) ---")
        # Mostrar solo la cantidad que el usuario pidió
        for i, (ruta, costo) in enumerate(todas_las_rutas[:cantidad]):
            ruta_formateada = " -> ".join(ruta)
            print(f"Ruta {i+1}: {ruta_formateada} | Costo Total: {costo}")
            
    except ValueError:
        print("\nError: Por favor, ingresa un número entero válido.")