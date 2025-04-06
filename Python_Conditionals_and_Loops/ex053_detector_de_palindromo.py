#Exercício usando fatiamento na condição

from time import sleep

print('''Vamos analisar se a sua frase é um palíndromo!
Você consegue pensar em um?''')
sleep(1)

frase=str(input('Digite uma frase: ')).strip().lower()
frase_sem_espaços=frase.replace(" ", "")

if frase_sem_espaços == frase_sem_espaços[::-1]:
    print(f'A frase "{frase}" é um palíndromo.')
else:
    print(f'A frase "{frase}" não é um palíndromo.')
