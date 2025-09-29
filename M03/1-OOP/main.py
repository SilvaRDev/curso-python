class Casa: 
  def __init__(self, cor, quartos, banheiros):
    self.cor = cor 
    self.quartos = quartos
    self.banheiros = banheiros

  def mostrarCor(self):
    print(f'A cor da casa é: {self.cor}')

  def mostrarQuartos(self):
    print(f'Esta casa tem {self.quartos} quartos.')

  def mostrarBanheiros(self): 
    print(f'Esta casa tem {self.banheiros} banheiros.')

  def adicionarQuarto(self):
    self.quartos += 1
    print(f'Esta casa tem {self.quartos} quartos.')

  def pintarCasa(self, novaCor):
    print(f'Pintando a casa de {self.cor} para {novaCor}')
    self.cor = novaCor

casa1 = Casa('Azul', 3, 4)
casa2 = Casa('Amarela', 2, 3)

print('Casa 1:')
casa1.mostrarCor()
casa1.mostrarQuartos()
casa1.mostrarBanheiros()
casa1.adicionarQuarto()
casa1.pintarCasa('Marrom')
casa1.mostrarCor()

print('\nCasa 2:')
casa2.mostrarCor()
casa2.mostrarQuartos()
casa2.mostrarBanheiros()
casa2.adicionarQuarto()
