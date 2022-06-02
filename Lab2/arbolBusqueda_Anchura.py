"""
Link de Github
https://github.com/daidrovo16/Lab_2_y_3.git
"""
''''''

from collections import defaultdict
class Grafo:
    """
        Se importa la libreria de collections para poder usar el diccionario defaultdict. 
        Al importar defaultdict, esta hace la creacion de un diccionario que representa un grafo.
        La diferencia de queue es que la cola es una lista, 
        mientras que defaultdict es un diccionario que representa una lista.
        
        --------------------------------------------------------------------------------- 
        El programa desarrollado Python3, de arboles binarios de busqueda por Anchura o recorrido BFS
        de un vertice dado. 
        
        ---------------------------------------------------------------------------------    
        BFS pasando por un vertice alcanzables desde la raiz.
        
        ----------------------------------------------------------------------------------
        class Grafo es una clase que representa 
        un grafo dirigido usando representación de lista de adyacencia
    """
    
    # Constructor
    def __init__(nodo):
        
        """
        Esta clase representa un grafo dirigido usando representación de lista de adyacencia.
        ---------------------------------------------------------------------------------        
        Se crea un instancia de la clase Grafo, y se le agrega una lista de adyacencia.
        Esta instancia se denomina __init__(nodo), a la que se le pasa un nodo.
        Creando una lista de adyacencia, en la cual se crea un diccionario 
        que almacena una lista de adyacencia.
        
        La variable que se creo en la instancia denominada nodo, es una lista de adyacencia.
        La cual se crea como un diccionario, donde se almacenan los vertices como llaves, 
        el nodo.grafo es un diccionario que representa el grafo.
        
        La API defaultdict(list) esusada en la creacion de un diccionario que crea una lista por defecto.
        
        Al pasar el nodo.grafo = defaultdict(list) se crea un diccionario que representa el grafo, 
        en forma de lista de adyacencia.
        """
        nodo.grafo = defaultdict(list)

    def agrega_Borde(nodo,u,v): 
        """ 
        Diccionario predeterminado para almacenar el gráfico
        ---------------------------------------------------------------------------------
        Para realizar el BFS, se agrega un borde entre los vertices u y v, 
        para esto se agrega el vertice v a la lista de adyacencia de u. 
        Para esto se debe tener en cuenta que el grafo es dirigido.
        Tambien se debe tener en cuenta que si el grafo al es dirigido, 
        se agrega un borde entre u y v, pero no entre v y u.
        ---------------------------------------------------------------------------------
        agrega_Borde(nodo,u,v) agrega un borde entre los vertices u y v, 
        append() agrega un elemento al final de la lista.
        nodo.grafo[u].append(v) agrega el vertice v a la lista de adyacencia de u.
        """
        nodo.grafo[u].append(v)

    def BFS(nodo, s):

        """ 
        Función para imprimir un BFS de gráfico
        BFS(nodo, s) imprime el BFS de gráfico desde el vertice s
        
        ---------------------------------------------------------------------------------
        Marca todos los vertices como no visitados
        Vertices_visitados = [False] * (max(nodo.grafo)+1) 
        crea una lista de False de longitud max(nodo.grafo)+1 
        
        ---------------------------------------------------------------------------------
        Crear una cola y lo pasa como lista. Se marca el nodo de origen visitado y se lo ingresa en la cola
        queue = [] crea una lista vacia
        queue.append(s) agrega el vertice s a la lista
        
        ---------------------------------------------------------------------------------
        Desencolar un vertice de hacer cola e imprimirlo
        vertice_Visitado[s] = True marca el vertice s como visitado 
    
        ---------------------------------------------------------------------------------
        Obtener todos los vertice adyacentes del vertice eliminados de la cola. Si un adyacente no ha sido visitado, luego márcalo
        visitado y ponerlo en cola
        while queue:
            s = queue.pop(0) elimina el primer elemento de la cola
            print(s, end = ' ') imprime el vertice s
            for i in nodo.grafo[s]: obtiene todos los vertices adyacentes del vertice s
            if vertice_Visitado[i] == False: marca el vertice i como visitado y lo pone en la cola
            queue.append(i) agrega el vertice i a la cola
            vertice_Visitado[i] = True marca el vertice i como visitado
            
            Al tener todo este while, se imprime el BFS de gráfico desde el vertice s, donde 
            se imprime el vertice s, y se imprime todos los vertices adyacentes del vertice s, 
            para esto se debe tener en cuenta que el grafo es dirigido.
            Al tener un vertice ya visitado en la cola, este elimina de la cola.
            Haciendo que el vertice s sea el siguiente de la cola, se puede imprimir el BFS de gráfico, 
            y haciendo que i sea el siguiente de la cola y asi sucesivamente. 
            
                '''
                Se crea un metodo __main__ para que el programa se ejecute, 
                para esto se crea una instancia de la clase Grafo. La cual se crea con el metodo __init__, 
                al tener casos de prueba, se crean instancias de la clase Grafo.
                Para esto se agrega diferentes casos de prueba, para que el programa se ejecute.
                Y pueda imprimir el BFS de gráfico.
                '''
        
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
#g.agrega_Borde(0, 1)
#g.agrega_Borde(0, 2)
#g.agrega_Borde(1, 2)
#g.agrega_Borde(2, 0)
#g.agrega_Borde(2, 3)
#g.agrega_Borde(3, 3)
#print ("Busqueda por anchura inicializando desde el vertice(2)")
#g.BFS(2) #Imprime los datos del grafo en forma de lista 
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 2:")
#g.agrega_Borde(5, 3)
#g.agrega_Borde(5, 7)
#g.agrega_Borde(3, 2)
#g.agrega_Borde(3, 4)
#g.agrega_Borde(2, 2)
#g.agrega_Borde(7, 8)
#g.agrega_Borde(4, 8)
#g.agrega_Borde(8, 8)
#print ("Busqueda por anchura inicializando desde el vertice(5)")
#g.BFS(5) #Imprime los datos del grafo en forma de lista 
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 3:")
#g.agrega_Borde(0, 1)
#g.agrega_Borde(0, 2)
#g.agrega_Borde(1, 2)
#g.agrega_Borde(1, 3)
#g.agrega_Borde(3, 4)
#g.agrega_Borde(2, 3)
#g.agrega_Borde(4, 0)
#g.agrega_Borde(4, 1)
#g.agrega_Borde(4, 5)
#g.agrega_Borde(5, 0)
#print ("Busqueda por anchura inicializando desde el vertice(0)")
#g.BFS(0) #Imprime los datos del grafo en forma de lista 
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 4:")
#g.agrega_Borde(0, 1)
#g.agrega_Borde(0, 2)
#g.agrega_Borde(1, 2)
#g.agrega_Borde(2, 0)
#g.agrega_Borde(2, 3)
#g.agrega_Borde(3, 3)
#g.agrega_Borde(3, 4)
#g.agrega_Borde(5, 4)
#g.agrega_Borde(5, 6)
#g.agrega_Borde(7, 6)
#print ("Busqueda por anchura inicializando desde el vertice(2)")
#g.BFS(2) #Imprime los datos del grafo en forma de lista 
#print()
print("-----------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------
print("Caso de prueba 5:")
g.agrega_Borde(0, 1)
g.agrega_Borde(0, 3)
g.agrega_Borde(0, 4)
g.agrega_Borde(4, 5)
g.agrega_Borde(3, 5)
g.agrega_Borde(1, 2)
g.agrega_Borde(5, 4)
print ("Busqueda por anchura inicializando desde el vertice(0)")
g.BFS(0) #Imprime los datos del grafo en forma de lista 
print()
