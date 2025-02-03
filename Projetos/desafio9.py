num = int(input('Insira um número para receber a tabuada: '))

zero = num * 0
um = num * 1
dois = num * 2 
tres = num * 3
quatro = num * 4
cinco = num * 5
seis = num * 6
sete = num * 7
oito = num * 7
nove = num * 9
dez = num * 10

print('|{} x 0 = {}|\n|{} x 1 = {}|\n|{} x 2 = {}|\n|{} x 3 = {}|\n'.format(num,zero,num,um,num,dois,num,tres),end='')

print('|{} x 4 = {}|\n|{} x 5 = {}|\n|{} x 6 = {}|\n|{} x 7 = {}|\n'.format(num,quatro,num,cinco,num,seis,num,sete), end='')

print('|{} x 8 = {}|\n|{} x 9 = {}|\n|{} x 10 = {}|'.format(num,oito,num,nove,num,dez), end='')