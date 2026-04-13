"""
Métodos úteis dos dicionários em Python:

len - quantas chaves
key - iteráveis com as chaves
values - iteráveis com os valores
items - iteráveis com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada
update - Atualiza um dicionário com outro


"""
# p1 = {
#     'nome':'Kevin',
#     'sobrenome':'Burgos"'
# }

# # print(p1.get('nome'))

# # nome = p1.pop('nome')
# # print(nome)
# # print(p1)

# # nome = p1.popitem()
# # print(nome)
# # print(p1)

# # p1.update({
# #     'nome':'novo valor',
# #     'idade':45,
# # })

# # p1.update(nome='novo valor', idade=30)

# tupla = ('nome','novo valor'),
# p1.update(tupla)
# print(p1)

perguntas = [
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções':['3','2','5','4'],
        'Resposta':'4',
    },
    {
        'Pergunta':'Quanto é 5*5?',
        'Opções':['90','12','25','10'],
        'Resposta':'25',
    },{
        'Pergunta':'Quanto é 10/2?',
        'Opções':['4','2','5','1'],
        'Resposta':'5',
    }
    ]


qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta',pergunta['Pergunta'])

    opcoes = pergunta["Opções"]

    for i, opcao in  enumerate(opcoes):
        print(f"{i}) ", opcao)
    print()


    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
        print('digit true')
    else:
        print('Isso não é um dígito')
        break

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True 

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou ✔')
    else:
        print('Errou ❌')


print(f"Você acertou: {qtd_acertos} de {len(perguntas)}")


       
        



