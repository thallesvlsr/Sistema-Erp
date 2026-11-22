from estruturas.fila_prioridade import FilaPrioridade
from models.produto import Produto


def criar_produto(codigo, quantidade, estoque_minimo):
    return Produto(
        codigo,
        f"Produto {codigo}",
        "Categoria teste",
        10.0,
        quantidade,
        estoque_minimo,
        "Fornecedor teste"
    )


def verificar_heap(fila):
    for indice in range(len(fila.itens)):
        esquerda = 2 * indice + 1
        direita = 2 * indice + 2

        if esquerda < len(fila.itens):
            assert (
                fila.prioridade(fila.itens[indice])
                >= fila.prioridade(fila.itens[esquerda])
            ), "Propriedade do heap violada entre pai e filho esquerdo."

        if direita < len(fila.itens):
            assert (
                fila.prioridade(fila.itens[indice])
                >= fila.prioridade(fila.itens[direita])
            ), "Propriedade do heap violada entre pai e filho direito."


def testar_fila_prioridade():
    print("===== TESTES DA FILA DE PRIORIDADE =====")

    fila = FilaPrioridade()

    assert fila.esta_vazia()
    assert fila.remover() is None
    print("[OK] Fila vazia")

    sem_estoque = criar_produto(1, 0, 5)
    abaixo_minimo = criar_produto(2, 2, 5)
    estoque_normal = criar_produto(3, 10, 5)

    fila.inserir(estoque_normal)
    fila.inserir(abaixo_minimo)
    fila.inserir(sem_estoque)

    verificar_heap(fila)
    assert fila.prioridade(fila.itens[0]) == 3
    print("[OK] Inserção e organização das prioridades")

    primeiro = fila.remover()
    segundo = fila.remover()
    terceiro = fila.remover()

    assert primeiro.codigo == 1
    assert segundo.codigo == 2
    assert terceiro.codigo == 3
    assert fila.esta_vazia()
    print("[OK] Remoção em ordem de prioridade")

    assert fila.remover() is None
    print("[OK] Remoção com fila vazia")

    produtos = [
        criar_produto(10, 0, 5),
        criar_produto(11, 1, 5),
        criar_produto(12, 8, 5),
        criar_produto(13, 0, 3),
        criar_produto(14, 2, 8),
        criar_produto(15, 20, 5),
        criar_produto(16, 4, 5),
    ]

    for produto in produtos:
        fila.inserir(produto)
        verificar_heap(fila)

    assert len(fila.listar()) == len(produtos)
    assert len(fila.itens) == len(produtos)
    print("[OK] Inserções múltiplas e propriedade do heap")

    prioridades_removidas = []
    codigos_removidos = []

    while not fila.esta_vazia():
        produto = fila.remover()
        prioridades_removidas.append(fila.prioridade(produto))
        codigos_removidos.append(produto.codigo)
        verificar_heap(fila)

    assert prioridades_removidas == sorted(prioridades_removidas, reverse=True)
    assert len(codigos_removidos) == len(produtos)
    assert len(set(codigos_removidos)) == len(produtos)
    print("[OK] Remoção de todos os produtos em ordem correta")
    print("[OK] Nenhum produto foi perdido ou removido duas vezes")

    print("\nTODOS OS TESTES DA FILA DE PRIORIDADE PASSARAM!")


if __name__ == "__main__":
    testar_fila_prioridade()
