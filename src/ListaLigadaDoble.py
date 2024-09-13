'''
Author: Juan Camilo Moná Luján
Info: camilo.mona.lujan@gmail.com
'''

from NodoDoble import Nodo

class LLD:
    def __init__(self, val):
        self._primerNodo = Nodo(val)
        self._ultimoNodo = None
        self._nodoActual = None

    @property
    def primerNodo(self):
        return self._primerNodo

    @primerNodo.setter
    def primerNodo(self, nodo):
        self._primerNodo = nodo

    @property
    def nodoActual(self):
        return self._nodoActual

    @nodoActual.setter
    def nodoActual(self, nodo):
        self._nodoActual = nodo

    @property
    def ultimoNodo(self):
        return self._ultimoNodo

    @ultimoNodo.setter
    def ultimoNodo(self, nodo):
        self._ultimoNodo = nodo

    #_______ MÉTODOS PROPIOS DE LA CLASE ________
    # -------------------------------------------
    def _validarAnterior(self):
        return True if self.nodoActual.anterior is None else False

    # -------------------------------------------
    def _validarSiguiente(self):
        return True if self.nodoActual.siguiente is None else False

    # -------------------------------------------
    def recorrerListaAdelante(self, bandera = False):
        if bandera:
            self.nodoActual = self.nodoActual.siguiente
        while self._validarSiguiente():
            self.nodoActual = self.nodoActual.siguiente

    # -------------------------------------------
    def recorrerListaAtras(self, bandera = False):
        if bandera:
            self.nodoActual = self.nodoActual.anterior
        while self._validarAnterior():
            self.nodoActual = self.nodoActual.anterior

    #-------------------------------------------
    def buscarElementoAdelante(self, nodo):
        nodoTmp = nodo
        self.nodoActual = self.primerNodo
        while self._validarSiguiente():
            self.recorrerListaAdelante(True)
            if self.nodoActual == nodoTmp:
                return self.nodoActual
        return None
    # --------------------------------------------
    def buscarElementoAdelante_Index(self, index):
        contadorTmp = 0
        self.nodoActual = self.primerNodo
        while contadorTmp != index:
            self.recorrerListaAdelante(True)
            contadorTmp += 1
        return self.nodoActual
    # -------------------------------------------
    def buscarElementoAtras(self, nodo):
        nodoTmp = nodo
        self.nodoActual = self.ultimoNodo
        while self._validarAnterior():
            self.recorrerListaAtras(True)
            if self.nodoActual == nodoTmp:
                return self.nodoActual
        return None
    #--------------------------------------------
    def buscarElementoAtras_Index(self, index):
        contadorTmp = 0
        self.nodoActual = self.ultimoNodo
        while contadorTmp != index:
            self.recorrerListaAtras(True)
            contadorTmp += 1
        return self.nodoActual
    # -------------------------------------------
    def tamaño(self):
        contadorTmp = 0;
        while self._validarSiguiente():
            self.recorrerListaAdelante(True)
            contadorTmp += 1
        return contadorTmp
    # -------------------------------------------
    def insertarPrimero(self, val):
        nodoTmp = Nodo(val)
        nodoTmp.siguiente = self.primerNodo
        self.primerNodo.anterior = nodoTmp
        self.primerNodo = nodoTmp
    #--------------------------------------------
    def insertarFinal(self, val):
        nodoTmp = Nodo(val)
        self.ultimoNodo.siguiente = nodoTmp
        nodoTmp.anterior = self.ultimoNodo
        self.ultimoNodo = nodoTmp
    # --------------------------------------------
    def insertarEn(self, val, index):
        nodoTmp = Nodo(val)



