#bifurcaciones son if o else
print("bienvenido a mi programa") #mensaje de bienvenida en el inicion del programa
url=input("ingrese una url: ") #se usa para escribir el programa al cual queres acceder copiando la url(http o https)
if url.startswith("https"): #lo que quiero que lea
    print("su pagina es segura")
else:
    print("la pagina no es segura")
print("fin del programa")
#si if se cumple manda el mensaje que es segura y imprime el mesaje y termina con el fin del programa, pero si no es segura directamente pasa a no es segura y fin del programa
#hay que respetar las lineas a la hora de escribir 
#si queres mas de 2 alternativas en el caso de por ejemplo que no es segura a es casi segura se le agrega elif y si son 4 se sigue agregando con elif: if, elif, elif,.., else
#////////////////////////////////////
print("bienvenido a mi programa")
edad=int(input("ingrese edad: "))
if edad >=40:
    print("usted es adulto")
elif edad >=30:
    print("usted es viejo")
else:
     print("usted es menor")
    
print(edad)

#SIEMPRE EN EL IF VOY A PONER EL VALOR MAS ALTO PARA PODER USAR BIEN LOS ELIF Y TERMINA CON ELSE SI QUIERO PONER UNA NEGACION MENOR COMO EN ESE EJEMPLO QUE HICE RECIEN
#format se usa{} y si ponemos {:20} en una tabla es que va a tener 20 cm para la derecha y si ponemos < es que va para la derecha porque el pico marca el sentido
#random exporta la lista por defecto que tiene el lenguaje y randing devuelve un numero entero aleatorio
#== es de comparacion
#!= es diferente
#+= es un valor de asignacion y el resultado lo almacena en una variable