print(f'Os números pares no espaço de 1 a 50 são:')
for c in range(1,50):
    if c %2 == 0:
        print(c, end=" ")  # o end=" " cria um espaço ao invés de quebra de linha