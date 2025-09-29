class Animal:
  def __init__(self, nome, cor, especie):
    self.nome = nome 
    self.cor = cor 
    self.especie = especie

  def apresentar(self):
    print(f'Eu sou um(a) {self.especie} chamado(a) {self.nome}!')

class Gato(Animal):
  def emitirSom(self):
    print('Miau')

  def arranhar(self):
    print('O gato está arranhando!')

class Cachorro(Animal):
  def emitirSom(self):
    print('Au Au!')

class Elefante(Animal):
  def emitirSom(self):
    print('Ffuuuuuuuu')

gato1 = Gato('Felix', 'Branco', 'Siamese')
gato1.apresentar()
gato1.emitirSom()
gato1.arranhar()

cachorro1 = Cachorro('Bob', 'Caramelo', 'Vira-Lata')
cachorro1.apresentar()
cachorro1.emitirSom()

cachorro2 = Cachorro('Spike', 'Preto', 'Bull terrier')
cachorro2.apresentar()

elefante1 = Elefante('Dumbo', 'Cinza', 'Elefante Asiático')
elefante1.apresentar()
elefante1.emitirSom()
