import numpy as np 
from classCola import ColaEnlazada
from classPila import PilaEnlazada

#Al ser un grafo no dirigido la info esta duplicada, entonces se trabaja con un arreglo

class grafoSecuencial(object):
    __conjunto_vertices = None
    __cant_vertices = 0 
    __arreglo = None 

    def __init__(self):
        self.__conjunto_vertices = None
        self.__cant_vertices = 0 
        self.__arreglo = None 

#-------------------------------------------------------------------------------------------------
    #Construye la tabla que representa el grafo
    def crearGrafo(self, cantNodos, vertices):
        self.__conjunto_vertices = vertices
        self.__cant_vertices = cantNodos
        self.__arreglo = np.empty(int(cantNodos*(cantNodos+1)/2), dtype=int)
        self.cerearArreglo()

#-------------------------------------------------------------------------------------------------    
    def cerearArreglo(self):
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = 0 

#-------------------------------------------------------------------------------------------------
    def buscarIndice(self, nodo):
        i = 0
        while( i<self.__cant_vertices and nodo!=self.__conjunto_vertices[i]):
            i+=1 
        return i

#-------------------------------------------------------------------------------------------------
    def cargarArreglo(self, i, j, peso=1):
        #Si el peso no viene, no es un grafo ponderado
        if(i<=j):
            aux = j
            j = i     #Intercambio las posiciones para unicamente trabajar con la diagonal de abajo
            i = aux
        dir = int ( i*(i-1)/2 + j )
        #Le resta 1 por lo que el indice del arrglo comienza en 0
        self.__arreglo[dir-1] = peso

#-------------------------------------------------------------------------------------------------
    #Viene directamene los indices de los nodos
    def adyacentes(self, i, j): 
        if(i<=j):
            aux = j    #Intercambio
            j = i      #Para trabajar con la matriz triangular inferior
            i = aux
        dir = int ( i*(i-1)/2 + j )
        if(self.__arreglo[dir-1] == 1):
            return True
        else:
            return False

#-------------------------------------------------------------------------------------------------
    def getGrado(self, nodo):
        origen = self.buscarIndice(nodo) + 1
        cont = 0
        for i in range(len(self.__conjunto_vertices)):
            if(self.adyacentes(origen,i+1)):
                cont+=1 
        return cont

#-------------------------------------------------------------------------------------------------
    def recorridoREA(self, nodo_inicial):
        longitudes = np.empty(self.__cant_vertices, dtype=str)  #Arreglo de longitud
        cola = ColaEnlazada()
       
        for i in range(self.__cant_vertices):
            longitudes[i] = '*'   #Simboliza un valor alto 
        
        indice_actual = self.buscarIndice(nodo_inicial)
        #Marcamos el vertice como visitado
        longitudes[indice_actual] = str(0)
        
        cola.insertar(nodo_inicial)

        while (not cola.vacia()):
            vertice_actual = cola.suprimir()
            print(vertice_actual, end=' ')
            indice_actual = self.buscarIndice(vertice_actual)

            for i in range(self.__cant_vertices):
                if(self.adyacentes(indice_actual+1, i+1)):
                    if(longitudes[i] == '*'):
                        #Marca como visitados los vertices adyacnetes que no han sido visitados aun
                        longitudes[i] = str(int(longitudes[indice_actual]) + 1)
                        cola.insertar(self.__conjunto_vertices[i])
        return longitudes

#-------------------------------------------------------------------------------------------------
    #Recorrido en profundidad
    def recorridoREP(self, nodo_inicial):
        visitados = np.empty(self.__cant_vertices, dtype=bool)
        for i in range(self.__cant_vertices):
            visitados[i] = False

        indice_actual = self.buscarIndice(nodo_inicial)
        visitados[indice_actual] = True

        print(nodo_inicial, end= ' - ')

        for i in range(self.__cant_vertices):
            if(self.adyacentes(indice_actual+1, i+1)):
                if(visitados[i] == False):
                    self.visitar(self.__conjunto_vertices[i], visitados)
        return visitados

    def visitar(self, nodo_actual, visitados):
        print(nodo_actual, end=' - ')
        indice_actual = self.buscarIndice(nodo_actual)
        visitados[indice_actual] = True
        for i in range(self.__cant_vertices):
             if(self.adyacentes(indice_actual+1, i+1)):
                 if(visitados[i] == False):
                     self.visitar(self.__conjunto_vertices[i], visitados)

#-------------------------------------------------------------------------------------------------
    #Recorrido en profundidad con manejo de pila
    def recorridoREPconPila(self, nodo_inicial):
        visitados = np.empty(self.__cant_vertices, dtype=bool)
        pila = PilaEnlazada()
        for i in range(self.__cant_vertices):
            visitados[i] = False 
        
        indice_actual = self.buscarIndice(nodo_inicial)
        visitados[indice_actual] = True 
        
        pila.insertar(nodo_inicial)
        while(not pila.vacia()):
            vertice_actual = pila.suprimir()
            print(vertice_actual, end=' - ')
            indice_actual = self.buscarIndice(vertice_actual)
            for i in range(self.__cant_vertices):
                #Para cada adyacente lo marca como visitado
                if(self.adyacentes(indice_actual+1, i+1)):
                    #Si no ha sido visitado
                    if(visitados[i] == False):
                        #La pila es la que garantiza el recorrido en profundidad
                        pila.insertar(self.__conjunto_vertices[i]) 
                        visitados[i] = True  #Lo marca como visitado
        return visitados

#-------------------------------------------------------------------------------------------------
    def conexo(self):
        i=0 
        visitados = self.recorridoREP(self.__conjunto_vertices[i])
        conexo = True
        while(i<self.__cant_vertices and conexo==True):
            if(visitados[i]!=True):
                conexo = False 
            else:
                i+=1
        return conexo

#-------------------------------------------------------------------------------------------------
    def mostrarArreglo(self):
        print(self.__arreglo) 

#-------------------------------------------------------------------------------------------------
    def mostrarVertices(self):
        print(self.__conjunto_vertices)
    
#-------------------------------------------------------------------------------------------------
    def getCantidadNodos(self):
        return self.__cant_vertices
