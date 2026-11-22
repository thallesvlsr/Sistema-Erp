# Ordena os elementos pelo código em ordem crescente.
# Essa ordenação será utilizada antes da busca binária.
def ordenar_por_codigo(itens):

    # Cria uma cópia para não modificar
    # diretamente a lista original.
    lista = itens.copy()

    # Insertion Sort.
    # O for e o range percorre a lista, começando pelo índice 1, ou seja, pelo segundo elemento.
    
    for i in range(1, len(lista)):

    # O "atual" guarda o elemento que queremos inserir na posição correta.
    # j começa na posição anterior ao elemento atual, permitindo comparar e deslocar os elementos anteriores.
    # O "i"indica a posição do elemento que estamos analisando.
        atual = lista[i]
        j = i - 1

        # Desloca para a direita os elementos
        # que possuem código maior que o atual.
        while j >= 0 and lista[j].codigo > atual.codigo:
            # lista[j + 1] = lista[j] move o produto uma posição para a direita
            # Já j -= 1 faz o algoritmo olhar o próximo produto à esquerda
            # o j -= 1 faz o j voltar uma posição depois de cada deslocamento.
            # Quando o while termina, j + 1 indica exatamente a posição que ficou disponível para inserir o atual.
            lista[j + 1] = lista[j]
            j -= 1

        # Insere o elemento na posição correta.
        # Depois que o while termina
        # Coloca o produto atual no espaço aberto
        lista[j + 1] = atual

    return lista

# Ordena os produtos alfabeticamente pelo nome.
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

# Ordena os produtos da maior quantidade
# para a menor quantidade.
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