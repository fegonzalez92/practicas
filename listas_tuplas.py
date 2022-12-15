#crear una lista
mi_list=("buenos aires","neuquen","bariloche","asuncion","brasil")

#imprimir pantalla de lista el segundo elemento
mi_list=("buenos aires","neuquen","bariloche","asuncion","brasil")
print(mi_list[1])

#imprimir en pantalla de la lista del segundo al cuarto
mi_list=("buenos aires","neuquen","bariloche","asuncion","brasil")
print(mi_list[1:4])

#visualizar la lista
print(mi_list=("buenos aires","neuquen","bariloche","asuncion","brasil"))

#visualizar datos de la lista
print(type(mi_list))

#visualizar la lista del 2 para delante de forma generica
mi_list=("buenos aires","neuquen","bariloche","asuncion","brasil")
print(mi_list[1:])

#visualizar la lista los primeros 4 elementos de la lista
mi_list=("buenos aires","neuquen","bariloche","asuncion","brasil")
print(mi_list[:4])

#agregar ciudad a la lista
mi_list.append("cordoba")
print(mi_list)

#la lista si acepta duplicados y los agrega a los 2 en la lista(mi_list o lista es lo mismo solo que lo escribi de distinta forma)
mi_list.append("cordoba")
print(mi_list)

#eliminar un elemento de la lista (ciudad de la lista quiere decir)
mi_list.remove("buenos aires")
print(mi_list)

#agregar otro elemento en la lista
mi_list.insert(3,"quito")
print(mi_list)

#unir una lista a mi lista actual, los corchetes se usa para aclarar que estoy usando otra lista
mi_list.extend(["mexico","españa","peru"])

#buscar la ciudad agregada en este caso cordoba
mi_list.index("cordoba")
print(mi_list)

#en el caso de que busquemos un elemento que no esta en la lista se hace de la misma manera pero va a tirar error

#eliminar el ultimo elemento de la lista y guardarlo en una variable e imprimirlo
ultimo = mi_list.pop()
print(ultimo)
#despues imprimimos a lista para comprobar que no este mas y ya estaria guardada en una variable e imprimido
print(mi_list)

#lista multiplicada por 4
print(mi_list*4)

elemento = "paris"
#hacemos si no esta elemento en la lista debe mostrar el mensaje que esta dentro del print.
if not (elemento in lista):
    mi_list.append(elemento)
    print("se inserto el elemento", elemento)
#esto es si llega a esta el elemento debe mostrar el mensaje que esta dentro del print
else:
    print("el elemento", elemento, "ya se encuentra en la lista")

#para saber cuantas veces se repite un numero en una tupla, como ejemplo el numero 10 de cuantas veces se repite 10 en la lista

print(tupla.count(10))

#para convertir la tupla en una lista 
lista=list(tupla)
print(lista)

#para saber que tipo de texto es
type(lista)

#la tupla se crea asi
tupla = (1,2,3,4,5)

#creando un diccionario

lista = []
tupla = ()
diccionario = {key:values}

#creo una funcion que extrae primos de una lista
def extrae_primos_de_lista(lista):
    lista_primos=[]
    for elemento in lista:
        if verifica_primo(int(elemento)):
            lista_primos.append(elemento)
    return lista_primos

