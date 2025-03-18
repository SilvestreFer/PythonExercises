#Contando com o 'for'
for c in range (1,10):
    print(c)
print('Fim?')
print('-='*11)

#Contando com o 'while'
c = 1
while c < 10:
    print(c)
    c+=1
print('Fim')
print('-='*11)

#Recebendo números com 'for'
for c in range(1,5):
    número = int(input('Digite um valor: '))
print('Fim')
print('-='*11)

#Recebendo números com 'while'
número = 1
while número != 0:
    número = int(input(('Digite um valor: ')))
print('Fim')
print('-='*11)

#Recebendo strings com 'while'
resposta = 'S'
while resposta == 'S':
    resposta = str(input('Quer continuar? [S/N]')).upper()
print('Fim')
print('-='*11)

#Calculando pares e ímpares com 'while'
número = 1
par = ímpar = 0
while número != 0:
    número = int(input('Digite um valor: '))
    if número != 0:
        if número%2 == 0:
            par += 1
        else:
            ímpar += 1
print(f'Você digitou {par} números pares e {ímpar} números ímpares!')
print('-='*11)