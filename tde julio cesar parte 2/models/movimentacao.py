# Classe que representa uma movimentação realizada no estoque.
class Movimentacao:

    def __init__(self, produto, tipo, quantidade, motivo):

        # Verifica se um produto foi informado.
        if not produto:
            raise ValueError(
                "O produto é obrigatório."
            )

        # Verifica se o tipo foi informado.
        if not tipo:
            raise ValueError(
                "O tipo da movimentação é obrigatório."
            )

        # Permite somente movimentações de entrada ou saída.
        if tipo != "entrada" and tipo != "saida":
            raise ValueError(
                "O tipo da movimentação deve ser 'entrada' ou 'saida'."
            )

        # A quantidade movimentada deve ser maior que zero.
        if quantidade <= 0:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        # Toda movimentação precisa possuir um motivo.
        if not motivo:
            raise ValueError(
                "O motivo da movimentação é obrigatório."
            )

        # Armazena os dados da movimentação.
        self.produto = produto
        self.tipo = tipo
        self.quantidade = quantidade
        self.motivo = motivo