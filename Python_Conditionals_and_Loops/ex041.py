from datetime import datetime

atleta=str(input('Você é o atleta?')).strip().lower()

if atleta == 'sim':
    nascimento=int(input('Em que ano você nasceu?'))
    ano=datetime.now().year
    idade=ano-nascimento

    if idade <=9:
        print(f'Como você tem {idade} anos, você participa na categoria MIRIM.')
    elif 9 < idade < 14:
        print(f'Com {idade} anos, você participa da categoria INFANTIL.')
    elif 16 < idade < 19:
        print(f'Com {idade} anos, você participa da categoria JUNIOR.')
    elif 19 < idade < 20:
        print(f'Com {idade} anos, você participa da categoria SÊNIOR.')
    elif 20 < idade:
        print(f'Com {idade} anos, você participa da categoria MASTER.')

else:
    nascimento = int(input('Em que ano o atleta nasceu?'))
    ano = datetime.now().year
    idade = ano - nascimento

    if idade <= 9:
        print(f'Como o atleta tem {idade} anos, participa na categoria MIRIM.')
    elif 9 < idade < 14:
        print(f'Com {idade} anos, o atleta participa da categoria INFANTIL.')
    elif 16 < idade < 19:
        print(f'Com {idade} anos, o atleta participa da categoria JUNIOR.')
    elif 19 < idade < 20:
        print(f'Com {idade} anos, o atleta participa da categoria SÊNIOR.')
    elif 20 < idade:
        print(f'Com {idade} anos, o atleta participa da categoria MASTER.')