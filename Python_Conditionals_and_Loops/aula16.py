lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis

print(lanche[:2])
print(lanche[1])
print(lanche)
print(lanche[-1])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for contador in range(0, len(lanche)):
    print(lanche[contador])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5)) #mostra quantas vezes o número se repete
print(c.index(8)) #mostra a posição
print(c.index(8))
print(c.index(5, 1))
