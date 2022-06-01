"""
Link de Github
https://github.com/daidrovo16/Lab_2_y_3.git
"""
''''''

from collections import defaultdict
class Grafo:
    """
    
        El programa desarrollado Python3, de arboles binarios de busqueda por Anchura o recorrido BFS
        de un vertice dado. 
        ---------------------------------------------------------------------------------    
        BFS pasando por un vertice alcanzables desde la raiz.
        ----------------------------------------------------------------------------------
    
    """
    
    # Constructor
    def __init__(nodo):

        """
        Esta clase representa un grafo dirigido usando representación de lista de adyacencia
        ---------------------------------------------------------------------------------        
        """
        nodo.grafo = defaultdict(list)

    def agrega_Borde(nodo,u,v):
        """ 
        Diccionario predeterminado para almacenar el gráfico
        ---------------------------------------------------------------------------------
        """
        nodo.grafo[u].append(v)

    def BFS(nodo, s):
 
        """ 
        Función para imprimir un BFS de gráfico
        ---------------------------------------------------------------------------------
        Marca todos los vertices como no visitados
        ---------------------------------------------------------------------------------
        Crear una cola y lo pasa como lista. Se marca el nodo de origen visitado y se lo ingresa en la cola
        ---------------------------------------------------------------------------------
        Desencolar un vertice de hacer cola e imprimirlo
        ---------------------------------------------------------------------------------
        Obtener todos los vertice adyacentes del vertice eliminados de la cola. Si un adyacente no ha sido visitado, luego márcalo
        visitado y ponerlo en cola
        """
        vertice_Visitado = [False] * (max(nodo.grafo) + 1)
        queue = []
        queue.append(s)
        vertice_Visitado[s] = True

        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in nodo.grafo[s]:
                if vertice_Visitado[i] == False:
                    queue.append(i)
                    vertice_Visitado[i] = True

#-----------------------------------------------------------------------------------------------------------------------
    impresion2 = __init__.__doc__
    print (impresion2)
    impresion3 = agrega_Borde.__doc__
    print (impresion3)
    impresion4 = BFS.__doc__
    print (impresion4)

impresion1 = Grafo.__doc__
print(impresion1)


if __name__ == "__main__":

    g = Grafo()
print("Caso de prueba 1:")
g.agrega_Borde(0, 1)
g.agrega_Borde(0, 2)
g.agrega_Borde(1, 2)
g.agrega_Borde(2, 0)
g.agrega_Borde(2, 3)
g.agrega_Borde(3, 3)
print ("Busqueda por anchura inicializando desde el vertice(2)")
g.BFS(2)
print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 2:")
g.agrega_Borde(1, 2)
g.agrega_Borde(1, 3)
g.agrega_Borde(2, 4)
g.agrega_Borde(2, 5)
g.agrega_Borde(3, 5)
g.agrega_Borde(4, 5)
g.agrega_Borde(4, 6)
g.agrega_Borde(5, 6)
print ("Busqueda por anchura inicializando desde el vertice(1)")
g.BFS(1)
print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 3:")
g.agrega_Borde(1, 2)
g.agrega_Borde(4, 6)
g.agrega_Borde(2, 7)
g.agrega_Borde(3, 2)
g.agrega_Borde(2, 5)
g.agrega_Borde(2, 8)
g.agrega_Borde(7, 2)
g.agrega_Borde(4, 5)
g.agrega_Borde(2, 3)
 
print ("Busqueda por anchura inicializando desde el vertice(2)")
g.BFS(1)
print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 4:")
g.agrega_Borde(1, 2)
g.agrega_Borde(4, 6)
g.agrega_Borde(2, 7)
g.agrega_Borde(3, 2)
g.agrega_Borde(2, 5)
g.agrega_Borde(2, 8)
g.agrega_Borde(7, 2)
g.agrega_Borde(4, 5)
g.agrega_Borde(2, 3)
 
print ("Busqueda por anchura inicializando desde el vertice(2)")
g.BFS(1)
print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 5:")
g.agrega_Borde(1, 2)
g.agrega_Borde(4, 6)
g.agrega_Borde(2, 7)
g.agrega_Borde(3, 2)
g.agrega_Borde(2, 5)
g.agrega_Borde(2, 8)
g.agrega_Borde(7, 2)
g.agrega_Borde(4, 5)
g.agrega_Borde(2, 3)
 
print ("Busqueda por anchura inicializando desde el vertice(2)")
g.BFS(1)
print()
