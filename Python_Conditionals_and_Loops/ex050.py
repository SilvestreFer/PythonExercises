soma = 0
contador = 0
for c in range(1,7):
    numero=int(input(f'Digite o {c}º número: '))
    if numero%2==0:
        soma+=numero
        contador+=1
if contador == 1:
    print(f'Você informou 1 valor par, {soma}.')
elif contador > 1:
    print(f'Você informou {contador} valores PARES. A soma dos pares é {soma}.')
else:
    print('Você informou apenas valores impares. A soma dos pares é 0.')
