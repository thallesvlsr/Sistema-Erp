
class NoAVL:

    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:

    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0

        return no.altura

    def fator_balanceamento(self, no):
        if no is None:
            return 0

        return self.altura(no.esquerda) - self.altura(no.direita)

    def atualizar_altura(self, no):
        if no is None:
            return

        no.altura = 1 + max(
            self.altura(no.esquerda),
            self.altura(no.direita)
        )

    def rotacao_direita(self, y):
        x = y.esquerda
        auxiliar = x.direita

        x.direita = y
        y.esquerda = auxiliar

        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        auxiliar = y.esquerda

        y.esquerda = x
        x.direita = auxiliar

        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

    def rotacao_esquerda_direita(self, no):
        no.esquerda = self.rotacao_esquerda(no.esquerda)
        return self.rotacao_direita(no)

    def rotacao_direita_esquerda(self, no):
        no.direita = self.rotacao_direita(no.direita)
        return self.rotacao_esquerda(no)

    def inserir(self, produto):
        self.raiz = self._inserir(self.raiz, produto)

    def _inserir(self, no, produto):

        if no is None:
            return NoAVL(produto)

        if produto.codigo < no.produto.codigo:
            no.esquerda = self._inserir(no.esquerda, produto)

        elif produto.codigo > no.produto.codigo:
            no.direita = self._inserir(no.direita, produto)

        else:
            return no

        self.atualizar_altura(no)

        balanceamento = self.fator_balanceamento(no)

        if balanceamento > 1 and produto.codigo < no.esquerda.produto.codigo:
            return self.rotacao_direita(no)

        if balanceamento < -1 and produto.codigo > no.direita.produto.codigo:
            return self.rotacao_esquerda(no)

        if balanceamento > 1 and produto.codigo > no.esquerda.produto.codigo:
            return self.rotacao_esquerda_direita(no)

        if balanceamento < -1 and produto.codigo < no.direita.produto.codigo:
            return self.rotacao_direita_esquerda(no)

        return no

    def buscar(self, codigo):
        atual = self.raiz

        while atual is not None:

            if codigo == atual.produto.codigo:
                return atual.produto

            elif codigo < atual.produto.codigo:
                atual = atual.esquerda

            else:
                atual = atual.direita

        return None

    def menor_valor(self, no):
        atual = no

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual

    def remover(self, codigo):
        self.raiz = self._remover(self.raiz, codigo)

    def _remover(self, no, codigo):

        if no is None:
            return None

        if codigo < no.produto.codigo:
            no.esquerda = self._remover(no.esquerda, codigo)

        elif codigo > no.produto.codigo:
            no.direita = self._remover(no.direita, codigo)

        else:

            if no.esquerda is None and no.direita is None:
                return None

            elif no.esquerda is None:
                return no.direita

            elif no.direita is None:
                return no.esquerda

            sucessor = self.menor_valor(no.direita)

            no.produto = sucessor.produto

            no.direita = self._remover(
                no.direita,
                sucessor.produto.codigo
            )

        self.atualizar_altura(no)

        balanceamento = self.fator_balanceamento(no)

        if balanceamento > 1 and self.fator_balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)

        if balanceamento > 1 and self.fator_balanceamento(no.esquerda) < 0:
            return self.rotacao_esquerda_direita(no)

        if balanceamento < -1 and self.fator_balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)

        if balanceamento < -1 and self.fator_balanceamento(no.direita) > 0:
            return self.rotacao_direita_esquerda(no)

        return no

    def percurso_in_order(self, no, produtos):
        if no is not None:
            self.percurso_in_order(no.esquerda, produtos)
            produtos.append(no.produto)
            self.percurso_in_order(no.direita, produtos)

    def listar_produtos(self):
        produtos = []
        self.percurso_in_order(self.raiz, produtos)
        return produtos

    def percurso_pre_order(self, no):
        if no is not None:
            print(no.produto.codigo)
            self.percurso_pre_order(no.esquerda)
            self.percurso_pre_order(no.direita)

    def percurso_post_order(self, no):
        if no is not None:
            self.percurso_post_order(no.esquerda)
            self.percurso_post_order(no.direita)
            print(no.produto.codigo)