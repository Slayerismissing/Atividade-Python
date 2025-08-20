from time import sleep


def exercício_1():
    contador = 0

    while contador < 100:
        print(contador)
        contador += 1 
        sleep(0.5)

#################################################################################

def exercício_2():
    contador = 0
    total = int(input('Digite o limite que você deseja: '))

    while contador < total:
        print(contador)
        contador += 1 

#################################################################################

def exercício_3():
    while True:
        numero_1 = int(input('Digite o número: '))
        numero_2 = int(input('Digite outro número: '))
        
        total = numero_1 + numero_2
        print(f'{numero_1} + {numero_2} = {total}!')

        decisão = input('Deseja continuar?(S ou N): ').upper()

        if decisão == 'S':
            continue
        elif decisão == 'N':
            print('\nEncerrando programa', end="")
            sleep(1)
            print('.', end="")
            sleep(1.5)
            print('.', end="")
            sleep(2)
            print('.', end="")
            break

###################################################################
def exercício_4():

    f1 = 0
    f2 = 1

    print(f1, end=", ")
    print(f2, end=", ")

    while True:
        f3 = f1 + f2

        if f3 > 500:
            break

        print(f3, end=", ")

        f1 = f2
        f2 = f3


#####################################################################

def exercício_5():


    while True:
        n_numeros = input('Digite a quantidade de números: ')

        try:
            n_numeros = int(n_numeros)
            validacao = True
        except ValueError:
            validacao = None
        if not validacao:
            print('Digite um número')
        else:
            numero = []

            for index in range(n_numeros):
                valor = int(input(f'digite o {index+1}° número: '))

                while valor < 0 or valor > 1000:
                    print('Digite números entre 0 e 1000')
                    valor = int(input(f'digite o {index+1}° número: '))

                numero.append(valor)


            print(numero.sort())
            maior = max(numero)
            menor = min(numero)
            somar = sum(numero)
            
            print(f'Esse foi o maior número {maior}!')
            print(f'Esse foi o menor número {menor}!')
            print(f'Essa é a soma de todos os números: {somar}!')

            decisao = input('Deseja continuar?(sim ou não): ').lower()

            if decisao.startswith('n'):
                print('Encerrando o programa...')
                break
            else:
                continue


#####################################################################


def exercício_6():

    while True:
        #Validando nome 
        nome = input('Digite seu nome: ')
        while len(nome) <= 3:
            print('Seu nome só tem 3 letras')
            nome = input('Digite seu nome: ')


        #validando Idade entre 0 a 150
        idade = input('Digite sua idade: ')
        validacao_idade = None
        try:
            idade = int(idade)
            validacao_idade = True
        except:
            validacao_idade = None
        if not validacao_idade:
            print('Digite um número válido!')
            continue
        else:
            while idade < 0 or idade > 150:
                print('Sua idade precisa ser entre 0 e 150')
                idade = int(input('Digite sua idade: '))


        #validando o sexo
        sexo = input('Qual o seu sexo?(f ou m): ')
        while sexo != 'f' and sexo != 'm':
            print('Digite f ou m')
            sexo = input('Qual o seu sexo?(f ou m): ')


        #validando estado civil
        est_civil = input('Qual o seu estado civil?("s" ,"c", "v", "d"): ')
        while est_civil not in ("s", "c", "v", "d"):
            print('Digite apenas s, c, v ou d')
            est_civil = input('Qual o seu estado civil?("s" ,"c", "v", "d"): ')


        #Verificação de salário
        salario = input('Quanto você ganha por mês?: ')
        validacao_sal = None
        try:
            salario = float(salario)
            validacao_sal = True
        except:
            validacao_sal = None
        if not validacao_sal:
            print('Digite um número válido!')
            continue
        else:
            while salario < 0:
                print('digite um salário maior que 0')
                salario = input('Quanto você ganha por mês?: ')
        
        #Pegando as respostas
        respostas = [
            f'Seu nome: {nome}',
            f'Você tem {idade} anos',
            f'Sexo: {sexo}',
            f'Estado Civil: {est_civil}',
            f'Salário: {salario}',
        ]

        for resposta in respostas:
            print(resposta)
            sleep(1)
            
        break

def exercício_7():

   numero = int(input('Digite um numero: '))
   primo = 0

   for i in range(1 , (numero + 1)):
       if numero % i == 0:
           primo += 1

   if primo == 2:
       print('Primo')
   else:
       print('Não primo')





