"""
numero = input('Digite um número: ')

if numero.isdigit():
    if numero % 2 == 0:
        print('Seu número é par!')
     else:
        print('Seu número é ímpar')
else:
    print('Isso não é um número')

--------------------------------------------------
numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

if numero_1 > numero_2:
    print(f'{numero_1} é maior do que {numero_2}')
elif numero_1 < numero_2:
    print(f'{numero_1} é menor do que {numero_2}')
else:
    print(f'os dois números são iguais')
-----------------------------------------------
    
letra = input('Digite uma letra: ').lower()

if letra in 'aeiou':
    print('vogal')
else:
    print('consoante')

--------------------------------------------------
nota_1 = int(input('Digite sua primeira nota: '))
nota_2 = int(input('Digite sua segunda nota: '))
media = (nota_1 + nota_2) / 2

if media < 7:
    print('Reprovado')
elif media >= 7:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção!')
-------------------------------------------------

numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')
numero_3 = input('Digite o terceiro número: ')

if numero_1 >= numero_2 and numero_1 >= numero_3:
    print(f'{numero_1} é o maior entre os 3')

elif numero_2 >= numero_1 and numero_2 >= numero_3:
    print(f'{numero_2} é o maior entre os 3')

elif numero_3 >= numero_1 and numero_3 >= numero_2:
    print(f'{numero_3} é o maior entre os 3')

else:
    print('todos são iguais')

------------------------------------------------------------------

turno_de_estudo = input('Em que turno você estuda?(M- Matutino, V-vespertino e N-noturno): ').upper()

if turno_de_estudo == 'M':
    print('Tenha um Bom Dia!')
elif turno_de_estudo == 'V':
    print('Tenha uma Boa Tarde!')
elif turno_de_estudo == 'N':
    print('Tenha uma Boa Noite!')
else:
    print('Digite uma letra correspondente ao seu turno!')

----------------------------------------------------------------


pergunta_1 = int(input('Telefonou para a vítima?(0 não, 1 sim): '))
pergunta_2 = int(input('Esteve no local do crime?(0 não, 1 sim): '))
pergunta_3 = int(input('Mora perto da vítima?(0 não, 1 sim): '))
pergunta_4 = int(input('Devia para a vítima?(0 não, 1 sim): '))
pergunta_5 = int(input('Já trabalhou com a vítima?(0 não, 1 sim): '))

total = pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5

if total == 0:
    print('Inocente')

if total > 1:
    if total <= 2:
        print('Suspeito!')
    elif total == 3  or total == 4:
        print('Cúmplice!')
    elif total >= 5:
        print('ASSASSINO')
------------------------------------------------------------


"""





