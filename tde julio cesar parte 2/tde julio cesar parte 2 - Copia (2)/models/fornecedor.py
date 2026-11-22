# Classe que representa um fornecedor do sistema.
class Fornecedor:

    def __init__(self, codigo, nome, telefone, email):

        # Verifica se o código foi informado.
        if not codigo:
            raise ValueError(
                "O código do fornecedor é obrigatório."
            )

        # Verifica se o nome foi informado.
        if not nome:
            raise ValueError(
                "O nome do fornecedor é obrigatório."
            )

        # Verifica se o telefone foi informado.
        if not telefone:
            raise ValueError(
                "O telefone do fornecedor é obrigatório."
            )

        # Verifica se o e-mail foi informado.
        if not email:
            raise ValueError(
                "O e-mail do fornecedor é obrigatório."
            )

        # Armazena os dados no objeto Fornecedor.
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.email = email