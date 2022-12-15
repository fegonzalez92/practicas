#se puede ejecutar el codigo desde donde quiera de un def, tengo que hacer click derecho y seleccionar ejecutar el archivo de phyton en terminal
def mensaje ():
    print("hola loco")
#de esta manera se imprime el mensaje que queres mostrar 
mensaje()

def mensaje2(nombre):
    print("bienvenido", nombre)
#de esta manera permito que se genere un parametro para que se pueda ingresar un nombre y de el mesaje
cad=input("ingrese su nombre: ")
mensaje2(cad)
#ahora vamos a hacer para que vuelva a iniciar el programa
def mensaje3(nombre):
    cadena="bienvenido" + nombre
    return cadena

nom=input("ingrese su nombre:" )
cadenaretorno=mensaje3(nom)
print(cadenaretorno)

#creo un contador y que sume de a 1 el resultado 
def lenN(cadena):
    cont=0
    for caract in cadena:
        cont+=1
    return cont
producto="cafe"
cuantos= lenN(producto)
print(cuantos)

#me convierte en entero a los numero pero error si ingreso una letra
def validar_numero_a_brevedad(cadena):
    while not cadena.isdigit():
        cadena=input("error, ingrese un numeor: ")
    return int(cadena)

cadena=input("ingrese un numero:")
numero=validar_numero_a_brevedad(cadena)
print(numero)