# Recebe o nome da cidade 
cidade = str(input('Insira o nome da sua cidade \nCidade: ')).strip()
# Prepara a String 
muda = cidade[:5].upper() #Coloca tudo em Maiúsculo para padrão de análise 
# print
print(muda == 'SANTO')