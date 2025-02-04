#Parte 1 - Recebendo a frase
frase = str(input('Digite uma frase: ')).strip()

#Parte 2 - Contar os 'a's
frase02 = frase.lower()
print(f'Nessa frase a letra "a" aparece {frase02.count('a')} vezes.')

#Parte 3 - A pela primeira vez
print(f'A letra "a" aparece pela primeira vez na posição {frase02.find('a')}.')

#Parte 4 - A pela última vez
print(f'A letra "a" aparece pela útima vez na posição {frase02.rfind('a')}.')