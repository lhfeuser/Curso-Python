# le o número 
num = int(input('Insira qualquer número inteiro inteiro entre 0 e 9999 \nNº: '))
# Contas
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
# print
print('Unidade: {} \nDezana: {} \nCentena: {} \nMilhar: {}'.format(u,d,c,m))
