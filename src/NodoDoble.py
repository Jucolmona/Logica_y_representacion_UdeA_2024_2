class Nodo:
    def __init__(self,inf):
        self._informacion = inf
        self._anterior = None
        self._siguiente = None

    @property
    def informacion(self):
        return self._informacion

    @informacion.setter
    def informacion(self, inf):
        self._informacion = inf

    @property
    def anterior(self):
        return self._anterior

    @anterior.setter
    def anterior(self, nodo):
        self._anterior = nodo

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        self._siguiente = nodo

    def __str__(self):
        return ("ND --> [ INFORMACION: {:>5} \n  {:>17}{:>7} \n {:>19}{:>6} ]").format(self.informacion,
                                                                                        "ANTERIOR: ", str(self.anterior),
                                                                                         "SIGUIENTE: ", str(self.siguiente))