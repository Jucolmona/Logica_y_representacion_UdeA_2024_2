def testListaLigadaSimple():
    from ListaLigadaSimple import ListaLigadaSimple
    testLista = ListaLigadaSimple("valor 1")
    testLista.insertar("Valor 2")
    testLista.insertar("Valor 3")
    testLista.insertar("Valor 4")
    testLista.insertar("Valor 5")
    testLista.insertar("Valor 6")
    testLista.insertar("Valor 7")
    testLista.insertar("Valor 8")
    testLista.insertar("Valor 9")
    testLista.insertar("Valor 10")

    print(testLista.cabeceraNodo.informacion)
    print(id(testLista.cabeceraNodo))

    testLista.imprimirLista()

    # testLista.nodoActual = testLista.cabeceraNodo
    # testLista.llevarAUltimo()
    # print(testLista.nodoActual)
    # print(testLista)
    testLista.insertarPrimero("valor 11")
    print("Despues de insertar primero")
    testLista.imprimirLista()
    testLista.insertarDespues("Valor K", 5)
    print("Despues de insertar en medio")
    testLista.imprimirLista()
    # print(testLista)
    # print(testLista.tamañoLista())
    # print(testLista.validarNodo("Valor 7"))
    # print(testLista.imprimirIndex("Valor 7"))
    # print(testLista.informacionPorIndice(5))

def testListaLigadaDoble(datosEntrada):
    from ListaLigadaDoble import LLD

    Lld_test = LLD("Primero")
    for dato in datosEntrada:
        Lld_test.insertarFinal(dato)
    Lld_test.imprimirListaAdelante()
    Lld_test.imprimirListaAtras()


datosEntrada = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")
testListaLigadaDoble(datosEntrada)


