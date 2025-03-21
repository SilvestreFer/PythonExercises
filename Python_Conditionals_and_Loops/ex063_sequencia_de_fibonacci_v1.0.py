print('-='*11, 'Sequência de Fibonacci', '-='*11)
número = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(t1,'➔', t2, end= ' ➔ ')
contador = 3 #começa em 3, porque já mostrei o primeiro (0) e segundo termo (1) que são pré-definidos.
while contador <= número:
    t3 = t1 + t2
    print(t3, end= ' ➔ ')
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')
