""" def greeting(name, age):
  print(f'Olá, {name}! Você tem {age} anos de idade.')

greeting('João', 19) """

""" def sum(n1, n2):
  return n1 + n2

result = sum(2, 5)

print(f'O resultado da soma é de: {result}') """

def calculateDiscount(value, percentage):
  return value - (value * percentage / 100)

finalValue = calculateDiscount(1010, 25)
print(f"O valor final com desconto, é de R${finalValue:.2f}")
