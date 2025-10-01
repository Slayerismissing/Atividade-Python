def q1():
    # Questão 1 - Manipulação de listas e strings

    frase = input("Digite uma frase: ")
    palavra = input("Digite uma palavra para buscar: ")

    frase_minuscula = frase.lower()
    palavra_minuscula = palavra.lower()
    palavras_frase = frase_minuscula.split()
    quantidade = 0
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1

    # Quantidade de Palavras
    print(quantidade)


def q2():
    # Q2 - Conversor de Temperatura
    # Conversão entre Celsius e Fahrenheit
    # Obrigração: criar um arquivo conversor.py e importar as funções
    import conversor

    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input("Escolha uma opção (1 ou 2): "))

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = conversor.celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C = {resultado:.2f}°F")

    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = conversor.fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {resultado:.2f}°C")

    else:
        print("Opção inválida.")


def q3():
    # Questão 3: Sistema de autenticação simples
    # Usuários e senhas pré-definidos. Criar uma função para autenticar.

    usuarios = {
        "admin": "1234",
        "joao": "senha123",
        "maria": "abc@2024"
    }


    def autenticar(usuario, senha):  
        if usuarios.get(usuario) == senha:
            return True
        else:
            return False

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if autenticar(usuario, senha):
        print("Autenticação bem-sucedida!")
    else:
        print("Usuário ou senha incorretos.")


def q4():
    # Questão 4 - Verificador de Números Pares e Ímpares
    # Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

    def par_ou_impar(n1):
        if n1 % 2 == 0:
            return 'par'
        else:
            return 'ímpar'

    numero = int(input("Digite um número: "))

    resultado = par_ou_impar(numero)

    print(f"{resultado}")


def q5():

    # Q5 - Controle de Notas
    # Complete a questão criando o notas.py e as funções de: média, maior e menor

    import notas

    notas_aluno = []

    print("=== Controle de Notas ===")
    while True:
        entrada = input("Digite uma nota (ou 'sair' para encerrar): ")

        if entrada.lower() == "sair":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas_aluno.append(nota)
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")

    if notas_aluno:
        print("\n--- Resultados ---")
        print(f"Média: {notas.media(notas_aluno):.2f}")
        print(f"Maior: {notas.maior(notas_aluno)}")
        print(f"Menor: {notas.menor(notas_aluno)}")
    else:
        print("Nenhuma nota foi informada.")


def q6():
    # Q6 - Conversor de Moedas
    # Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
    # real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão
    import conversor_din

    valor = float(input("Digite o valor: "))
    cotacao = float(input("Digite a cotação do dólar: "))

    real_para_dolar = conversor_din.real_para_dollar(valor, cotacao)
    dolar_para_real = conversor_din.dollar_para_real(valor, cotacao)

    print(f"\n{valor:.2f} reais equivalem a {real_para_dolar:.2f} dólares.")
    print(f"{valor:.2f} dólares equivalem a {dolar_para_real:.2f} reais.")
   