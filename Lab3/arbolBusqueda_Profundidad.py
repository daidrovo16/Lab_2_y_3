
"""
Link de Github
https://github.com/daidrovo16/Lab_2_y_3.git
"""

# Importacion de librerias
from collections import defaultdict

class Grafos:
    
    """
    
    Implementacion de la clase grafo haciendo uso de las listas de adyacencia
    
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
    """ Se crea un grafo predeterminado por datos definido"""
g = Grafos()
#-----------------------------------------------------
print("Caso de prueba 1:")
g.agrega_Borde(8, 1)
g.agrega_Borde(4, 6)
g.agrega_Borde(2, 7)
g.agrega_Borde(3, 2)
g.agrega_Borde(2, 5)
g.agrega_Borde(2, 8)
g.agrega_Borde(3, 9)

print("Busqueda en Profundidadss inicializando desde el verice(1)")
g.busqueda(1)
print()
#-----------------------------------------------------
print("Caso de prueba 2:")
g.agrega_Borde(8, 1)
g.agrega_Borde(4, 6)
g.agrega_Borde(2, 7)
g.agrega_Borde(3, 2)
g.agrega_Borde(2, 5)
g.agrega_Borde(2, 8)
g.agrega_Borde(3, 9)
print("Busqueda en Profundidadss inicializando desde el verice(3)")
g.busqueda(3)
print()

#-----------------------------------------------------
print("Caso de prueba 3:")
g.agrega_Borde(0, 1)
g.agrega_Borde(3, 4)
g.agrega_Borde(1, 2)
g.agrega_Borde(7, 2)
g.agrega_Borde(4, 5)
g.agrega_Borde(2, 3)
g.agrega_Borde(4, 3)
 
print("Busqueda en Profundidadss inicializando desde el verice(1)")
g.busqueda(1)
print()


