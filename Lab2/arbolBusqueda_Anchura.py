"""
Link de Github
https://github.com/daidrovo16/Lab_2_y_3.git
"""
'''Programa Python3 para imprimir el recorrido BFS
    de un vértice fuente dado. 
    BFS pasando por un vértices alcanzables desde 
    la raiz.'''

from collections import defaultdict

'''Esta clase representa un grafo dirigido
usando representación de lista de adyacencia'''
class Grafo:

    # Constructor
    def __init__(nodo):

        nodo.grafo = defaultdict(list)

    # diccionario predeterminado para almacenar el gráfico
    def agrega_Borde(nodo,u,v):
        nodo.grafo[u].append(v)

    # Función para imprimir un BFS de gráfico
    def BFS(nodo, s):
 
        """ Marca todos los vertices como no visitados"""
        vertice_Visitado = [False] * (max(nodo.grafo) + 1)

        """Crear una cola y lo pasa como lista.
            Se marca el nodo de origen visitado y se lo ingresa en la cola
        """
        queue = []
        queue.append(s)
        vertice_Visitado[s] = True
 
        while queue:
 
            """Desencolar un vértice de
             hacer cola e imprimirlo"""
            s = queue.pop(0)
            print (s, end = " ")
 
            """ Obtener todos los vértices adyacentes del
            vértices eliminados de la cola. Si un adyacente
            no ha sido visitado, luego márcalo
            visitado y ponerlo en cola """
            for i in nodo.grafo[s]:
                if vertice_Visitado[i] == False:
                    queue.append(i)
                    vertice_Visitado[i] = True
    impresion2 = __init__.__doc__
    print (impresion2)
    impresion3 = agrega_Borde.__doc__
    print (impresion3)
    impresion4 = BFS.__doc__
    print (impresion4)

impresion1 = Grafo.__doc__
print(impresion1)


if __name__ == "__main__":
    """Codigo de ejecucion.
    Crear un gráfico dado en
    el diagrama de arriba"""
g = Grafo()
g.agrega_Borde(0, 1)
g.agrega_Borde(0, 2)
g.agrega_Borde(1, 2)
g.agrega_Borde(2, 0)
g.agrega_Borde(2, 3)
g.agrega_Borde(3, 3)
 
print ("Busqueda por anchura inicializando desde el vertice(2)")
g.BFS(2)

print()
