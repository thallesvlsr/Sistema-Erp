from estruturas.arvore_avl import ArvoreAVL
from models.produto import Produto


def criar_produto(codigo):
    return Produto(
        str(codigo).zfill(4),
        f"Produto {codigo}",
        "Teste",
        10.0,
        5,
        2,
        "Fornecedor teste"
    )


def verificar_arvore(no):
    if no is None:
        return 0

    altura_esquerda = verificar_arvore(no.esquerda)
    altura_direita = verificar_arvore(no.direita)

    assert abs(altura_esquerda - altura_direita) <= 1, (
        f"Árvore desbalanceada no código {no.produto.codigo}"
    )

    altura_calculada = 1 + max(altura_esquerda, altura_direita)
    assert no.altura == altura_calculada, (
        f"Altura incorreta no código {no.produto.codigo}"
    )

    return altura_calculada


def testar_rotacoes():
    casos = [
        ([30, 20, 10], 20, "Rotação simples à direita (LL)"),
        ([10, 20, 30], 20, "Rotação simples à esquerda (RR)"),
        ([30, 10, 20], 20, "Rotação dupla esquerda-direita (LR)"),
        ([10, 30, 20], 20, "Rotação dupla direita-esquerda (RL)"),
    ]

    for codigos, raiz_esperada, descricao in casos:
        arvore = ArvoreAVL()

        for codigo in codigos:
            arvore.inserir(criar_produto(codigo))

        assert arvore.raiz.produto.codigo == str(raiz_esperada).zfill(4)
        verificar_arvore(arvore.raiz)
        print(f"[OK] {descricao}")


def testar_busca_e_listagem():
    arvore = ArvoreAVL()

    for codigo in [40, 20, 60, 10, 30, 50, 70]:
        arvore.inserir(criar_produto(codigo))

    assert arvore.buscar("0020") is not None
    assert arvore.buscar("0099") is None

    codigos = [produto.codigo for produto in arvore.listar_produtos()]
    assert codigos == [
        "0010", "0020", "0030", "0040", "0050", "0060", "0070"
    ]

    verificar_arvore(arvore.raiz)
    print("[OK] Busca de produto existente e inexistente")
    print("[OK] Listagem In-Order em ordem crescente")


def testar_remocoes():
    arvore = ArvoreAVL()

    # Esta sequência cria uma árvore com folhas, nós com um filho
    # e nós com dois filhos.
    for codigo in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        arvore.inserir(criar_produto(codigo))

    # Remove uma folha.
    arvore.remover("0010")
    assert arvore.buscar("0010") is None
    verificar_arvore(arvore.raiz)
    print("[OK] Remoção de folha")

    # Remove um nó que possui dois filhos.
    arvore.remover("0030")
    assert arvore.buscar("0030") is None
    verificar_arvore(arvore.raiz)
    print("[OK] Remoção de nó com dois filhos")

    # Remove um nó com um filho (a estrutura pode variar após rebalanceamentos).
    arvore.remover("0080")
    assert arvore.buscar("0080") is None
    verificar_arvore(arvore.raiz)
    print("[OK] Remoção e rebalanceamento")

    # Remove a raiz atual.
    codigo_raiz = arvore.raiz.produto.codigo
    arvore.remover(codigo_raiz)
    assert arvore.buscar(codigo_raiz) is None
    verificar_arvore(arvore.raiz)
    print("[OK] Remoção da raiz")


def testar_varias_operacoes():
    arvore = ArvoreAVL()

    codigos = list(range(1, 201))

    # Inserções em ordem crescente, cenário que exige balanceamento.
    for codigo in codigos:
        arvore.inserir(criar_produto(codigo))
        verificar_arvore(arvore.raiz)

    # Remoções alternadas, verificando o balanceamento após cada uma.
    for codigo in codigos[::2]:
        arvore.remover(str(codigo).zfill(4))
        verificar_arvore(arvore.raiz)

    print("[OK] 200 inserções crescentes com balanceamento")
    print("[OK] 100 remoções com balanceamento preservado")


if __name__ == "__main__":
    print("\n===== TESTES DA ÁRVORE AVL =====\n")
    testar_rotacoes()
    testar_busca_e_listagem()
    testar_remocoes()
    testar_varias_operacoes()
    print("\nTODOS OS TESTES DA AVL PASSARAM!\n")
