distancia = float(input('Qual for a distância da viagem em Km?'))

if distancia <=200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
 print(f'O valor da passagem é R${passagem:.2f}.')

#Outra forma:
# passagem = distancia * 0.50 if distancia <=200 else distancia * 0.45
# print(f'O valor da passagem é R${passagem:.2f}.')