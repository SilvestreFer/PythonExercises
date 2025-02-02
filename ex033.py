print('Vou comparar três números para você! B)')

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
terceiro_numero = int(input('Digite o terceiro número:'))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]

print(f'O maior número entre {primeiro_numero}, {segundo_numero} e {terceiro_numero} é {max(numeros)} e o menor é {min(numeros)}.')