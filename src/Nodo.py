"""
Author: Juan Camilo Moná Luján
Fecha: 31 - 08 - 2023
"""

class Nodo:
    def __init__(self, inf):
        self._informacion = inf
        self._siguiente = None
    # ----- GETTERS Y SETTERS DE LA CLASE ------
    @property
    def informacion(self):
        return self._informacion

    @informacion.setter
    def informacion(self, inf):
        self._informacion = inf

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        self._siguiente = nodo




