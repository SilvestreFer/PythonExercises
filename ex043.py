peso=float(input('Qual o seu peso em quilos?'))
altura=float(input('Qual a sua altura em metros?'))

imc=peso/altura**2

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso. Tente procurar profissionais adquados para lhe ajudar com o ganho de massa muscular.')
elif 18.5 < imc < 25:
    print('Você está no seu peso ideal! Parabéns! Continue cuidando da sua saúde.')
elif 25 < imc < 30:
    print('Você está com SOBREPESO. Procure profissionais adequados para lhe ajudar com a perda de peso.')
elif 30 < imc < 40:
    print('Você está com OBESIDADE. Procure profissionais adequados para lhe ajudar a cuidar da saúde.')
elif 40 < imc:
    print('Você está com OBESIDADE MÓBIDA. Procure profissionais adequados para lhe ajudar a cuidar da saúde.')