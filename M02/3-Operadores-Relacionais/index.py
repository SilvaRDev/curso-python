""" age = int(input('Insira a sua idade: '))
carteira = True
verifyAge = age >= 18 and carteira == True

print(verifyAge) """

user = input('Insira o seu usuário: ')
password = input('Insira a sua senha: ')
verifiedUser = user == 'Admin' and password == '1234Teste' 

print(f"Usuário autenticado: {verifiedUser}")
