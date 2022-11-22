import numpy as np
from claseNodo import Nodo

class Grafo: #grafo conexo
    __vertices = None
    __matriz = None
    __LNV=None

    def __init__(self,vertices=[]):
        self.__vertices=vertices
        self.__LNV=[]
        self.__matriz=np.empty(len(vertices),dtype=Nodo)

    def Buscar(self, elemento):
        bandera = True
        i = 0
        while bandera and i < len(self.__vertices):
            if self.__vertices[i] == elemento:
                bandera = False
            else:
                i += 1
        if bandera == False:
            return i
        else:
            return None   

    def Aristas(self,elemento1,elemento2,peso):
        i=self.Buscar(elemento1)
        j=self.Buscar(elemento2)
        if i != None and j!=None:
            self.__matriz[i][j]=peso
            self.__matriz[j][i]=peso
        else:
            print("posicion I o J no encontrada")
            
    def NodoPrometedor(self):
        min=0
        nodo = None
        for i in self.__vertices:
            print(self.__LNV) 
            print("nodos vivos")
            print(i.Colision(self.__LNV))
            if i.Colision(self.__LNV) < min: 
                min = i.Colision(self.__LNV)
                nodo=i
                print(nodo.getX(),nodo.getY())
        return nodo

    def ArbolEXP(self):
        nodo=self.NodoPrometedor()
'''
Prim(T: Tabla);
Para i desde 1 hasta |V| hacer
    v ← vertice con la distancia mas corta y desconocido
    T[v].conocido ← True
    Para cada w adyacente a v hacer
        Si T[w].conocido = False
        entonces
            Si w(v,w) < T[w].distancia
            entonces
                T[w].distancia ← w(v,w)
                T[w].camino ← v
            FinSi
        FinSi
    FinPara
FinPara
'''
        
'''
repetir
 elegir el nodo mas prometedor como nodo_E;
 generar todos sus hijos;
 matar el nodo_E;
 para cada hijo hacer
    si colision(hijo) > colision(mejor_solucion_en_curso) 
        entonces se mata
    sino
        si no es solucion 
            entonces se pasa a la lista_de_nodos_vivos
        sino 
            {es solucion: el coste no es estimado sino real}
            es la mejor_solucion_en_curso y se revisa la lista_de_nodos_vivos,
            eliminando los que prometen algo peor
        fsi
    fsi
 fpara
hasta que la lista esta vacia
 '''
if __name__ == '__main__':
    lista=[]
    for i in range(4):
        for j in range(4):
            new=Nodo(4,i,j)
            lista.append(new)
    grafo=Grafo(lista)
    grafo.NodoPrometedor()