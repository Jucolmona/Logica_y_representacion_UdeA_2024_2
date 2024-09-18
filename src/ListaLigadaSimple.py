"""
Author: Juan Camilo Moná Luján
Fecha: 01 - 09 - 2024
"""

from Nodo import Nodo

class LLS:

    def __init__(self, val):
        self._primerNodo = Nodo(val)
        self._nodoActual = None

    # ----- GETTERS Y SETTERS DE LA CLASE ------
    @property
    def primerNodo(self):
        return self._primerNodo

    @primerNodo.setter
    def primerNodo(self, val):
        self._primerNodo = val

    @property
    def nodoActual(self):
        return self._nodoActual

    @nodoActual.setter
    def nodoActual(self, nodo):
        self._nodoActual = nodo

    # ------- MÉTODOS PROPIOS DE LA CLASE ---------
    # ---------------------------------------------
    # ---------- MÉTODOS AUXILIARES ---------------
    # ---------------------------------------------
    def recorrerLista(self):
        """
        Este método ayua a llevar el nodo actual, hasta el último nodo
        :return:
                no retorna ningún valor, solo cambia el estado del objeto
        """
        while self.nodoActual.siguiente is not None:
            self.nodoActual = self.nodoActual.siguiente

    # ---------------------------------------------
    def tamanoLista(self):
        self.nodoActual = self.primerNodo
        contadorTmp = 0
        if self.nodoActual is None:
            return contadorTmp
        while self.nodoActual.siguiente is not None:
            self.nodoActual = self.nodoActual.siguiente
            contadorTmp += 1
        return contadorTmp

    # ---------------------------------------------
    def nodoPorIndice(self, index):
        """
        Recorre la lista hasta encontrar el nodo que se encuentra en la posición dada por
        el parámetro index, en caso de que el indice dado no exceda el tamaño de
        la lista.
        :param index:
                    variable de tipo entero que representa la posición o indice del
                    nodo que se quiere recuperar.
        :return:
                retorna un nodo que es el que se encuentra en la posición indicada por el
        """
        if index < self.tamanoLista():
            contadorTmp = 0
            self.nodoActual = self.primerNodo
            while self.nodoActual is not None:
                if contadorTmp == index:
                    nodoTmp = self.nodoActual
                    self.recorrerLista()
                    return nodoTmp
                self.nodoActual = self.nodoActual.siguiente
                contadorTmp += 1
        else:
            return "Indice {} fuera de rango, el tamaño de la lista es {}".format(index, self.tamanoLista())

    # ---------------------------------------------
    # ---------- PROCESAMIENTO DE LLS -------------
    # ---------------------------------------------
    def insertar(self, val):
        '''
        Se inserta un nuevo elemento o dato en la Lista Ligada Simple.
        Por defecto se insertan los elementos despues del último nodo.

        :param val: datos que serán insertados en Lista Ligada Simple (LLS)
        :return: void()
        '''
        nodoTmp = Nodo(val)
        if self.primerNodo.siguiente is None:
            self.primerNodo.siguiente = nodoTmp
            self.nodoActual = nodoTmp
            return
        self.nodoActual = self.primerNodo
        self.recorrerLista()
        self.nodoActual.siguiente = nodoTmp
        self.nodoActual = nodoTmp
        print("Se ha insertado correctamente el nodo {}".format(self.nodoActual))

    # ---------------------------------------------
    def insertarPrimero(self, val):
        nodoTmp = Nodo(val)
        nodoTmp.siguiente = self.primerNodo
        self.primerNodo = nodoTmp
        print("Se ha actualizado correctamente el primer nodo del nodo: {}".format(nodoTmp))


    # ---------------------------------------------
    def insertarDespues(self, val, index):
        """
         Inserta elementos de la lista (nodos) despues de un elemento dado.
        :param val:
                    información que se guardar en el nuevo nodo que se va a insertar
        :param index:
                    indice del nodo el cual apuntará hacia el nuevo nodo
        :return:
        """
        nodoDado = self.nodoPorIndice(index)
        nodoTmp = Nodo(val)
        self.nodoActual = self.primerNodo
        if self.nodoActual.siguiente is None:
            self.nodoActual.siguiente = nodoTmp
            self.nodoActual = nodoTmp
            return
        while self.nodoActual.siguiente is not None:
            if self.nodoActual is nodoDado:
                refNodoTmp = self.nodoActual.siguiente
                self.nodoActual.siguiente = nodoTmp
                self.nodoActual = self.nodoActual.siguiente
                self.nodoActual.siguiente = refNodoTmp
                return
            self.nodoActual = self.nodoActual.siguiente


    # ---------------------------------------------
    def imprimirLista(self):
        self.nodoActual = self.primerNodo
        print('|{:<10} | {:<15}|'.format('VALOR', 'LIGAS'))
        while self.nodoActual.siguiente is not None:
            print('|{:<10} | {:<10}|'.format(self.nodoActual.informacion, id(self.nodoActual.siguiente)))
            self.nodoActual = self.nodoActual.siguiente

    # ---------------------------------------------
    def validarNodo(self, val):
        """
        Función que verifica si el nodo se encuentra dentro de la lista ligada
        según la información dada que recibe la función
        :param val:
                    parametro que pasa la información que se desea validar y la cual se
                    quiere corroborar para ver si se está en el nodo
        :return:
                se retorna un valor de tipo entero y binario que indica si la información
                y por tanto el nodo de la lista se encuentra (1) o no (0)
        """
        self.nodoActual = self.primerNodo
        contadorTmp = 0
        if self.nodoActual.siguiente is None:
            if self.nodoActual.informacion == val:
                print("Información encontrada en cabecera")
                return 1
            else:
                print("Lista vacia, no se encuentra información")
                return 0
        while self.nodoActual.siguiente is not None:
            if self.nodoActual.informacion == val:
                return 1
            self.nodoActual = self.nodoActual.siguiente
            contadorTmp += 1
        return 0


    # ---------------------------------------------
    def imprimirIndex(self, val):
        """
        Imprime el indice de la lista según el valor o la información del nodo dado
        :param val:
                    información contenida dentro de un nodo de la lista y del cual se
                    quiere recuperar el indice.
        :return:
                    retorna un valor de tipo entero que indica la posicion del nodo que
                    contiene la información dada
        """
        bandera = self.validarNodo(val)
        if bandera == 1:
            contadorTmp = 0
            self.nodoActual = self.primerNodo
            while self.nodoActual.siguiente is not None:
                if self.nodoActual.informacion == val:
                    return contadorTmp
                self.nodoActual = self.nodoActual.siguiente
                contadorTmp += 1
        elif bandera == 0:
            return "Elemento no encontrado en la lista"


    # ---------------------------------------------
    def informacionPorIndice(self, index):
        """
        Imprime la información del nodo que se encuentra en la posición dada por
        el parámetro index, en caso de que el indice dado no exceda el tamaño de
        la lista.
        :param index:
                    variable de tipo entero que representa la posición o indice del
                    nodo que se quiere recuperar.
        :return:
                retorna la información contenida dentro del nodo que se posiciona
                según el indice pasado a la función.
        """
        tamanoTmp = self.tamanoLista()
        if index < tamanoTmp:
            contadorTmp = 0
            self.nodoActual = self.primerNodo
            while self.nodoActual is not None:
                if contadorTmp == index:
                    informacionTmp = self.nodoActual.informacion
                    self.recorrerLista()
                    return informacionTmp
                self.nodoActual = self.nodoActual.siguiente
                contadorTmp += 1
        else:
            return "Indice {} fuera de rango, el tamaño de la lista es {}".format(index, tamanoTmp)


    # ---------------------------------------------
    def imprimirMedio(self):
        tamanoTmp = self.tamanoLista()
        if tamanoTmp%2 == 0:
            indiceMitad = tamanoTmp/2
            return self.informacionPorIndice(indiceMitad)
        else:
            indiceMitad = tamanoTmp//2
            return self.informacionPorIndice(indiceMitad)


    # ---------------------------------------------
    def __str__(self):
        if self.cabeceraNodo is None:
            return "HEAD --> {:<2} --> NULL".format(self.primerNodo)
        else:
            return "HEAD --> {:<2} --> {:<2} --> ... {:^2} ... --> {:>2} --> NULL".format(self.primerNodo.informacion,
                                                                        self.primerNodo.siguiente.informacion,
                                                                        self.imprimirMedio(),
                                                                        self.nodoActual.informacion)