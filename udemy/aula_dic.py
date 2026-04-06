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


pessoa = {
    'nome':"Kevin",
    'sobrenome':"Burgos",
}

print(len(pessoa)) # 2
print(list(pessoa.keys())) # ['nome','sobrenome']
print(list(pessoa.values())) #['Kevin','Burgos']
print(list(pessoa.items())) #[('nome','Kevin'), ('sobrenome', 'Burgos')]



