esc = 0

while esc != 5:
    v1 = float(input('\033[mInsira o Primeiro Valor \nValor: '))
    print('=-'*20)
    v2 = float(input('\033[mInsira o Segundo Valor \nValor: '))
    print('=-'*20)
    esc = int(input('\033[mO Que Você Deseja Fazer? \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair \nEscolha: '))
    print('=-'*20)
    
    if esc == 1:
        sm = v1 + v2
        print('\033[32mA Soma de {:.2f} e {:.2f} é de {:.2f}'.format(v1,v2,sm))
        print('=-'*20)
    elif esc == 2:
        mult = v1 * v2
        print('\033[32mA Multiplicação de {:.2f} e {:.2f} é de {:.2f}'.format(v1,v2,mult))
        print('=-'*20)
    if esc == 3:
        if v1 > v2:
            print('\033[32mEntre {:.2f} e {:.2f} o {:.2f} é o maior'.format(v1,v2,v1))
            print('=-'*20)
        elif v2 > v1:
            print('\033[32mEntre {:.2f} e {:.2f} o {:.2f} é o maior'.format(v2,v1,v2))
            print('=-'*20)
        else: 
            print('\033[32mOs valores {:.2f} e {:.2f} são iguais'.format('v1,v2'))
            print('=-'*20)

    elif esc == 4:
        print('\033[mInsira Novos Números')
        print('=-'*20)
    

    