#Parte 01: Recebe o nome:

nome = str(input('Qual é o seu nome completo?')).strip()

#Parte 02: Encontrando o 'Silva
 #in é o operador do Python para encontrar coisas na string
 #upper, porque o usuário pode digitar a palavra com letras malucas

print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')