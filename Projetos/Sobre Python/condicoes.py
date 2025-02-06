"""
if algo.acontecer():   se
    bloco True
else:
    bloco False        senão
"""

tempo = int(input('Quantos anos tem o seu carro? \nDigite aqui: '))

if tempo <= 3:
    print('Seu carro é novinho!!!')
else:
    print('Seu carro ja está velho. :(')
print('fim')

# print('carro novo' if tempo<=3 else 'carro velho') simplificado 