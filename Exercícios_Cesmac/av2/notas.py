def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def maior(lista):
    if len(lista) == 0:
        return None
    return max(lista)

def menor(lista):
    if len(lista) == 0:
        return None
    return min(lista)    