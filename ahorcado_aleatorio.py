import random as rd
palabras=["Capuchino","Cafe","Oreo","Palabras","Helado"]
pal=rd.choice(palabras)
palMayus=pal.upper()
indice=rd.randint(0,len(palMayus)-1)
letra=palMayus[indice]
nPri=len(palMayus[:indice])
nUlt=len(palMayus[indice+1:])
pista=(nPri * " _ ") + letra + (nUlt * " _ ")
print(pista)
palUser=input("Adivine la palabra: ").upper()
cond= palUser == palMayus
print("gano?: ",cond)