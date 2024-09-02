"""
Author: Juan Camilo Moná Luján
Fecha: 01 - 09 - 2024
"""

from Nodo import Nodo

class ListaLigadaSimple:

    def __init__(self, val):
        self._cabeceraNodo = Nodo(val)
        self._nodoActual = None

    # ----- GETTERS Y SETTERS DE LA CLASE ------
    @property
    def cabeceraNodo(self):
        return self._cabeceraNodo

    @cabeceraNodo.setter
    def cabeceraNodo(self, val):
        self._cabeceraNodo = val;

    @property
    def nodoActual(self):
        return self._nodoActual

    @nodoActual.setter
    def nodoActual(self, nodo):
        self._nodoActual = nodo

    # ----- MÉTODOS PROPIOS DE LA CLASE ------
    def insertar(self, val):
        nodoTmp = Nodo(val)
        if self.cabeceraNodo.siguiente is None:
            self.cabeceraNodo.siguiente = nodoTmp
            self.nodoActual = nodoTmp
            return

        self.nodoActual = self.cabeceraNodo
        while self.nodoActual.siguiente is not None:
            self.nodoActual = self.nodoActual.siguiente

        self.nodoActual.siguiente = nodoTmp
        self.nodoActual = nodoTmp

        print("Se ha insertado correctamente el nodo {}".format(self.nodoActual))
    # ---------------------------------------------
    def insertarPrimero(self, val):
        nodoTmp = Nodo(val)
        nodoTmp.siguiente = self.cabeceraNodo
        self.cabeceraNodo = nodoTmp

        print("Se ha actualizado correctamente la cabecera del nodo: {}".format(nodoTmp))
    # ---------------------------------------------
    def imprimirLista(self):
        self.nodoActual = self.cabeceraNodo
        print('|{:<10} | {:<15}|'.format('VALOR', 'LIGAS'))
        while self.nodoActual.siguiente is not None:
            print('|{:<10} | {:<10}|'.format(self.nodoActual.informacion, id(self.nodoActual.siguiente)))
            self.nodoActual = self.nodoActual.siguiente
    # ---------------------------------------------
    def tamañoLista(self):
        self.nodoActual = self.cabeceraNodo
        contadorTmp = 0
        if self.nodoActual is None:
            return contadorTmp
        while self.nodoActual.siguiente is not None:
            self.nodoActual = self.nodoActual.siguiente
            contadorTmp += 1
        return contadorTmp
    # ---------------------------------------------
    def validarNodo(self, val):
        self.nodoActual = self.cabeceraNodo
        contadorTmp = 0
        if self.nodoActual is None:
            if self.nodoActual.informacion == val:
                print("Información encontrada en cabecera")
                return 1
            else:
                print("Lista vacia, no se encuentra información")
                return 0
        while self.nodoActual is not None:
            if self.nodoActual.informacion == val:
                return 1
            self.nodoActual = self.nodoActual.siguiente
            contadorTmp += 1
        return 0
    # ---------------------------------------------
    def imprimirIndex(self, val):
        bandera = self.validarNodo(val)
        if bandera == 1:
            contadorTmp = 0
            self.nodoActual = self.cabeceraNodo
            while self.nodoActual.siguiente is not None:
                if self.nodoActual.informacion == val:
                    return contadorTmp
                self.nodoActual = self.nodoActual.siguiente
                contadorTmp += 1
        elif bandera == 0:
            return "Elemento no encontrado en la lista"
    # ---------------------------------------------
    def llevarAUltimo(self):
        while self.nodoActual.siguiente is not None:
            self.nodoActual = self.nodoActual.siguiente

    # ---------------------------------------------
    def informacionPorIndice(self, index):
        tamañoTmp = self.tamañoLista()
        if index < tamañoTmp:
            contadorTmp = 0
            self.nodoActual = self.cabeceraNodo
            while self.nodoActual is not None:
                if contadorTmp == index:
                    informacionTmp = self.nodoActual.informacion
                    self.llevarAUltimo()
                    return informacionTmp
                self.nodoActual = self.nodoActual.siguiente
                contadorTmp += 1
        else:
            return "Indice {} fuera de rango, el tamaño de la lista es {}".format(index, tamañoTmp)
    # ---------------------------------------------
    def imprimirMedio(self):
        tamañoTmp = self.tamañoLista()
        if tamañoTmp%2 == 0:
            indiceMitad = tamañoTmp/2
            return self.informacionPorIndice(indiceMitad)
        else:
            indiceMitad = tamañoTmp//2
            return self.informacionPorIndice(indiceMitad)

    def __str__(self):
        if self.cabeceraNodo is None:
            return "HEAD --> {:<2} --> NULL".format(self.cabeceraNodo)
        else:
            return "HEAD --> {:<2} --> {:<2} --> ... {:^2} ... --> {:>2} --> NULL".format(self.cabeceraNodo.informacion,
                                                                        self.cabeceraNodo.siguiente.informacion,
                                                                        self.imprimirMedio(),
                                                                        self.nodoActual.informacion)