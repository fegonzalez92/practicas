class Perro():
    """un simple intento de modelar un perro"""
    def __init__(self, nombre, edad): #funcion constructora 
        """inicializa los atributos nombre y edad"""
        self.nombre = nombre
        self.edad = edad

    def sentar (self):
        """simular que el pero se sienta en base a una ordem"""
        print(self.nombre.title() + "esta sentado")

    def rodar(self):
        """simular que el perro esta rodando"""
        print(self.nombre.title() + "esta rodando")

mi_perro = Perro("willi", 6)  #instancio una clase = creo un objeto a traver de un atributo

print("mi perro se llama" + mi_perro.nombre.title())
print("mi perro tiene" + str(mi_perro.edad) + "años")

edad = mi_perro.edad #accedo a un atributo
print(edad)
mi_perro.rodar()
mi_perro.sentar()