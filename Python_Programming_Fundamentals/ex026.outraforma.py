#Parte 01: Recebe a frase
frase=str(input('Digite uma frase: ')).upper().strip()

#Parte 02: Contando os 'A's
print(f'A letra "A" aparece {frase.count('A')} vezes na frase.')
print(f'A primeira vez que a letra "A" aparece é na posição {frase.find('A')+1}.')
print(f'A última vez que a letra "A" aparece é na posição {frase.rfind('A')+1}.')

