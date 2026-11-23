
from models.produto import Produto
from models.fornecedor import Fornecedor
from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService
from services.estoque_service import EstoqueService
from services.reposicao_service import ReposicaoService


produto_service = ProdutoService()
fornecedor_service = FornecedorService()

estoque_service = EstoqueService(produto_service)
reposicao_service = ReposicaoService(produto_service)


def cadastrar_produto():
    try:
        print("\n--- CADASTRAR PRODUTO ---")

        codigo = input("Código: ")
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        estoque_minimo = int(input("Estoque mínimo: "))
        fornecedor = input("Fornecedor: ")

        produto = Produto(
            codigo,
            nome,
            categoria,
            preco,
            quantidade,
            estoque_minimo,
            fornecedor
        )

        produto_service.cadastrar(produto)
        print("\nProduto cadastrado com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")

    produtos = produto_service.listar()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("\n-------------------------")
        print("Código:", produto.codigo)
        print("Nome:", produto.nome)
        print("Categoria:", produto.categoria)
        print(f"Preço: R$ {produto.preco:.2f}")
        print("Quantidade:", produto.quantidade)
        print("Estoque mínimo:", produto.estoque_minimo)
        print("Fornecedor:", produto.fornecedor)


def buscar_produto():
    print("\n--- BUSCAR PRODUTO ---")

    codigo = input("Código do produto: ")
    produto = produto_service.buscar_por_codigo(codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("\n--- PRODUTO ENCONTRADO ---")
    print("Código:", produto.codigo)
    print("Nome:", produto.nome)
    print("Categoria:", produto.categoria)
    print(f"Preço: R$ {produto.preco:.2f}")
    print("Quantidade:", produto.quantidade)
    print("Estoque mínimo:", produto.estoque_minimo)
    print("Fornecedor:", produto.fornecedor)


def alterar_produto():
    try:
        print("\n--- ALTERAR PRODUTO ---")

        codigo = input("Código do produto: ")
        produto = produto_service.buscar_por_codigo(codigo)

        if not produto:
            print("\nProduto não encontrado.")
            return

        nome = input("Novo nome: ")
        categoria = input("Nova categoria: ")
        preco = float(input("Novo preço: "))
        quantidade = int(input("Nova quantidade: "))
        estoque_minimo = int(input("Novo estoque mínimo: "))
        fornecedor = input("Novo fornecedor: ")

        produto_service.alterar(
            codigo,
            nome,
            categoria,
            preco,
            quantidade,
            estoque_minimo,
            fornecedor
        )

        print("\nProduto alterado com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def remover_produto():
    try:
        print("\n--- REMOVER PRODUTO ---")

        codigo = input("Código do produto: ")
        produto_service.remover(codigo)

        print("\nProduto removido com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def cadastrar_fornecedor():
    try:
        print("\n--- CADASTRAR FORNECEDOR ---")

        codigo = input("Código: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        fornecedor = Fornecedor(codigo, nome, telefone, email)
        fornecedor_service.cadastrar(fornecedor)

        print("\nFornecedor cadastrado com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def listar_fornecedores():
    print("\n--- FORNECEDORES CADASTRADOS ---")

    fornecedores = fornecedor_service.listar()

    if len(fornecedores) == 0:
        print("Nenhum fornecedor cadastrado.")
        return

    for fornecedor in fornecedores:
        print(
            f"\nCódigo: {fornecedor.codigo}"
            f"\nNome: {fornecedor.nome}"
            f"\nTelefone: {fornecedor.telefone}"
            f"\nE-mail: {fornecedor.email}"
        )


def buscar_fornecedor():
    print("\n--- BUSCAR FORNECEDOR ---")

    codigo = input("Código do fornecedor: ")
    fornecedor = fornecedor_service.buscar_por_codigo(codigo)

    if not fornecedor:
        print("\nFornecedor não encontrado.")
        return

    print(
        f"\nCódigo: {fornecedor.codigo}"
        f"\nNome: {fornecedor.nome}"
        f"\nTelefone: {fornecedor.telefone}"
        f"\nE-mail: {fornecedor.email}"
    )


def alterar_fornecedor():
    try:
        print("\n--- ALTERAR FORNECEDOR ---")

        codigo = input("Código do fornecedor: ")
        fornecedor = fornecedor_service.buscar_por_codigo(codigo)

        if not fornecedor:
            print("\nFornecedor não encontrado.")
            return

        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        email = input("Novo e-mail: ")

        fornecedor_service.alterar(
            codigo,
            nome,
            telefone,
            email
        )

        print("\nFornecedor alterado com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def remover_fornecedor():
    try:
        print("\n--- REMOVER FORNECEDOR ---")

        codigo = input("Código do fornecedor: ")
        fornecedor_service.remover(codigo)

        print("\nFornecedor removido com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def entrada_estoque():
    try:
        print("\n--- ENTRADA DE ESTOQUE ---")

        codigo = input("Código do produto: ")
        quantidade = int(input("Quantidade: "))
        motivo = input("Motivo: ")

        estoque_service.entrada(codigo, quantidade, motivo)

        print("\nEntrada realizada com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def saida_estoque():
    try:
        print("\n--- SAÍDA DE ESTOQUE ---")

        codigo = input("Código do produto: ")
        quantidade = int(input("Quantidade: "))
        motivo = input("Motivo: ")

        estoque_service.saida(codigo, quantidade, motivo)

        print("\nSaída realizada com sucesso!")

    except ValueError as erro:
        print("\nErro:", erro)


def listar_movimentacoes():
    print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")

    movimentacoes = estoque_service.listar_historico()

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")
        return

    for movimentacao in movimentacoes:
        print(
            f"\nProduto: {movimentacao.produto.nome}"
            f"\nCódigo: {movimentacao.produto.codigo}"
            f"\nTipo: {movimentacao.tipo}"
            f"\nQuantidade: {movimentacao.quantidade}"
            f"\nMotivo: {movimentacao.motivo}"
        )


def desfazer_movimentacao():
    try:
        print("\n--- DESFAZER ÚLTIMA MOVIMENTAÇÃO ---")

        movimentacao = estoque_service.desfazer_ultima_movimentacao()

        print("\nMovimentação desfeita com sucesso!")
        print(f"Produto: {movimentacao.produto.nome}")

    except ValueError as erro:
        print("\nErro:", erro)


def mostrar_reposicao():
    print("\n--- FILA DE REPOSIÇÃO ---")

    fila = reposicao_service.gerar_fila_reposicao()

    if fila.esta_vazia():
        print("Nenhum produto precisa de reposição.")
        return

    while not fila.esta_vazia():
        produto = fila.remover()

        print(
            f"\nProduto: {produto.nome}"
            f"\nCódigo: {produto.codigo}"
            f"\nQuantidade: {produto.quantidade}"
            f"\nEstoque mínimo: {produto.estoque_minimo}"
            f"\nPrioridade: {fila.prioridade(produto)}"
        )


def produtos_por_nome():
    print("\n--- PRODUTOS ORDENADOS POR NOME ---")

    produtos = produto_service.ordenar_nome()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"{produto.codigo} - "
            f"{produto.nome} - "
            f"Quantidade: {produto.quantidade}"
        )


def produtos_por_quantidade():
    print("\n--- PRODUTOS ORDENADOS POR QUANTIDADE ---")

    produtos = produto_service.ordenar_quantidade()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"{produto.codigo} - "
            f"{produto.nome} - "
            f"Quantidade: {produto.quantidade}"
        )


def percurso_in_order():
    print("\n--- PERCURSO IN-ORDER ---")

    produtos = produto_service.listar()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("Código:", produto.codigo)


def percurso_pre_order():
    print("\n--- PERCURSO PRE-ORDER ---")

    raiz = produto_service.arvore.raiz

    if raiz is None:
        print("Nenhum produto cadastrado.")
        return

    produto_service.arvore.percurso_pre_order(raiz)


def percurso_post_order():
    print("\n--- PERCURSO POST-ORDER ---")

    raiz = produto_service.arvore.raiz

    if raiz is None:
        print("Nenhum produto cadastrado.")
        return

    produto_service.arvore.percurso_post_order(raiz)


def menu_produtos():
    while True:
        print("\n===== PRODUTOS =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Alterar")
        print("5 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            alterar_produto()
        elif opcao == "5":
            remover_produto()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_fornecedores():
    while True:
        print("\n===== FORNECEDORES =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Alterar")
        print("5 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_fornecedor()
        elif opcao == "2":
            listar_fornecedores()
        elif opcao == "3":
            buscar_fornecedor()
        elif opcao == "4":
            alterar_fornecedor()
        elif opcao == "5":
            remover_fornecedor()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_estoque():
    while True:
        print("\n===== ESTOQUE =====")
        print("1 - Entrada")
        print("2 - Saída")
        print("3 - Histórico")
        print("4 - Desfazer última movimentação")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            entrada_estoque()
        elif opcao == "2":
            saida_estoque()
        elif opcao == "3":
            listar_movimentacoes()
        elif opcao == "4":
            desfazer_movimentacao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        print("\n===== RELATÓRIOS =====")
        print("1 - Produtos por nome")
        print("2 - Produtos por quantidade")
        print("3 - Produtos para reposição")
        print("4 - Percurso In-Order")
        print("5 - Percurso Pre-Order")
        print("6 - Percurso Post-Order")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            produtos_por_nome()
        elif opcao == "2":
            produtos_por_quantidade()
        elif opcao == "3":
            mostrar_reposicao()
        elif opcao == "4":
            percurso_in_order()
        elif opcao == "5":
            percurso_pre_order()
        elif opcao == "6":
            percurso_post_order()
        elif opcao == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\n==============================")
        print("       ERP DE ESTOQUE")
        print("==============================")
        print("1 - Produtos")
        print("2 - Fornecedores")
        print("3 - Estoque")
        print("4 - Relatórios")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_fornecedores()
        elif opcao == "3":
            menu_estoque()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "0":
            print("\nSistema encerrado.")
            break
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu_principal()


# Declaração de autoria
# Autores: Thalles Ryan de Camargo Santos e Osvaldo da Silva Nascimento
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado

# e não para a geração integral deste código.
