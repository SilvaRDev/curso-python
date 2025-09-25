nomeDoProduto = input('Insira o nome do produto ')
preco = int(input('Insira o valor do produto: '))
desconto = int(input('Insira a porcentagem de desconto: '))

novoPreco = preco - preco * desconto / 100
print(f"O produto '{nomeDoProduto}' com o desconto aplicado, passará de R${preco} para o novo valor de R${novoPreco}")
