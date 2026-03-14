palavra1 = "fosh"
palavra2 = "fish"

colunas = len(palavra1)
linhas = len(palavra2)
celula = [[0 for _ in range(colunas)] for _ in range(linhas)]

def found_substring():
    for i in range(linhas):
        for j in range(colunas):
            if palavra1[i] == palavra2[j]:
               celula[i][j] = celula[i-1][j-1] + 1
            else:
                celula[i][j] = 0
    print_matrix(celula)

def found_max_substring():
    for i in range(linhas):
        for j in range(colunas):
            if palavra1[i] == palavra2[j]:
               celula[i][j] = celula[i-1][j-1] + 1
            else:
                celula[i][j] = max(celula[i][j-1], celula[i-1][j])
    print_matrix(celula)

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print('')

found_max_substring()