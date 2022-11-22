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

    def setReina(self,x,y):
        self.__arreglo[x]=y
        
    def getX (self):
        return self.__pos
    
    def getY (self):
        return self.__arreglo[self.__pos]
    
    def Colision(self,lista):
        if self.__pos != None and len(lista) != 0:    
            x=self.__pos
            y=self.__arreglo[self.__pos]
            choca=0
            for reina in lista: #recorro la lista de reinas
                if abs(x+y) != abs (reina.getX()+reina.getY()) and abs(x-y) != abs(reina.getX()-reina.getY()):#diagonales
                    if x != reina.getX() and y != reina.getY():#vertical y horizontal
                        pass
                    else:
                        choca+=1
                else:
                    choca +=1
            retorna=choca
        else:
            retorna=0
            return retorna