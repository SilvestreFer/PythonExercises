soma = 0
contador = 0
for c in range(1,500,2):
    if c % 3 == 0:
        soma += c
        #Um acumular soma um valor.
        contador += 1
        #Um contador conta mais 1.
print(f'A soma de todos os {contador} valores solicitados é {soma}.')
