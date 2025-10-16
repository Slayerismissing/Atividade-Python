
def ex2():
    def desconto(preco):
        return 0.1 * preco

    valor = int(input('Digite o valor do produto: '))

    des = desconto(valor)

    total = valor - des

    print(f'Seu preço com desconto de 10%({des}) é de: {total}')


def ex3():
    import funcoes_bolsa

    acao = int(input('Digite o valor da ação: '))

    verificacao = funcoes_bolsa.positivo(acao)

    print(verificacao)


def ex4():
    
    def verificacao(idade):

        if idade > 18:
            return 'Maior idade'
        else:
            return 'Menor idade'
    
    usuario = int(input('Digite sua idade: '))

    veri = verificacao(usuario)

    print(veri)

def ex5():

    def calcular(peso, altura):
        return peso / (altura **2)
    
    peso1 = float(input('Digite seu peso: '))
    alt = float(input('Digite sua altura: '))

    total = calcular(peso1, alt)

    print(f'{total:.2f}')

    if total > 25:
        print('acima do peso')
    elif total < 24.90 and total > 18.50:
        print('Peso normal')
    else:
        print('Abaixo do peso') 

def ex6():

    def imposto(valor):
        return 0.15 * valor
    
    produto = int(input('Digite o valor do produto: '))

    taxa = imposto(produto)

    total = taxa + produto

    print(f'Essa é a taxa de 15%({taxa}) no valor do produto: {total}')


def ex7():

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')

    try:
        num1 = float(num1)
        num2 = float(num2)

        if num2 == 0:
            print('não pode dividir por 0')
        else:
            total = num1 / num2
            print(f'{total}')

    except ValueError:
        print('digite um número válido')

    
def ex8():

    num = input('Digite um número: ')

    try:
        num = int(num)
        if num == 0:
            raise ZeroDivisionError
        else:
            print(num)
    except ValueError:
        print('Digite um número!')
    except ZeroDivisionError:
        print(f'Sem número 0')
    

def ex9():

    def dividir(a,b):
        return a/b
    
    num1 = input('Digite o numerador: ')
    num2 = input('Digite o denominador: ')


    try:
        num1 = int(num1)
        num2 = int(num2)

        if num2 == 0:
            raise ZeroDivisionError('Denominador não pode ser 0')
        else:
            total = dividir(num1, num2)
            print(total)
    except ZeroDivisionError as e:
        print(str(e))

