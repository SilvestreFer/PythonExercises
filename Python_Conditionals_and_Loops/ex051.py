primeiro=int(input('Digite o primeiro termo da sua Progressão Aritmética: '))
razão=int(input('Digite a razão: '))

print('Estes são os 10 primeiros termos da sua PA: ')
for c in range(primeiro, primeiro + 10*razão, razão):
    print(c, end=' ')