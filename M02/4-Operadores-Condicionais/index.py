""" numero = int(input('Digite um número: '))

if numero == 10:
  print('Você acertou o número!')
else:
  print('Você errou o número. Tente novamente!') """

""" age = int(input('Insira a sua idade: '))

if age >= 18: 
  print('Maior de idade')
else: 
  print('Menor de idade') """

""" note = float(input('Insira a sua nota: '))

if note >= 7:
  print('Você foi aprovado!')
elif note >= 5 and note < 7: 
  print('Você está na recuperação. ')
else: 
  print('Você foi reprovado.') """

""" user = input('Insira o seu usuário: ')
password = input('Insira a sua senha: ')

if user == 'Admin' and password == '1234Teste':
  print('Seja bem-vindo(a)!')
else: 
  print('Usuário e/ou senha inválido(s)') """

age = int(input('Insira a sua idade: '))

if age >= 18:
  print('SUCESSO: Liberado com sucesso!')
elif age >= 16 and age < 18:
  parentAuthorization = input('Você tem autorização dos pais para entrar(s/n)? ')
  if parentAuthorization == 's':  
    print('SUCESSO: Liberado com autorização dos pais!')
  else: 
    print('ERRO: Não autorizado.')
else: 
  print('ERRO: Não autorizado (Menor de idade)')

