class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome 
    self.idade = idade

  def apresentar(self):
    print(f'Olá! O meu nome é {self.nome}, e tenho {self.idade} anos de idade.')

class Funcionario(Pessoa):
  def __init__(self, nome, idade, cargo):
    super().__init__(nome, idade) # Puxa as informações da classe pai (Nesse caso, de Pessoa.)
    self.cargo = cargo 

  def trabalhar(self):
    print(f'{self.nome} está trabalhando como {self.cargo}.') 

class Cliente(Pessoa): 
  def __init__(self, nome, idade, saldo):
    super().__init__(nome, idade)
    self.saldo = saldo

  def comprar(self, valorCompra):
    if valorCompra <= self.saldo:
      self.saldo -= valorCompra 
      print(f'Olá, {self.nome}! Sua compra de R${valorCompra} foi aprovada.')
      print(f'Seu saldo atual é de R${self.saldo}.')
    else:
      print(f'Olá, {self.nome}! Saldo insuficiente.')

f1 = Funcionario('Maria', 38, 'Gerente de contas')
f1.trabalhar()

c1 = Cliente('Arthur', 16, 200)
# c1.apresentar()
c1.comprar(300)

c1 = Cliente('José', 46, 50)
c1.comprar(30)
