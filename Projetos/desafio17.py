import math

# Inserir os catetos
ca = float(input('Insira o cateto adjacente. \nCateto: '))
print('--'*15)
co = float(input('Insira o cateto oposto. \nCateto: '))
print('--'*15)

#calculo da hipotenusa
hip = math.hypot(co,ca)

# Apresentando o resultado
print('O valor da hipotenusa é de {:.2f}'.format(hip))

# fiz desse jeito corrigido para o mostrado acima
"""
from math import sqrt,pow

# Inserir os catetos
ca = float(input('Insira o cateto adjacente. \nCateto: '))
print('--'*15)
co = float(input('Insira o cateto oposto. \nCateto: '))
print('--'*15)

# Calculo da Hipotenusa 
hip = sqrt(pow(ca, 2) + pow(co, 2))

# Apresentando o resultado
print('O valor da hipotenusa é de {}'.format(hip))
"""