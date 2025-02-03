num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

soma = num1 + num2
multi = num1 * num2
div = num1 / num2
divin = num1 // num2
exp = num1 ** num2

print('A soma dos valores é de {} \nA multiplicação é de {} \nA divisão é de {:.2f}\n'.format(soma,multi,div), end='')
print('A divisão inteira é de {}\nA potência é de {}'.format(divin,exp))