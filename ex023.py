#Parte 01 - Recebendo os dados pelo teclado

import emoji
print('Digite um número de 0 a 9999 e eu vou te dizer os dígitos separados com as casas a qual pertencem 😎')
numero = int(input('Digite o número que você escolheu: '))
print(f'Analisando o número...')

#Parte 02 - Cálculo
unidades = numero %10
dezenas = (numero//10) %10
centenas = (numero//100) %10
milhares = (numero//1000) %10

#Parte 03 - Mostrando para o usuário
print('Unidade: ', unidades)
print('Dezena: ', dezenas)
print('Centena: ', centenas)
print('Milhar: ', milhares)

