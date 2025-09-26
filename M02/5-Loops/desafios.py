# FOR 001
""" for i in range(1, 11): 
  print (f"Contador: {i}") """

# FOR 002
""" print('========================= TABUADA =========================')
number = int(input('Insira um número: '))

for i in range(1, 11):
  total = number * i
  print(f'{number} X {i} = {total}')

print('========================= TABUADA =========================') """

# FOR 003
""" num = 0

for i in range(2, 101, 2):
  num += i

print(f'O resultado da soma dos números de 1 a 100 é {num}!') """

# WHILE 001
index = 10

while index > 0:
  print(index)
  index -= 1

print('Lançar foguete!')

# WHILE 002 
password = input('Insira a sua senha: ')

while password != '1234':
  password = input('Senha incorreta, digite-a novamente: ')

print('Seja bem-vindo(a)!')

# WHILE 003
numberSum = 0

while numberSum <= 100:
  number = int(input('Insira um número: '))
  numberSum += number
  print(f'Valor atual: {numberSum}')

print(f'Valor da soma dos números digitados: {numberSum}!')
