# Recebe a distância em km
dis = int(input('Qual a Distância da Sua Viagem em Km \nDistância: '))
# Condições
if dis - 200 > 0:
    print('Sua Passagem Custará R${:.2f}'.format(dis*0.45))
else:
    print('Sua Passagem Custará R${:.2f}'.format(dis*0.50))
