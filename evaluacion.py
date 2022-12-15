def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,2),(4,1)]
    '''
    #Tu código aca:
    if not (type(lista) is list):
        return None
    
    frequencyCounter = {}
    
    for i in lista:
        key = ""
        if isinstance(i, int):
            key = i

        elif isinstance(i, int):
            key = str(i)
        if key in frequencyCounter.keys():
            frequencyCounter[key] += 1
        else:
            frequencyCounter[key] = 1
    newArr = []
    for key in frequencyCounter.keys():
        if key.isdigit():
            newTupple = (int(key), frequencyCounter[key])
        else:
            newTupple = (key, frequencyCounter[key])
            newArr.append(newTupple)
    return newArr