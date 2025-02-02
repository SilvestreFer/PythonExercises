nota1=float(input('Qual foi a sua primeira nota?'))
nota2=float(input('Qual foi a sua segunda nota?'))

media=(nota1 + nota2)/2

if media <= 5:
    print(f'A sua média é \033[31m{media}\033[m. Você foi \033[0;30;41mREPROVADO\033[m! Estude mais da próxima vez.')

elif 5 < media <= 6.9:
    print(f'A sua média é \033[33m{media}\033[m. Você está em \033[0;30;43mRECUPERAÇÃO\033[m. Bom estudo para as novas provas!')

elif media >= 7:
    print(f'A sua média é \033[32m{media}\033[m. Você foi \033[0;30;42mAPROVADO\033[m! Meus parabéns!')