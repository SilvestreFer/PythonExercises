peso=float(input('Qual o seu peso em Kg?'))
altura=float(input('Qual a sua altura em metros?'))

imc=peso/altura**2

print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso. Procure profissionais adquados para lhe ajudar.')
elif 18.5 <= imc < 25:
    print('Você está no seu PESO IDEAL! Parabéns! Continue cuidando da sua saúde.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO. Procure profissionais adequados para lhe ajudar com a perda de peso.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE. Cuidado! Procure profissionais adequados para lhe ajudar a cuidar da saúde.')
elif 40 <= imc:
    print('Você está em OBESIDADE MÓBIDA. Cuidado! Procure profissionais adequados para lhe ajudar a cuidar da saúde.')