class Pessoa:
  def __init__(self, nome, idade, cargo):
    self.nome = nome 
    self.idade = idade 
    self.cargo = cargo

  def informacoes(self):
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.idade}')
    print(f'Cargo: {self.cargo}\n')

  def promover(self, novoCargo):
    print(f'{self.nome} foi promovido(a) para a nova função de {novoCargo}')

  def atualizarIdade(self, novaIdade):
    if novaIdade > self.idade:
      print(f'Atualizando a idade de: {self.idade} para: {novaIdade}.')
    else:
      print('A nova idade tem que ser maior que a antiga.')


colaborador1 = Pessoa('João', 26, 'Programador júnior')
colaborador2 = Pessoa('Alana', 23, 'Assistente Júnior')
colaborador3 = Pessoa('Carlos', 42, 'Dev Sênior')

colaborador1.informacoes()
colaborador1.promover('Programador Pleno')
colaborador1.atualizarIdade(27)

colaborador2.informacoes()

colaborador3.informacoes()