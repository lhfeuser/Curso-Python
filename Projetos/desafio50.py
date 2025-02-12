total = 0
for num in range(1,7):
    dig = int(input('Digite um número \nNúmero: '))
    print('=-'*10)
    if dig % 2 == 0:
        total += dig
print(total)
    