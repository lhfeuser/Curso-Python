# Recebe o tamanho das retas
print('--'*17)
r1 = int(input('Insira o Valor da Primeira Reta \nValor: '))
print('--'*17)
r2 = int(input('Insira o Valor da Segunda Reta \nValor: '))
print('--'*17)
r3 = int(input('Insira o Valor da Terceira Reta \nValor: '))
print('--'*17)
# Condições
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Parabéns!!! Você tem um Retângulo!!')
print('Os segmentos acima não podem formar um triângulo')