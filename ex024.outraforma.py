#Parte 01 - Receber a cidade

   #É legal quando estiver trabalhando com string sempre dar um strip, porque os +
   #usuários escrevem espaços aleatórios

cidade = str(input('Em que cidade você nasceu? ')).strip()

#Parte 02 - Mostrando se a cidade tem 'Santo'

 #Nesse código usamos a contagem usamos o fatiamento de string, para encontrar uma +
 #palavra específica (Santo).
 #O comando upper foi usado pro caso de se o usuário escrever letras malucas, não +
 #modificar a contagem.

print(cidade[:5].upper() == 'SANTO')