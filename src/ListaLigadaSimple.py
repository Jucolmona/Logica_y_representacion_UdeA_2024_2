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
        """
        Función que verifica si el nodo se encuentra dentro de la lista ligada
        según la información dada que recibe la función
        :param val:
                    parametro que pasa la información que se desea validar y la cual se
                    quiere corroborar para ver si se encunetra dentro del nodo
        :return:
                se retorna un valor de tipo entero y binario que indica si la información
                y por tanto el nodo de la lista se encuentra (1) o no (0)
        """
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
        """
        Este método ayua a llevar el nodo actual, hasta el último nodo
        :return:
                no retorna ningún valor, solo cambia el estado del objeto
        """
        while self.nodoActual.siguiente is not None:
            self.nodoActual = self.nodoActual.siguiente
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
        tamañoTmp = self.tamañoLista()
        if index < tamañoTmp:
            contadorTmp = 0
            self.nodoActual = self.cabeceraNodo
            while self.nodoActual is not None:
                if contadorTmp == index:
                    nodoTmp = self.nodoActual
                    self.llevarAUltimo()
                    return nodoTmp
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
        self.nodoActual = self.cabeceraNodo
        if self.nodoActual is None:
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
    def __str__(self):
        if self.cabeceraNodo is None:
            return "HEAD --> {:<2} --> NULL".format(self.cabeceraNodo)
        else:
            return "HEAD --> {:<2} --> {:<2} --> ... {:^2} ... --> {:>2} --> NULL".format(self.cabeceraNodo.informacion,
                                                                        self.cabeceraNodo.siguiente.informacion,
                                                                        self.imprimirMedio(),
                                                                        self.nodoActual.informacion)