# Ler a altura e largura
alt = float(input('Insira a Altura em Metros \nAltura: '))
lar = float(input('Insira a Largura em Metros \nLargura: '))

# calculo da area
area = alt * lar

# calculo da qntd de tinta 1==2m2
qntd = area / 2

# quantidad de tinta necessária 
print('Você precisará de {:.2f}lts de tinta para pintar {:.2f}m²'.format(qntd,area))