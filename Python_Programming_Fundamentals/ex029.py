velocidade=int(input('Qual a velocidade do carro em Km/h? '))

if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'Você foi multado! Você excededeu o limite de velocidade permitido que é 80Km/h. ')
    print(f'Você deverá pagar o valor de R${multa:.2f}.')
else:
    print('Ótima performance! Continue dirigindo com prudência!')
print('Se beber não dirija!')