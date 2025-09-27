from functions import checkAgeOfMajority

age = int(input('Insira a sua idade: '))

if (checkAgeOfMajority(age)):
  print('Você é maior de idade.')
else:
  print('Você é menor de idade.')

