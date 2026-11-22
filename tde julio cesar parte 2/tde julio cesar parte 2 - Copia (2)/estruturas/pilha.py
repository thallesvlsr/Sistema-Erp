# Classe que representa uma estrutura de Pilha.
# Será utilizada para armazenar o histórico das movimentações.
class Pilha:

    def __init__(self):

        # Cria a lista interna que armazenará
        # os elementos da pilha.
        self.itens = []


    # -------------------------
    # EMPILHAR
    # -------------------------

    def empilhar(self, item):

        # Adiciona um item no topo da pilha.
        self.itens.append(item)


    # -------------------------
    # DESEMPILHAR
    # -------------------------

    # verifica se a pilha está vazia. Se estiver, retorna None
    # Caso contrário, remove e retorna o elemento do topo, que é o último adicionado.
    def desempilhar(self):

        # Verifica se a pilha está vazia.
        if self.esta_vazia():
            return None

        # Remove e retorna o elemento do topo.
        return self.itens.pop()


    # -------------------------
    # TOPO
    # -------------------------

    def topo(self):

        # Verifica se existe algum elemento.
        if self.esta_vazia():
            return None

        # Retorna o último elemento sem removê-lo.
        return self.itens[-1]


    # -------------------------
    # VERIFICAR SE ESTÁ VAZIA
    # -------------------------

    def esta_vazia(self):

        # Retorna True se a pilha estiver vazia.
        return len(self.itens) == 0


    # -------------------------
    # LISTAR
    # -------------------------

    def listar(self):

        # Retorna todos os elementos armazenados.
        return self.itens