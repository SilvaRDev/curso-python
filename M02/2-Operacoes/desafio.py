totalServings = int(input('Quantas porções o produto tem no total? '))
servingsPerDay = int(input('Quantas porções do produto você consome por dia? '))
productDuration = totalServings / servingsPerDay

print(f"O produto terá uma duração de {productDuration:.0f} dias.")
