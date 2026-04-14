def questao_1():
    aluno = {
        'nome':"Keivn",
        "idade":20,
        "nota":6.5,
        "aprovado":False,
    }

    nome = aluno['nome']

    nota_nova = {"nota":7.5}

    aluno.update(nota_nova)

    print(f"Olá, {nome}. Sua nota foi {aluno['nota']}")

    if aluno["nota"] >= 7:
        aprove = {"aprovado":True}
        aluno.update(aprove)
        print("aprovado")
    else:
        print("Você não foi aprovado")

    print(aluno)


def questao_2():
    estoque = {
    "arroz": 50,
    "feijão": 30,
    "macarrao": 0,
    "oleo": 15,
    "farinha": 0
    }

    estoque.update({"acucar":40})

    estoque.pop('macarrao')
    
    print(estoque)

questao_2()