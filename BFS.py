from collections import deque

grafo = {}

grafo["Eu"] = ["Claire", "Bob", "Alice"]
grafo["Bob"] = ["Anuj", "Peggy"]
grafo["Claire"] = ["Thom", "Jonny"]
grafo["Alice"] = ["Peggy"]
grafo["Peggy"] = []
grafo["Jonny"] = []
grafo["Thom"] = []
grafo["Anuj"] = []

def bfs(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    ja_verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        print(pessoa)
        if not pessoa in ja_verificadas:
            if pessoa_e_vendendor(pessoa):
                return
            else:
                fila_de_pesquisa += grafo[pessoa]
                ja_verificadas.append(pessoa)

def pessoa_e_vendendor(nome):
    return nome[-1] == "j"

def dfs(nome):
    stack = grafo[nome]
    ja_verificadas = set()

    while stack:
        pessoa = stack.pop()
        if not pessoa in ja_verificadas:
            print(pessoa)
            if pessoa_e_vendendor(pessoa):
                return

            stack.extend(grafo.get(pessoa, []))
            ja_verificadas.add(pessoa)

dfs("Eu")