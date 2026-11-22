class Produto:

    def __init__(
        self,
        codigo,
        nome,
        categoria,
        preco,
        quantidade,
        estoque_minimo,
        fornecedor
    ):

        # Valida se o código foi informado.
        if not codigo:
            raise ValueError(
                "O código do produto é obrigatório."
            )

        # Valida se o nome foi informado.
        if not nome:
            raise ValueError(
                "O nome do produto é obrigatório."
            )

        # Valida se a categoria foi informada.
        if not categoria:
            raise ValueError(
                "A categoria do produto é obrigatória."
            )

        # O preço pode ser zero, mas não negativo.
        if preco < 0:
            raise ValueError(
                "O preço não pode ser negativo."
            )

        # A quantidade pode ser zero,
        # representando um produto sem estoque.
        if quantidade < 0:
            raise ValueError(
                "A quantidade não pode ser negativa."
            )

        # O estoque mínimo também não pode ser negativo.
        if estoque_minimo < 0:
            raise ValueError(
                "O estoque mínimo não pode ser negativo."
            )

        # Valida se o fornecedor foi informado.
        if not fornecedor:
            raise ValueError(
                "O fornecedor é obrigatório."
            )

        # Armazena os dados no objeto Produto.
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo
        self.fornecedor = fornecedor