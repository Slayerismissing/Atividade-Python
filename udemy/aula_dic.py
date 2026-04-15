"""
Dictionary Useful Methods in Python:
This module demonstrates the most commonly used dictionary methods for data manipulation and retrieval.
Methods:
    len(dict): Returns the number of key-value pairs in the dictionary.
    dict.keys(): Returns a view object containing all the keys in the dictionary.
                 Can be converted to a list for iteration.
    dict.values(): Returns a view object containing all the values in the dictionary.
                   Can be converted to a list for iteration.
    dict.items(): Returns a view object containing all key-value pairs as tuples.
                  Can be converted to a list for iteration.
    dict.setdefault(key, default): Adds a key-value pair to the dictionary if the key 
                                   does not already exist. Returns the value.
    dict.copy(): Creates a shallow copy of the dictionary. Modifications to nested 
                 objects will affect both copies.
    dict.get(key, default=None): Safely retrieves the value for a given key, returning 
                                 a default value if the key doesn't exist.
    dict.pop(key, default=None): Removes and returns the value for a given key. 
                                 Raises KeyError if key doesn't exist and no default provided.
    dict.update(other_dict): Updates the dictionary with key-value pairs from another 
                             dictionary, overwriting existing keys.
Example:
    A person dictionary with name and surname information, showcasing basic 
    dictionary traversal and method usage.
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



