lanche=['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)

lanche[3]= 'Picolé'
lanche.append('Cookie')
lanche.insert(0, 'Cachoro quente')
print(lanche)
print(len(lanche))
print(lanche[0])
print(lanche[1])

del lanche[3]
lanche.pop(3)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)

valores = list(range(4,11))
valores = [8,2,5,4,9,3,0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
if 1 in valores:
    valores.remove(1)
    print(valores)
else:
    print(f'Não encontrei o valor {1}.')
for contador in range(0,3):
    valores.append(int(input('Digite um valor: ')))
    print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim da lista!')

a = [2,3,4,7]
b = a [:] #[:] cria uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
