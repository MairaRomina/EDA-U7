import numpy as np

class ArbolExpansion: #grafo conexo
    __vertices = None
    __matriz = None
    __LNV=None #Lista de nodos vivos

    def __init__(self,vertices):
        self.__vertices=vertices 
        self.__matriz=np.full(vertices)

    def arbol(self):
        pass
'''
repetir
 elegir el nodo mas prometedor como nodo_E;
 generar todos sus hijos;
 matar el nodo_E;
 para cada hijo hacer
    si coste(hijo) > coste(mejor_solucion_en_curso) 
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