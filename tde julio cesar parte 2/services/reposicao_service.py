
from estruturas.fila_prioridade import FilaPrioridade
from algoritmos.ordenacao import merge_sort


class ReposicaoService:

    def __init__(self, produto_service):
        self.produto_service = produto_service

    def gerar_fila_reposicao(self):

        fila = FilaPrioridade()

        produtos = self.produto_service.listar()

        produtos = merge_sort(produtos)

        for produto in produtos:

            if produto.quantidade < produto.estoque_minimo:
                fila.inserir(produto)

        return fila