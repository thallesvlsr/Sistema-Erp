from models.movimentacao import Movimentacao
from estruturas.pilha import Pilha


class EstoqueService:

    def __init__(self, produto_service):
        self.produto_service = produto_service
        self.historico = Pilha()

    def entrada(self, codigo_produto, quantidade, motivo):

        produto = self.produto_service.buscar_por_codigo(
            codigo_produto
        )

        if not produto:
            raise ValueError("Produto não encontrado.")

        if quantidade <= 0:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        produto.quantidade += quantidade

        movimentacao = Movimentacao(
            produto,
            "entrada",
            quantidade,
            motivo
        )

        self.historico.empilhar(movimentacao)

    def saida(self, codigo_produto, quantidade, motivo):

        produto = self.produto_service.buscar_por_codigo(
            codigo_produto
        )

        if not produto:
            raise ValueError("Produto não encontrado.")

        if quantidade <= 0:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        if quantidade > produto.quantidade:
            raise ValueError("Estoque insuficiente.")

        produto.quantidade -= quantidade

        movimentacao = Movimentacao(
            produto,
            "saida",
            quantidade,
            motivo
        )

        self.historico.empilhar(movimentacao)

    def listar_historico(self):
        return self.historico.listar()

    def desfazer_ultima_movimentacao(self):

        movimentacao = self.historico.topo()

        if movimentacao is None:
            raise ValueError(
                "Não há movimentações para desfazer."
            )

        produto = movimentacao.produto

        if movimentacao.tipo == "entrada":

            if movimentacao.quantidade > produto.quantidade:
                raise ValueError(
                    "Não é possível desfazer essa entrada."
                )

            produto.quantidade -= movimentacao.quantidade

        elif movimentacao.tipo == "saida":

            produto.quantidade += movimentacao.quantidade

        self.historico.desempilhar()

        return movimentacao