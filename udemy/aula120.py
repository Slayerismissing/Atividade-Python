# Manipulando chaves e valores em dicionários

pessoa = {}
chave = 'nome'

pessoa[chave] = 'Kevin Burgos'
pessoa['sobrenome'] = 'Oliveira'

print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])