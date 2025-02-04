#Parte 1:

nome=str(input('Digite seu nome completo: '))
print('Analisando seu nome... ')
print(f'O nome com apenas letras maiusculas é: {nome.upper()}')

#Parte 2:
print(f'O nome com apenas letras minusculas é: {nome.lower()}')

#Parte 3:
semespaco = nome.replace(' ','')
print('A quantidade de letras no nome  completo é: ', len(semespaco))

#Parte 4:
nomes = nome.split()
print(f'Seu primeiro nome é {nomes[0]} e ele tem letras {len(nomes[0])}')

