# ler o valor do produto
valor = float(input('Insira o valor do produto \nValor: R$'))

# calculo do desconto 
dscnt = valor * 0.95

# valor de desconto obtido
qntddes = valor - dscnt

# apresentar valores
print('O valor com desconto aplicado é de R${:.2f} e o desconto foi de R${:.2f}'.format(dscnt,qntddes))