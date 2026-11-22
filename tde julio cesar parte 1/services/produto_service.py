from estruturas.lista import Lista
from algoritmos.busca_binaria import busca_binaria_por_codigo
from algoritmos.ordenacao import (
    ordenar_por_codigo,
    ordenar_por_nome,
    ordenar_por_quantidade
)


# Classe responsável pelas operações relacionadas aos produtos.
class ProdutoService:

    def __init__(self):

        # Estrutura utilizada para armazenar os produtos.
        self.produtos = Lista()


    # -------------------------
    # CADASTRAR
    # -------------------------

    def cadastrar(self, produto):

        # Verifica através da busca binária
        # se já existe um produto com esse código.
        produto_existente = self.buscar_por_codigo(
            produto.codigo
        )

        if produto_existente:
            raise ValueError(
                "Já existe um produto com esse código."
            )

        # Insere o produto na lista.
        self.produtos.inserir(produto)


    # -------------------------
    # LISTAR
    # -------------------------

    def listar(self):

        # Retorna todos os produtos cadastrados.
        return self.produtos.listar()


    # -------------------------
    # BUSCAR POR CÓDIGO
    # -------------------------

    def buscar_por_codigo(self, codigo):

        # Primeiro ordena uma cópia da lista pelo código.
        # Isso é necessário para utilizar a busca binária.
        lista_ordenada = ordenar_por_codigo(
            self.produtos.listar()
        )

        # Realiza a busca binária na lista ordenada.
        return busca_binaria_por_codigo(
            lista_ordenada,
            codigo
        )


    # -------------------------
    # ALTERAR
    # -------------------------

    def alterar(
        self,
        codigo,
        nome,
        categoria,
        preco,
        quantidade,
        estoque_minimo,
        fornecedor
    ):

        # Localiza o produto através da busca binária.
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            raise ValueError(
                "Produto não encontrado."
            )

        # Altera os dados do objeto encontrado.
        produto.nome = nome
        produto.categoria = categoria
        produto.preco = preco
        produto.quantidade = quantidade
        produto.estoque_minimo = estoque_minimo
        produto.fornecedor = fornecedor


    # -------------------------
    # REMOVER
    # -------------------------

    def remover(self, codigo):

        # Localiza o produto através da busca binária.
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            raise ValueError(
                "Produto não encontrado."
            )

        # Remove o objeto da lista original.
        self.produtos.remover(produto)


    # -------------------------
    # ORDENAR POR NOME
    # -------------------------

    def ordenar_nome(self):

        return ordenar_por_nome(
            self.produtos.listar()
        )


    # -------------------------
    # ORDENAR POR QUANTIDADE
    # -------------------------

    def ordenar_quantidade(self):

        return ordenar_por_quantidade(
            self.produtos.listar()
        )