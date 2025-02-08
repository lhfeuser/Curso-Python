#recebe o valor do salário
sal = float(input('Insira o Valor do Salário \nSalário: R$'))
print('--'*10)
#condições
if sal <= 1250.50:
    print('Seu Salário Agora é de \nSalário: R${:.2f}'.format((sal*0.15)+sal))
    print('--'*10)
else:
    print('Seu Salário Agora é de \nSalário: R${:.2f}'.format((sal*0.10)+sal))
    print('--'*10)