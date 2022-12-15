import random as rd
palabras=["Capuchino","Cafe","Oreo","Palabras","Helado"]
indice=rd.randint(0,len(palabras)-1) #0,1,2,3,4.. rl -1 es para que reste una palabra y me de 4 y no 5
pal=palabras[indice]
palMayus=pal.upper() #upper hace que la palabra se vea en mayuscula
letraPri=palMayus[0] # marca cual es la primer posicion de la palabra 
letraUlt=palMayus[-1] #marca la ultima letra y se usa el -1 porque si pongo 5 si son 5 ejemplos en el punto 2 me va a marcar 6 palabras y son solo 5 por eso se usa el -1
n=len(palMayus)-2
subGuio=n * " _ " #esto multiplica la cantidad de espacios y se usa " _ " asi separado porque sino van a salir pegados los _
pista= letraPri + subGuio + letraUlt #armo la escuacion
print(pista) 
palUser=input("Adivine la palabra: ").upper()
cond= palUser == palMayus
print("gano?: ",cond)
