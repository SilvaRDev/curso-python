""" nome = 'Rafael'
idade = 19
altura = 1.80
mensagem = 'Olá, mundo!'
programador = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(mensagem))
print(type(programador)) """

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

"""frutaFavorita = input('Qual é a sua fruta favorita? ')

# f-string
print(f"Seu nome é {nome}, e você tem {idade} anos de idade, e a sua fruta favorita é {frutaFavorita}!") """

print(f"Olá, {nome}! Daqui 5 anos você terá {int(idade) + 5} anos de idade.")
