sx = ''

while sx in 'M' or sx in 'F':
    sx = str(input('\033[mInsira o sexo da pessoa M/F \nSexo: ')).upper().strip()
    print('=-'*15)

    if sx != 'M' and sx != 'F':
        while sx != 'M' and sx != 'F':
            print('\033[31mDigite novamente')
            print('=-'*15)
            sx = str(input('\033[33mInsira novamente o sexo da pessoa M/F \nSexo: ')).upper().strip()
            print('=-'*15)