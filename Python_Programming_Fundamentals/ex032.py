#Biblioteca para trabalhar com a data do computador:
from datetime import date

#Pedindo o ano para análise:
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))

#Para a data do PC
if ano == 0:
    ano = date.today().year

#Calculo para o ano bissexto: É mais que divisão por 4!
 # o ano tem que ser um número divisível por 4 e um ano que cumpra o critério anterior não pode ser divisível por 100, a menos que seja também divisível por 400.
 
if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:
    print(f'O ano {ano} é bissexto :)')

else:
    print(f'O ano {ano} NÃO é bissexto.')