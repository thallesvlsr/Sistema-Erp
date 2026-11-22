from estruturas.lista import Lista
from algoritmos.busca_binaria import busca_binaria_por_codigo
from algoritmos.ordenacao import ordenar_por_codigo


class FornecedorService:

    def __init__(self):
        self.fornecedores = Lista()


    # -------------------------
    # CADASTRAR
    # -------------------------

    def cadastrar(self, fornecedor):

        fornecedor_existente = self.buscar_por_codigo(
            fornecedor.codigo
        )

        if fornecedor_existente:
            raise ValueError(
                "Já existe um fornecedor com esse código."
            )

        self.fornecedores.inserir(fornecedor)


    # -------------------------
    # LISTAR
    # -------------------------

    def listar(self):

        return self.fornecedores.listar()


    # -------------------------
    # BUSCAR POR CÓDIGO
    # -------------------------

    def buscar_por_codigo(self, codigo):

        lista_ordenada = ordenar_por_codigo(
            self.fornecedores.listar()
        )

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
        telefone,
        email
    ):

        fornecedor = self.buscar_por_codigo(codigo)

        if not fornecedor:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        fornecedor.nome = nome
        fornecedor.telefone = telefone
        fornecedor.email = email


    # -------------------------
    # REMOVER
    # -------------------------

    def remover(self, codigo):

        fornecedor = self.buscar_por_codigo(codigo)

        if not fornecedor:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        self.fornecedores.remover(fornecedor)