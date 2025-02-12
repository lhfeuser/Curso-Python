termo = int(input('Insira o primeiro termo da PA \nTermo: '))
razão = int(input('Insira a razão da PA \nRazão: '))
decimo = termo + (10 -1) * razão
# Mostra a PA
for pa in range(termo, decimo + razão, razão):
       print('{} '.format(pa), end = ' - ')
print('FIM')
        