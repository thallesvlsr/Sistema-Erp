class FilaPrioridade:

    def __init__(self):
        self.itens = []

    def inserir(self, produto):
        self.itens.append(produto)
        self.subir(len(self.itens) - 1)

    def remover(self):
        if self.esta_vazia():
            return None

        if len(self.itens) == 1:
            return self.itens.pop()

        prioritario = self.itens[0]
        self.itens[0] = self.itens.pop()
        self.descer(0)

        return prioritario

    def prioridade(self, produto):
        if produto.quantidade == 0:
            return 3

        if produto.quantidade < produto.estoque_minimo:
            return 2

        return 1

    def subir(self, indice):
        while indice > 0:
            pai = (indice - 1) // 2

            if self.prioridade(self.itens[indice]) <= self.prioridade(self.itens[pai]):
                break

            self.itens[indice], self.itens[pai] = self.itens[pai], self.itens[indice]
            indice = pai

    def descer(self, indice):
        tamanho = len(self.itens)

        while True:
            maior = indice
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2

            if (
                esquerda < tamanho
                and self.prioridade(self.itens[esquerda])
                > self.prioridade(self.itens[maior])
            ):
                maior = esquerda

            if (
                direita < tamanho
                and self.prioridade(self.itens[direita])
                > self.prioridade(self.itens[maior])
            ):
                maior = direita

            if maior == indice:
                break

            self.itens[indice], self.itens[maior] = self.itens[maior], self.itens[indice]
            indice = maior

    def esta_vazia(self):
        return len(self.itens) == 0

    def listar(self):
        return self.itens.copy()