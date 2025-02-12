n = int(input('Qual Tabuada Você Deseja \nNúmero: '))

for tab in range(0,11):
    print('|{} x {} = {} |'.format(tab, n, (tab*n)))