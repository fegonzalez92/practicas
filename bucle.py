print("hola")
n=7 #se puede hacer de esta manera tambien para agregar la cantidad de veces indicando en range(n)
for i in range(5): #for y despues el nombre que quiere en este caso puse "i" que va a ser el inicion del conteo en este ejemplo 0,1,2,3,4, despues es in range y dentro del parentesis es la cantidad de veces que quiero que se repita el mensaje en este caso 5
    print("nro. de repeticiones") #el mensaje que se va a repetir
print("fin")
for bolo in range(2):
    print("gracias totales")

#/////////
for n in range(10): #haciendo esto podemos extener la tabla numerica indicando que n va a retornar en 2,3,4,5,etc..
    n= int(input("ingrese un numero:" ))
    for i in range(10):
        resultado= i*n
        print(i,"x",n,"=",resultado) #aca defino lo que es la cuenta que va dentro del for, y las variables no llevan comillas como por ejemplo i, n, resultado.. el X(POR) Y = (EN LA CUENTA X Y =) si llevan comillas

#////////

for n in range(1,10): #haciendo esto podemos extener la tabla numerica indicando que n va a retornar en 2,3,4,5,etc..
    print("---tabla " + str(n) + "---") #con esto armamos una tabla ordenada
    for i in range(10):
        resultado= i*n
        print(i,"x",n,"=",resultado) #aca defino lo que es la cuenta que va dentro del for, y las variables no llevan comillas como por ejemplo i, n, resultado.. el X(POR) Y = (EN LA CUENTA X Y =) si llevan comillas

#///////
cadena = input("ingrese la palabra: ").lower() # el . lower hace que busque en el texto una palabra en mayuscula
for caracter in cadena: 
    if caracter in "aeoASd": #aca busca lo que quiero, que en este caso serian las vocales en mayuscula que ingrese 
        print(caracter)

#///
lista=["fede","lolo","helado"] #ingreso una lista que las listas se ingresa con []
for cadena in lista: # indico que es una cadena de una lista
    print("----" + cadena + "----") #quiero que se imprima el resultado de esta cuenta en forma de tabla
    for caracter in cadena:
        mini=caracter.lower()  # aca se usa mini que es miniscula para que se imprima tambien usando la formula de arriba y que se imprima el resultado
        if mini in "aeoas": # que se imprima si encuentra esto en la lista
            print(mini) #que se imprima
print("fin") #que termine el programa si termino de recorrer el programa

#////
frutas=["mora","frutas","mandarina","pera"]
for i in range(len(frutas)): #le digo que i es 0 y que cuente 
    print(frutas) #se imprima indicandome con enumeracion del 0 al 4 

#///
frutas=["mora","frutas","mandarina","pera"]
print("lista de compras")
for i in range(len(frutas)): #le digo que i es 0 y que cuente 
    fruta=frutas[i] #le indicio que sea por indice
    print(i,frutas) #y que lo imprime armandome una lista de compras por indice

#///
frutas=["mora","frutas","mandarina","pera"]
precioxlb=[0.50, 1.00, 2.00, 3.00]
print("lista de precio menor a 2.00")
for i in range(len(frutas)): #le digo que i es 0 y que cuente 
    fruta=frutas[i] #le indicio que sea por indice
    precio=precioxlb[i]
    if precio < 2.00:
        print(frutas) 

#///
frutas=["mora","frutas","mandarina","pera"]
precioxlb=[0.50, 1.00, 2.00, 3.00]
print("lista de precio menor a 2.00")
for fruta in frutas: #le digo que fruta es 0 y que busque la fruta
    pos=frutas.index(fruta) #le indicio que sea por posicion
    precio=precioxlb[pos]
    if precio < 2.00:
        print(frutas) 

#///
#si quiero buscar el cliente que compro la fruta en estos 3 ejemplos directamnte lo hago por la posicion
cliente=["kasd","frutas","mandarina","pera"]
cantidad=["2","3","5","10"]
fruta=["mora","jadja","sdasda","dasda"]
for fruta in frutas:
    pos=frutas.index(fruta) #el .index lo use para indicarle al programa que tiene que buscar
    if fruta=="mora": #indico que fruta es mora
        can=cantidad[pos] #digo que can es cantidad y le marco que busque la posicion con pos
        cli=cliente[pos] #lo mismo que dije arriba pero en vez de cantidad es ciente 
        print(cli,can)