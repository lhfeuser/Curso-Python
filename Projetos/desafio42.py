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
    if r1 == r2 and r1 == r3:
        print('Você tem um triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Você tem um triângulo Isósceles')
    else:
        print('Você tem um triângulo Escaleno')
else:
    print('Os segmentos acima não podem formar um triângulo')
