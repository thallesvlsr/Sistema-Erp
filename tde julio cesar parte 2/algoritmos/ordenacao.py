def ordenar_por_codigo(itens):
    lista = itens.copy()

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j].codigo > atual.codigo:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista


def ordenar_por_nome(produtos):
    lista = produtos.copy()

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j].nome > atual.nome:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista


def ordenar_por_quantidade(produtos):
    lista = produtos.copy()

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j].quantidade < atual.quantidade:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista


def merge_sort(produtos):
    if len(produtos) <= 1:
        return produtos.copy()

    meio = len(produtos) // 2

    esquerda = merge_sort(produtos[:meio])
    direita = merge_sort(produtos[meio:])

    return intercalar(esquerda, direita)


def intercalar(esquerda, direita):
    resultado = []

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i].codigo <= direita[j].codigo:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado