class Animal:
    def __init__ (self, nome, cor, especie, tamanho, genero):
     print("Criando animal ... {}", format(self))
     self.nome = nome
     self.cor = cor
     self.especie = especie
     self.tamanho = tamanho
     self.genero = genero

    def apresentar(self):
      print("Seu animal é um:",self.especie, self.genero, "com o nome de", self.nome, "de cor", self.cor)
    def andar(self):
        print("Andando...")
    def correr(self):
        print("Correndo...")
    def comer(self):
        print("Comendo...")
