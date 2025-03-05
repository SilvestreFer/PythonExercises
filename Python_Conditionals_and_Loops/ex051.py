from time import sleep

print('Vamos calcular os 10 primeiros termos de uma Progressão Aritmética!')
sleep(1)

primeiro=int(input('Digite o primeiro termo da sua PA: '))
razão=int(input('Digite a razão: '))
décimo= primeiro + (10-1) *razão #Usei a fórmula do n termo de uma PA: "an = a1 + (n – 1)r"
sleep(1)

print('Estes são os 10 primeiros termos da sua PA: ')
for c in range(primeiro, décimo+razão, razão):
    print(c, end=' ➔ ')
print('Abacou!')