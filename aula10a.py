#Condções - ou o bloco vedadeiro ou o bloco falso

tempo=int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')


#Condição simplificada - escreve a mesma coisa, mas com menos linhas de código.
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('---FIM---')
