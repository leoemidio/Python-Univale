class Carro:
    pneu = 4 # atributo #

    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo

carro01 = Carro ("Toyota", "hilux") # objeto que foi instanciado
carro02 = Carro ("Vw", "gol") 

print(carro01.modelo)
print(carro02.modelo)
