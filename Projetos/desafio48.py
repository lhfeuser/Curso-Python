s = 0
c=0
for impar in range(1,501,2):
    if impar % 3 == 0:
        s += impar
        c += 1
print('A soma dos valores é de {} e foram somados {} números'.format(s,c))
    
   