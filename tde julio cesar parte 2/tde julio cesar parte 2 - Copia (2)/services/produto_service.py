
from estruturas.arvore_avl import ArvoreAVL
from algoritmos.ordenacao import (
    ordenar_por_nome,
    ordenar_por_quantidade
)


class ProdutoService:

    def __init__(self):
        self.arvore = ArvoreAVL()

    def cadastrar(self, produto):
        produto_existente = self.buscar_por_codigo(produto.codigo)

        if produto_existente:
            raise ValueError("Já existe um produto com esse código.")

        self.arvore.inserir(produto)

    def listar(self):
        return self.arvore.listar_produtos()

    def buscar_por_codigo(self, codigo):
        return self.arvore.buscar(codigo)

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
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            raise ValueError("Produto não encontrado.")

        produto.nome = nome
        produto.categoria = categoria
        produto.preco = preco
        produto.quantidade = quantidade
        produto.estoque_minimo = estoque_minimo
        produto.fornecedor = fornecedor

    def remover(self, codigo):
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            raise ValueError("Produto não encontrado.")

        self.arvore.remover(codigo)

    def ordenar_nome(self):
        return ordenar_por_nome(self.listar())

    def ordenar_quantidade(self):
        return ordenar_por_quantidade(self.listar())
