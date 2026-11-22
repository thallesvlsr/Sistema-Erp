from types import SimpleNamespace

from algoritmos.ordenacao import (
    ordenar_por_codigo,
    ordenar_por_nome,
    ordenar_por_quantidade,
    merge_sort
)


def criar_produto(codigo, nome, quantidade):
    return SimpleNamespace(
        codigo=codigo,
        nome=nome,
        quantidade=quantidade
    )


def testar_ordenacao():
    print("===== TESTES DOS ALGORITMOS DE ORDENAÇÃO =====")

    produtos = [
        criar_produto(30, "Teclado", 8),
        criar_produto(10, "Monitor", 2),
        criar_produto(50, "Mouse", 15),
        criar_produto(20, "Headset", 0),
        criar_produto(40, "Webcam", 8)
    ]

    # Ordenação por código
    resultado = ordenar_por_codigo(produtos)
    assert [p.codigo for p in resultado] == [10, 20, 30, 40, 50]
    print("[OK] Ordenação por código")

    # Ordenação por nome
    resultado = ordenar_por_nome(produtos)
    assert [p.nome for p in resultado] == [
        "Headset", "Monitor", "Mouse", "Teclado", "Webcam"
    ]
    print("[OK] Ordenação por nome")

    # Ordenação por quantidade
    resultado = ordenar_por_quantidade(produtos)
    assert [p.quantidade for p in resultado] == [15, 8, 8, 2, 0]
    print("[OK] Ordenação por quantidade")

    # Merge Sort
    resultado = merge_sort(produtos)
    assert [p.codigo for p in resultado] == [10, 20, 30, 40, 50]
    print("[OK] Merge Sort")

    # Lista vazia
    assert ordenar_por_codigo([]) == []
    assert ordenar_por_nome([]) == []
    assert ordenar_por_quantidade([]) == []
    assert merge_sort([]) == []
    print("[OK] Testes com listas vazias")

    # Apenas um produto
    unico = [criar_produto(99, "Produto único", 3)]

    assert ordenar_por_codigo(unico)[0].codigo == 99
    assert ordenar_por_nome(unico)[0].nome == "Produto único"
    assert ordenar_por_quantidade(unico)[0].quantidade == 3
    assert merge_sort(unico)[0].codigo == 99
    print("[OK] Testes com um único produto")

    # Valores repetidos
    repetidos = [
        criar_produto(5, "Produto A", 4),
        criar_produto(2, "Produto B", 4),
        criar_produto(5, "Produto C", 4),
        criar_produto(2, "Produto D", 4)
    ]

    resultado = merge_sort(repetidos)
    assert [p.codigo for p in resultado] == [2, 2, 5, 5]
    print("[OK] Merge Sort com códigos repetidos")

    # Verificar estabilidade do Merge Sort
    assert [p.nome for p in resultado] == [
        "Produto B", "Produto D", "Produto A", "Produto C"
    ]
    print("[OK] Merge Sort preserva a ordem dos elementos empatados")

    # Verificar se as listas originais continuam intactas
    assert [p.codigo for p in produtos] == [30, 10, 50, 20, 40]
    print("[OK] Listas originais preservadas")

    print("\nTODOS OS TESTES DE ORDENAÇÃO PASSARAM!")


if __name__ == "__main__":
    testar_ordenacao()