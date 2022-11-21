import numpy as np

class Nodo:
    __arreglo = None #arreglo posee la reina
    __dimension = None #dimension del arreglo
    __pos = None #coordenadas reina

    def __init__ (self, cant, x=None, y=None):
        self.__dimension = cant
        self.__arreglo = np.full(cant, -1)
        if x !=None and y != None:
            self.__pos=x
            self.__arreglo[x]=y
            
    def getX (self):
        return self.__pos
    
    def getY (self):
        return self.__arreglo[self.__pos]
    
    def hijos(self, y,lista):#y:nivel
        for x in range(self.__dimension):
            for reina in lista:
                if abs(x+y) != abs (reina.getX()+reina.getY()) and abs(x-y) != abs(reina.getX()-reina.getY()):
                    if x != reina.getX() and y != reina.getY():
                        lista.append(Nodo(self.__dimension,x,y))
        return lista