from estruturas.fila_prioridade import FilaPrioridade


# Classe responsável por identificar
# os produtos que precisam de reposição.
class ReposicaoService:

    def __init__(self, produto_service):

        # Recebe o ProdutoService para acessar
        # os produtos cadastrados no sistema.
        self.produto_service = produto_service


    # -------------------------
    # GERAR FILA DE REPOSIÇÃO
    # -------------------------

    def gerar_fila_reposicao(self):

        # Cria uma nova fila de prioridade.
        fila = FilaPrioridade()

        # Obtém todos os produtos cadastrados.
        produtos = self.produto_service.listar()

        # Percorre todos os produtos.
        for produto in produtos:

            # Verifica se o produto está
            # abaixo do estoque mínimo.
            if produto.quantidade < produto.estoque_minimo:

                # Adiciona o produto à fila de reposição.
                fila.inserir(produto)

        # Retorna a fila pronta.
        return fila