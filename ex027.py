#Parte 01 - Receber o nome completo
nome = str(input('Qual o seu nome completo? ')).strip()
nomes = nome.split()

#Parte 02 - Mostrar o primeiro nome
 #primeiro_nome = nomes[0] ---- Não tá errado, mas considerar se eu vou precisar +
 #desse valor em variável. Como é só pra printar, posso colocar direto no format.
print('Muito prazer em te conhecer!')
print(f'O seu primeiro nome é: {nomes[0]}')

#Parte 03 - Mostrar o último nome
#Mesma coisa da parte dois: preciso da variável? Deixei essa pra lembrar da possibilidade
último_nome = nomes[-1]
print(f'O seu último nome é: {último_nome}')