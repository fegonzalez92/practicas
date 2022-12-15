import random as rd
billetera=10 #aca es el dinero que vas a tener para jugar como limite
gana=0 #aca va a ir el resultado para poder realizar el conteo de cuantas veces gano
continuar="si" #porque tiene que ser una confirmacion para poder tener un valor en el inicio
print("---bienvenido a mi juego---") #mensaje de inicio
print("usted tiene ${} en la billetera".format(billetera)) #nos muestra cuanto tiene en la billetera usando un format indicando que tiene una billetera {10}
while billetera>0 and continuar=="si": #el while hace que el siga el ciclo y siga el ciclo y asi..
    apuesta=int(input("ingrese su apuesta: ")) #indico con el int que es un numero entero y el mensaje para que indique el valor
    if apuesta <= billetera: 
        dado1=rd.randint(1,6)
        dado2=rd.randint(1,6)
        total=dado1+dado2
        resto=total%2
        parimpar=input("adivina es pa o impar?")
        print("salio: {} + {} = {}".format(dado1,dado2,total)) #muestra la cuenta que hizo para dar el resultado
        print("gano")
        billetera += apuesta
        gana+=1

    elif resto!=0 and parimpar=="impar":
            print("gano")
            billetera += apuesta
            gana+=1     
    else:
            print("perdio")
            billetera-=apuesta
            print("billetera: {}".format(billetera))
    if billetera!=0:
            continuar=input("desea seguir jugando?")
            print("--------------------------------")
    else:
        print("la apuesta es mayor al dinero que tiene en la billetera")
print("usted gano {} partidas".format(gana))
print("gracias por jugar")

#si tenes $10 en la billetera y seguis ganando no te va a contar mas que 10 porque ese es su maximo