dados = dict()
dados = {'nome': 'Pedro',
    'idade' : 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)

filme = {'título': 'Star Wars',
         'ano':1977,
         'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}.')

locadora = list()
locadora.append({'título': 'Star Wars',
         'ano':1977,
         'diretor': 'George Lucas'})
locadora.append({'título': 'Avengers',
         'ano': 2012,
         'diretor': 'Joss Whedon'})
locadora.append({'título': 'Matrix',
         'ano':1999,
         'diretor': 'Wachowski'})
print(locadora[0]['ano'])
print(locadora[2]['título'])
