grafo = {
    "Inicio": {
        "A": 6,
        "B": 2
    },
    "A": {
        "Fim": 1
    },
    "B": {
        "A": 3,
        "Fim": 5
    },
    "Fim": {}
}

custos = {
    "A": 6,
    "B": 2,
    "Fim": float("inf")
}

pais = {
    "A": "Inicio",
    "B": "Inicio",
    "Fim": None
}

processados = []


def dijkstra():
    node = ache_custo_mais_baixo(custos)
    while node is not None:
        custo = custos[node]
        vizinhos = grafo[node]
        for n in vizinhos.keys():
            print(n)
            novo_custo = custo + vizinhos[n]
            if novo_custo < custos[n]:
                custos[n] = novo_custo
                pais[n] = node
        processados.append(node)
        node = ache_custo_mais_baixo(custos)

def ache_custo_mais_baixo(custos):
    node_custo_mais_baixo = None
    custo_mais_baixo = float("inf")
    
    for node in custos:
        custo = custos[node]
        if custo < custo_mais_baixo and node not in processados:
            custo_mais_baixo = custo
            node_custo_mais_baixo = node
    return node_custo_mais_baixo

dijkstra()