mip = 0
mnp = 1000000
# Recebe os pesos
for p in range(1,6):
    peso = float(input('Insira o peso \nPeso: '))
    if mip < peso:
        mip = peso
    elif mnp > peso:
        mnp = peso
print('O menor peso é de {:.2f}Kg e o maior é de {:.2f}Kg'.format(mnp,mip))
