
"""
Link de Github
https://github.com/daidrovo16/Lab_2_y_3.git
"""

# Importacion de librerias
from collections import defaultdict

class Grafos:
    """
    Para ello se debe de crear una instancia de la clase Grafos.
    Se agregan los bordes del grafo, y luego se debe de llamar a la funcion busqueda.
    la cual recibe como parametro el nodo inicial. Esto se realiza para que el programa pueda mostrar el recorrido del grafo. 
    -------------------------------------------------
    Antes de empezar a entrar a la funcion, se importa la libreria collections.defaultdict. 
    Esta libreria nos permite crear un diccionario de datos, en este caso, un diccionario de listas. 
    Luego de esto se Implementa de la clase Grafo haciendo uso de las listas de adyacencia para el almacenamiento de los nodos 
    -------------------------------------------------
    """
    # Constructor
    def __init__(self):
        """
        Se realiza la implementacion de un diccionario de datos
        para el almacenamiento de los nodos del grafo
        -------------------------------------------------
        Se implementa la funcion de agregacion de un borde al grafo
        
        """
        self.grafos = defaultdict(list)

    def agrega_Borde(self, u, v):
            """ 
            Funcion para el uso de Busqueda en profundidad(DFS)
            """
            self.grafos[u].append(v)
        
    def DFS(self, v, busqueda_Marcada):
        
        """
            
            Funcion que visita o marca el nodo y lo muestra como obtenido
            ---------------------------------------------
            Funcion que indica la recurrencia de los vertices adyacentes al vertice obtenido
            ------------------------------------------
            Funcion para hacer el recorrido en DFS. Uso de recursividad en la busqueda por profundidad
        """
        busqueda_Marcada.add(v)
        print(v, end=' ')
    
        for visita_Vertice in self.grafos[v]:
            if visita_Vertice not in busqueda_Marcada:
                self.DFS(visita_Vertice, busqueda_Marcada)


    def busqueda(self, v):
        
        """
        Crea una lista, la cual almacena los nodos visitados
        
        --------------------------------------------------
        Se genera un llamada a la funcion recursiva,
        la cual muestra el recorrido del arbol
        
        """
        busqueda_Marcada = set()

        
        self.DFS(v, busqueda_Marcada) 

#-----------------------------------------------------------------------------------------------------------------------
    impresion3 = __init__.__doc__
    print (impresion3)             
    impresion2 = agrega_Borde.__doc__
    print (impresion2)
    impresion1 = DFS.__doc__
    print (impresion1)
    impresion5 = busqueda.__doc__
    print (impresion5)

impresion4 = Grafos.__doc__
print (impresion4)  

if __name__ == '__main__':
    """ Se crea un grafo predeterminado por datos definido
    """
g = Grafos()
#-----------------------------------------------------
print("Caso de prueba 1:")
g.agrega_Borde(0, 1)
g.agrega_Borde(0, 2)
g.agrega_Borde(1, 3)
g.agrega_Borde(1, 4)
g.agrega_Borde(1, 5)
g.agrega_Borde(2, 6)
print("Busqueda en Profundidadss inicializando desde el vertice(0)")
g.busqueda(0)
print()
print("-----------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------
print("Caso de prueba 2:")
#g.agrega_Borde(1, 2)
#g.agrega_Borde(1, 3)
#g.agrega_Borde(2, 4)
#g.agrega_Borde(2, 5)
#g.agrega_Borde(3, 6)
#g.agrega_Borde(3, 7)
#print("Busqueda en Profundidadss inicializando desde el vertice(1)")
#g.busqueda(1)
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------
print("Caso de prueba 3:")
#g.agrega_Borde(1, 2)
#g.agrega_Borde(2, 5)
#g.agrega_Borde(1, 3)
#g.agrega_Borde(1, 4)
#g.agrega_Borde(2, 6)
#g.agrega_Borde(6, 4)
#print("Busqueda en Profundidadss inicializando desde el vertice(1)")
#g.busqueda(1)
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------
print("Caso de prueba 4:")
#g.agrega_Borde(0, 1)
#g.agrega_Borde(0, 2)
#g.agrega_Borde(1, 2)
#g.agrega_Borde(2, 4)
#g.agrega_Borde(0, 3)
#print("Busqueda en Profundidadss inicializando desde el vertice(0)")
#g.busqueda(0)
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------
print("Caso de prueba 5:")
#g.agrega_Borde(0, 1)
#g.agrega_Borde(0, 2)
#g.agrega_Borde(1, 3)
#g.agrega_Borde(1, 4)
#g.agrega_Borde(1, 5)
#g.agrega_Borde(1, 6)
#g.agrega_Borde(6, 2)
#print("Busqueda en Profundidadss inicializando desde el vertice(0)")
#g.busqueda(0)
#print()
