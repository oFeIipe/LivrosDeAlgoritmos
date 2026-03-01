estados_abranger = set(['sp', 'mg', 'rj', 'es', 'mt', 'ms', 'ba', 'pe', 'go'])


estacoes = {}

estacoes['kum'] = set(['rj', 'pe', 'go'])
estacoes['kdois'] = set(['sp', 'mg', 'go'])
estacoes['ktres'] = set(['rj', 'mt', 'ba'])
estacoes['kquatro'] = set(['es', 'ms', 'ba'])
estacoes['kcinco'] = set(['pe', 'sp', 'rj'])

estacoes_final = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estacoes_final.add(melhor_estacao)
    estados_abranger -= estados_cobertos
print(estacoes_final)