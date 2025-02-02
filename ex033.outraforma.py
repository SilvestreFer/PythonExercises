a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

#Verificando quem é o menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

#Mostrando os resultados:
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')