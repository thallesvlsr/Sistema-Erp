# Função que realiza uma busca binária pelo código.
# a lista recebida precisa estar
# ordenada pelo código.
def busca_binaria_por_codigo(lista, codigo):

    # Define o início da área de busca.
    inicio = 0

    # Define o final da área de busca.
    fim = len(lista) - 1

    # Continua procurando enquanto ainda existir
    # uma área válida da lista para analisar.
    while inicio <= fim:

        # Calcula a posição do elemento do meio.
        meio = (inicio + fim) // 2

        # Pega o elemento que está no meio.
        item = lista[meio]

        # Se o código do elemento do meio for igual
        # ao código procurado, encontramos o objeto.
        if item.codigo == codigo:
            return item

        # Se o código procurado for maior,
        # elimina a metade esquerda da busca.
        elif item.codigo < codigo:
            inicio = meio + 1

        # Caso contrário, o código procurado é menor
        # e eliminamos a metade direita.
        else:
            fim = meio - 1

    # Se terminar o while sem encontrar,
    # significa que o código não existe.
    return None