# quantidade de km rodados 
km = float(input('Quantos Km você rodou com o carro? \nKm: '))

# Dias alugados tendo em vista que o dia custa 60R$
dia = int(input('Por quantos dias você alugou o carro? \nDias: '))

#Calculo de valores tendo em vista que o dia custa 60R$ e o Km rodado custa 0,15R$
custo = dia * 60 + km * 0.15

#Valor a ser pago
print('O valor a ser pago pelo carro é de R${:.2f}'.format(custo))