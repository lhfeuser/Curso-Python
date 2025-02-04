# Importação das bibliotecas
from math import floor

# Inserir um número para saber sua parte inteira
num = float(input('Insira um número para saber sua parte inteira \nInsira o número: '))

#Fazendo a parte inteira
inteiro = floor(num)

# Mostrando a parte inteira
print('A parte inteira de {} é {}'.format(num,inteiro))
