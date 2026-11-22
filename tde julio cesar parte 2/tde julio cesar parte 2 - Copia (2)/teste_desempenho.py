"""
TESTE DE DESEMPENHO - ERP DE ESTOQUE
Coloque este arquivo na pasta raiz do projeto da PARTE 2,
no mesmo nível das pastas algoritmos, estruturas, models e services.

Execute com:
    python teste_desempenho.py

O teste compara:
1. Busca: Parte 1 (Insertion Sort + Busca Binária) x Parte 2 (AVL)
2. Fila: Parte 1 (lista com busca linear) x Parte 2 (heap binário)
3. Ordenação: Parte 1 (Insertion Sort) x Parte 2 (Merge Sort)

Cada medição é repetida 5 vezes. Os tempos são médias em milissegundos.
"""

import csv
import random
import statistics
import time
from types import SimpleNamespace

from estruturas.arvore_avl import ArvoreAVL
from estruturas.fila_prioridade import FilaPrioridade
from algoritmos.busca_binaria import busca_binaria_por_codigo
from algoritmos.ordenacao import merge_sort


REPETICOES = 5
TAMANHOS = [100, 1000, 10000]
SEMENTE = 2026


def criar_produtos(quantidade):
    produtos = []
    for i in range(quantidade):
        # Código com zeros à esquerda para manter a ordem numérica e textual.
        codigo = str(i).zfill(8)
        produtos.append(
            SimpleNamespace(
                codigo=codigo,
                nome=f"Produto {codigo}",
                categoria="Teste",
                preco=10.0,
                quantidade=(i % 8),
                estoque_minimo=5,
                fornecedor="Fornecedor teste",
            )
        )

    random.Random(SEMENTE + quantidade).shuffle(produtos)
    return produtos


# -------------------------
# IMPLEMENTAÇÃO DA PARTE 1
# -------------------------

def insertion_sort_codigo(produtos):
    lista = produtos.copy()

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j].codigo > atual.codigo:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista


class FilaPrioridadeParte1:
    """Fila da Parte 1: lista e procura linear do item prioritário."""

    def __init__(self):
        self.itens = []

    def inserir(self, produto):
        self.itens.append(produto)

    def prioridade(self, produto):
        if produto.quantidade == 0:
            return 3
        if produto.quantidade < produto.estoque_minimo:
            return 2
        return 1

    def remover(self):
        if not self.itens:
            return None

        indice_prioritario = 0
        for i in range(1, len(self.itens)):
            if self.prioridade(self.itens[i]) > self.prioridade(
                self.itens[indice_prioritario]
            ):
                indice_prioritario = i

        return self.itens.pop(indice_prioritario)


# -------------------------
# MEDIÇÃO
# -------------------------

def medir(funcao, repeticoes=REPETICOES):
    tempos = []

    for _ in range(repeticoes):
        inicio = time.perf_counter()
        funcao()
        fim = time.perf_counter()
        tempos.append((fim - inicio) * 1000)

    return statistics.mean(tempos)


def medir_busca(produtos):
    codigo_procurado = str(len(produtos) // 2).zfill(8)

    # Parte 1: reproduz o fluxo do serviço: ordenar a lista e então buscar.
    def busca_parte1():
        lista_ordenada = insertion_sort_codigo(produtos)
        return busca_binaria_por_codigo(lista_ordenada, codigo_procurado)

    # Parte 2: a árvore é montada fora do cronômetro; mede a busca na AVL.
    arvore = ArvoreAVL()
    for produto in produtos:
        arvore.inserir(produto)

    def busca_parte2():
        return arvore.buscar(codigo_procurado)

    tempo1 = medir(busca_parte1)
    tempo2 = medir(busca_parte2)

    return tempo1, tempo2


def medir_fila(produtos):
    # Mede o fluxo completo: montar a fila com os produtos que precisam
    # de reposição e retirar todos em ordem de prioridade.
    def processar_parte1():
        fila = FilaPrioridadeParte1()
        for produto in produtos:
            if produto.quantidade < produto.estoque_minimo:
                fila.inserir(produto)

        while fila.remover() is not None:
            pass

    def processar_parte2():
        fila = FilaPrioridade()
        for produto in produtos:
            if produto.quantidade < produto.estoque_minimo:
                fila.inserir(produto)

        while fila.remover() is not None:
            pass

    tempo1 = medir(processar_parte1)
    tempo2 = medir(processar_parte2)

    return tempo1, tempo2


def medir_ordenacao(produtos):
    tempo1 = medir(lambda: insertion_sort_codigo(produtos))
    tempo2 = medir(lambda: merge_sort(produtos))
    return tempo1, tempo2


def executar():
    resultados = []

    print("\n========== TESTE DE DESEMPENHO ==========")
    print(f"Repetições por medição: {REPETICOES}")
    print("Os valores abaixo são médias em milissegundos.\n")

    for quantidade in TAMANHOS:
        print(f"\nTestando {quantidade:,} produtos...".replace(",", "."))
        produtos = criar_produtos(quantidade)

        busca1, busca2 = medir_busca(produtos)
        fila1, fila2 = medir_fila(produtos)
        ordem1, ordem2 = medir_ordenacao(produtos)

        resultados.extend([
            [quantidade, "Busca por código", "Parte 1", busca1],
            [quantidade, "Busca por código", "Parte 2", busca2],
            [quantidade, "Processamento completo da fila de reposição", "Parte 1", fila1],
            [quantidade, "Processamento completo da fila de reposição", "Parte 2", fila2],
            [quantidade, "Ordenação por código", "Parte 1", ordem1],
            [quantidade, "Ordenação por código", "Parte 2", ordem2],
        ])

        print(f"Busca - Parte 1: {busca1:.4f} ms | Parte 2: {busca2:.4f} ms")
        print(f"Fila  - Parte 1: {fila1:.4f} ms | Parte 2: {fila2:.4f} ms")
        print(f"Ordem - Parte 1: {ordem1:.4f} ms | Parte 2: {ordem2:.4f} ms")

    nome_csv = "resultados_desempenho.csv"
    with open(nome_csv, "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["Quantidade de produtos", "Operação", "Versão", "Média (ms)"])
        escritor.writerows(resultados)

    print(f"\nArquivo gerado: {nome_csv}")
    print("Abra o CSV no Excel para consultar os resultados.")

    # Gráficos são opcionais: o teste e o CSV funcionam sem matplotlib.
    try:
        import matplotlib.pyplot as plt

        operacoes = [
            "Busca por código",
            "Processamento completo da fila de reposição",
            "Ordenação por código",
        ]

        for operacao in operacoes:
            fig, ax = plt.subplots()
            for versao in ("Parte 1", "Parte 2"):
                xs = []
                ys = []
                for linha in resultados:
                    if linha[1] == operacao and linha[2] == versao:
                        xs.append(str(linha[0]))
                        ys.append(linha[3])
                ax.plot(xs, ys, marker="o", label=versao)

            ax.set_title(operacao)
            ax.set_xlabel("Quantidade de produtos")
            ax.set_ylabel("Tempo médio (ms)")
            ax.legend()
            ax.grid(True)
            fig.tight_layout()
            arquivo_grafico = (
                "grafico_" + str(operacoes.index(operacao) + 1) + ".png"
            )
            fig.savefig(arquivo_grafico)
            plt.close(fig)
            print(f"Gráfico gerado: {arquivo_grafico}")

    except ImportError:
        print("\nMatplotlib não está instalado. Os resultados CSV foram salvos.")
        print("Se quiser os gráficos, instale com: pip install matplotlib")


if __name__ == "__main__":
    executar()
