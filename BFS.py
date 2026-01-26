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
        if not pessoa in ja_verificadas:
            if pessoa_e_vendendor(pessoa):
                print(f"{pessoa} é um vendedor de mangas")
                return
            else:
                print(pessoa)
                fila_de_pesquisa += grafo[pessoa]
                ja_verificadas.append(pessoa)


def pessoa_e_vendendor(nome):
    return nome[-1] == "j"

bfs("Eu")