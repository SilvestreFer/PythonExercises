import emoji

print(f'Os números pares no espaço de 1 a 50 são:')
for c in range(1,51):
    if c %2 == 0:
        print(c, end=" ")  # o end=" " cria um espaço ao invés de quebra de linha

print('Acabou!', emoji.emojize(":smiling_face:"))

#Nesse exercício faz todos os laços. "Tem mais trabalho pro processador".