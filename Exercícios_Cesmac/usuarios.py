import os
from time import sleep

usuarios = []

try:
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                user, senha = linha.split(';')
                usuarios.append({'user':user, 'senha':senha})
except FileNotFoundError:
    with open('usuarios.txt', 'w') as arquivo:
        pass


while True:
    os.system('cls')
    print('Boas vindas! Escolha uma das opções a baixo:\n' \
    '1 - entra com usuário\n' \
    '2 - criar um novo usuário\n' \
    '3 - sair')
    opcoes = input('Escolha: ')


    try:
        opcoes = int(opcoes)
    except ValueError:
        print('Por favor, digite um número válido')
        continue
    

    # 1 - Entrada com usuário
    if opcoes == 1:
        
            os.system('cls')
            if not usuarios:
                print('Não existe usuários cadastrados, por favor cadastrar um novo')
                sleep(2)
                continue

            usuario = input('digite seu login: ')
            senha = input('digite sua senha: ')

            entrada = False

            for u in usuarios:
                if usuario == u["user"] and senha == u["senha"]:
                    print('Bem vindo!')
                    entrada = True
                    break
            
            if entrada:
                print('teste')
                break
            else:
                print('Usuário ou Senha incorretos')
                sleep(1)
                print('Retornando ao menu...')
                sleep(1.5)
                

            
    if opcoes == 2:
        os.system('cls')
        user_novo = input('Cadastre um novo user(não use ";"): ').strip()
        senha_novo = input('Cadastre uma nova senha(não use ";"): ')
        
        user_novo_normalizado = user_novo.lower()

        existente = False
        for u in usuarios:
            if u["user"].strip().lower() == user_novo_normalizado:
                existente = True
                break
        
        if existente:
            print('esse usuário já existe')
            sleep(1.5)
        else:
            usuarios.append({"user": user_novo, "senha": senha_novo})
            print('Novo usuário cadastrado com sucesso!')
            
            with open('usuarios.txt', 'a') as arquivo:
                arquivo.write(f'{user_novo};{senha_novo}\n')
            
            sleep(1.5)



    if opcoes == 3:
        os.system('cls')
        print('Saindo do programa')
        break