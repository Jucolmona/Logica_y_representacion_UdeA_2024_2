def testListaLigadaSimple():
    from ListaLigadaSimple import LLS
    testLista = LLS("valor 1")
    datos = ("Valor 2", "Valor 3", "Valor 4", "Valor 5", "Valor 6", "Valor 7", "Valor 8", "Valor 9", "Valor 10")
    for dato in datos:
        testLista.insertar(dato)

    print(testLista.primerNodo.informacion)
    print(id(testLista.primerNodo))

    testLista.imprimirLista()

    print('-------------- TEST INSERTAR PRIMERO -----------------')
    testLista.insertarPrimero("valor 11")
    print("Despues de insertar primero")
    testLista.imprimirLista()
    print('-------------- TEST INSERTAR DESPUES -----------------')
    testLista.insertarDespues("Valor K", 5)
    print("Despues de insertar en medio")
    testLista.imprimirLista()

    print('-------------- TEST TAMAÑO DE LSITA -----------------')
    print(testLista.tamanoLista())    # print(testLista)

    print('-------------- TEST NODO POR INDICE -----------------')
    print(testLista.nodoPorIndice(5))

    print('-------------- TEST VALIDAR NODO -----------------')
    print(testLista.validarNodo("Valor 7"))
    print(testLista.validarNodo("Valor 11"))

    print('-------------- TEST IMPRIMIR INDICE -----------------')
    print(testLista.imprimirIndex("Valor 7"))

    print('-------------- TEST INFORMACION POR INDICE -----------------')
    print(testLista.informacionPorIndice(5))
    print(testLista.informacionPorIndice(15))

def testListaLigadaDoble(datosEntrada):
    from ListaLigadaDoble import LLD

    Lld_test = LLD("Primero")
    for dato in datosEntrada:
        Lld_test.insertarFinal(dato)
    Lld_test.imprimirListaAdelante()
    Lld_test.imprimirListaAtras()


#datosEntrada = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")
#testListaLigadaDoble(datosEntrada)
testListaLigadaSimple()

