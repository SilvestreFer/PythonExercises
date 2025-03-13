sexo = ''
while sexo not in ['M', 'F']:
    sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()
print('Fim')

#outra forma

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()
print('Fim')