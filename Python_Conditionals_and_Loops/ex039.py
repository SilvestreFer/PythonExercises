from datetime import datetime

male=str(input('Você é do sexo masculino?')).strip().lower()

if male == 'sim':
    nascimento=int(input('Em que ano você nasceu?'))
    ano=datetime.now().year #não dá pra usar datetime direto, precisa criar uma variável.
    idade=ano-nascimento
    if idade < 18:
        faltam=18-idade
        print(f'Você ainda vai se alistar no serviço militar. Faltam {faltam} anos para esse momento.')
    elif idade == 18:
        print('É hora de se alistar para o serviço militar! Procure mais informações com o orgão responsável.')

    elif idade > 18:
        passou=idade-18
        print(f'Você já passou do tempo para alistamento no serviço militar que deveria ter acontecido {passou} anos atrás. '
          f'Procure mais informações com o orgão responsável.')
else:
    print('O alistamento no serviço militar não é obrigatótio para você.')