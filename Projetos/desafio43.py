# Recebe altura e peso da pessoa 
peso = float(input('Insira seu peso \nPeso: '))
alt = float(input('Insira sua altura \nAltura: '))
# Calcula o imc
imc = peso / (alt**2)
#Condiçoes
if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Você está com Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Você está com Sobrepeso')
elif imc > 30 and imc <- 40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Mórbida')
