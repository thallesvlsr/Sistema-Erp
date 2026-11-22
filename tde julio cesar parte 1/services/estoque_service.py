from models.movimentacao import Movimentacao
from estruturas.pilha import Pilha


class EstoqueService:

    def __init__(self, produto_service):

        self.produto_service = produto_service
        self.historico = Pilha()


    # -------------------------
    # ENTRADA
    # -------------------------

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

        # essa linha adiciona a movimentação recém-realizada ao histórico
        # Como o histórico é uma pilha, a última movimentação registrada será a primeira a sair quando o programa executar desempilhar()
        self.historico.empilhar(movimentacao)


    # -------------------------
    # SAÍDA
    # -------------------------

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


    # -------------------------
    # LISTAR HISTÓRICO
    # -------------------------

    # devolve as movimentações armazenadas na pilha para que o programa possa exibi-las.
    def listar_historico(self):

        return self.historico.listar()


    # -------------------------
    # DESFAZER ÚLTIMA MOVIMENTAÇÃO
    # -------------------------

    def desfazer_ultima_movimentacao(self):

        movimentacao = self.historico.topo()

        if movimentacao is None:
            raise ValueError(
                "Não há movimentações para desfazer."
            )

        # pega o produto associado à ultima movimentação e o guarda na variável produto.
        produto = movimentacao.produto

        # Se foi entrada, desfazer retira a quantidade.
        if movimentacao.tipo == "entrada":

            # antes de desfazer uma entrada, o código verifica se o estoque atual tem unidades
            # suficientes para retirar a quantidade daquela entrada. Se não tiver, gera um erro e impede a operação.
            if movimentacao.quantidade > produto.quantidade:
                raise ValueError(
                    "Não é possível desfazer essa entrada."
                )

            produto.quantidade -= movimentacao.quantidade

        # Se foi saída, desfazer devolve a quantidade.
        elif movimentacao.tipo == "saida":

            produto.quantidade += movimentacao.quantidade

        # Depois de corrigir a quantidade do produto, essa linha remove a última movimentação da pilha do histórico.
        self.historico.desempilhar()

        return movimentacao