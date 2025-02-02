apelido = {'Juandrio':'Amor',
           'Juan':'Amor',
           'Fernanda':'Fê',
           'Tarsila':'Tatá'}

nome = str(input('Qual é o seu nome?')).strip().title()

if nome in apelido:
    apelido = apelido[nome]
else:
    apelido = nome

if nome == 'Fernanda':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Cláudia, Jéssica, Juliana':
    print('Belo nome feminino.')
    #Desse jeito o comando 'in' ler uma string
    #Com isso verifica se o nome digitado está em qualquer posição dessa string
    #E aceita nomes como Julia ou Éssi, por exemplo.
elif nome in ['Juandrio','Juan']:
    print('Oi, gato!')
elif nome == 'Tarsila':
    print('Oi, gata! Cê tá boa?')
elif nome in ['José', 'Fernando']:
    print('Você tem o nome do meu pai! :)')
elif nome == 'Rosa' or nome == 'Roseane':
    print('Oi, mãe!')
    mae=str(input('A senhora é a minha mãe, não é?')).strip()
    if mae == 'sim' or mae == 'claro' or mae == 'lógico':
        print('Bença, mãe?')
    else:
        print('Desculpe! Tenha um bom dia senhora Rosa.')
else:
    print('Oi! Tudo bem?')
print(f'Tenha um bom dia, {apelido}!')