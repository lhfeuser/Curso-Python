# Inserir a Temperatura em C
tempc = float(input('Insira a temperatura em °C \nTemperatura: '))

# conversão para °F
tempf = 9 * tempc / 5 + 32

# informa a conversão. 
print('A temperatura de {}°C corresponde a {}°F'.format(tempc,tempf))

