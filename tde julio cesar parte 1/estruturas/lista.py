# Classe que representa uma estrutura de Lista.
# Será utilizada para armazenar produtos e fornecedores.
class Lista:

    def __init__(self):

        # Cria a lista interna que armazenará os objetos.
        self.itens = []


    # -------------------------
    # INSERIR
    # -------------------------

    def inserir(self, item):

        # Adiciona um novo item à lista.
        self.itens.append(item)


    # -------------------------
    # REMOVER
    # -------------------------

    def remover(self, item):

        # Remove o item informado da lista.
        self.itens.remove(item)


    # -------------------------
    # TAMANHO
    # -------------------------

    def tamanho(self):

        # Retorna a quantidade de elementos armazenados.
        return len(self.itens)


    # -------------------------
    # LISTAR
    # -------------------------

    def listar(self):

        # Retorna todos os elementos armazenados.
        return self.itens