maior = float('-inf')
menor = float('inf')

for c in range(5):
    peso = float(input(f'Qual o pesso da pessoa {c+1} em kg?'))
    if peso > maior:
        maior=peso
    if peso < menor:
        menor=peso
print(f'O maior peso é {maior}kg e o menor peso é {menor}kg.')