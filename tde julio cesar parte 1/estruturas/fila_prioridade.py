# Classe que representa uma Fila de Prioridade.
# Será utilizada para organizar os produtos
# que precisam de reposição de estoque.
class FilaPrioridade:

    # __init__: é um método especial que o Python executa automaticamente quando criamos um objeto.
    # self representa o próprio objeto que está sendo criado. 
    # É por meio dele que guardamos informações e acessamos métodos desse objeto.
    def __init__(self):

        # Cria a lista interna que armazenará os produtos.
        self.itens = []

    # cria um método que recebe um produto e permite adicioná-lo à lista do objeto.
    def inserir(self, produto):

        # pega o produto recebido e o adiciona ao final da lista itens que pertence à fila
        self.itens.append(produto)

    # define o método responsável por remover um elemento do objeto.
    # O que será removido e de qual posição depende do código escrito dentro desse método.
    def remover(self):

        # Se a fila estiver vazia,
        # não existe produto para remover.
        if self.esta_vazia():
            return None

       # esse código percorre a fila, guarda a posição do produto de maior prioridade e, no final 
       # remove e retorna esse produto para que ele seja tratado primeiro na reposição.
        indice_prioritario = 0

        # Percorre os outros produtos da fila.
        for i in range(1, len(self.itens)):

            # Compara a prioridade dos produtos.
            if self.prioridade(self.itens[i]) > self.prioridade(
                self.itens[indice_prioritario]
            ):
                indice_prioritario = i

        # Remove e retorna o produto de maior prioridade.
        return self.itens.pop(indice_prioritario)

    def prioridade(self, produto):

        # Produto com estoque zerado:
        # prioridade máxima.
        if produto.quantidade == 0:
            return 3

        # Produto abaixo do estoque mínimo:
        # segunda maior prioridade.
        if produto.quantidade < produto.estoque_minimo:
            return 2

        # Produto com estoque normal:
        # prioridade menor.
        return 1


    # -------------------------
    # VERIFICAR SE ESTÁ VAZIA
    # -------------------------

    # verifica se a fila tem zero elementos e retorna True 
    # se estiver vazia ou False se tiver algum produto.
    def esta_vazia(self):

        return len(self.itens) == 0


    # -------------------------
    # LISTAR
    # -------------------------

    # devolve os elementos armazenados em self.itens, 
    # permitindo que outra parte do ERP consulte e mostre os produtos.
    def listar(self):

        return self.itens