# Recebe valor e forma de pagamento
valor = float(input('Informe o valor do produto \nValor: '))
print('=-'*15)
print('Dinheiro/Cheque = D \nCartão à Vista = CA \n2x Cartão = CP \n3x ou + = CM')
print('=-'*15)
pag = str(input('Informe a forma de Pagamento \nPagemento: ')).upper().strip()
print('=-'*15)
des = 0
# condições
if pag == 'D':
    des = valor - (valor * 0.10)
    print('O valor com desconto aplicado é de {:.2f}'.format(des))
elif pag == 'CA':
    des = valor - (valor * 0.05)
    print('O valor com desconto aplicado é {:.2f}'.format(des))
elif pag == 'CP':
    print('Esse método de pagamento não possui desconto, valor a pagar {:.2f}'.format(valor))
elif pag == 'CM':
    des = valor + (valor * 0.20)
    print('O valor a pagar é de R${:.2f} e teve um total de R${:.2f} juros aplicados'.format(des,(valor*0.20)))
print('=-'*15)