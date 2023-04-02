import conjuntos as conj


def repMatriz(A, R):
    # A partir de uma relação R de um conjunto A é montado e retornada a matriz de zero-um que representa os pares ordenados de R
    n = len(A)
    MatrizR = [[0 for i in range(n)] for j in range(n)]
    for (i, j) in R:
        ii = A.index(i)
        jj = A.index(j)
        MatrizR[ii][jj] = 1
    return MatrizR


def fechoReflexivo(MatrizR):
    # Calcula o fecho reflexivo a partir de uma matrizR
    FR = [[e for e in l] for l in MatrizR]
    for i in range(len(FR)):
        FR[i][i] = 1
    return FR


def fechoSimetrico(MatrizR):
    # Calcula o fecho simétrico a partir de uma matrizR
    FS = [[e for e in l] for l in MatrizR]
    for i in range(len(FS)):
        for j in range(len(FS[i])):
            if FS[i][j] == 1:
                FS[j][i] = 1
    return FS


def compose(A, B):
    # Faz a composição de duas matrizes zero-um
    if len(A) != len(B):
        return []
    M = []
    for i in range(len(A)):
        Li = []
        for j in range(len(A)):
            put = 0
            for k in range(len(A)):
                if A[i][k] == B[k][j] and A[i][k] == 1:
                    put = 1
                    break
            Li.append(put)
        M.append(Li)
    return M


def fechoTransitivoRosen(MatrizR, debug=False):
    # Calcula o fecho transitivo a partir de uma matrizR usando o algoritmo descrito na página 550 do livro do Rosen
    Mr = [[e for e in l] for l in MatrizR]
    FT = [[e for e in l] for l in MatrizR]
    if debug == True:
        print(f"Mr1 = {Mr}")
    for e in range(1, len(MatrizR)):
        Mr = compose(Mr, MatrizR)
        if debug == True:
            print(f"Mr{e+1} = {Mr}")
        for i in range(len(Mr)):
            for j in range(len(Mr[i])):
                if Mr[i][j] == 1:
                    FT[i][j] = 1
    return FT


def fechoTransitivoWarshall(MatrizR):
    # Calcula o fecho transitivo a partir de uma matrizR usando o algoritmo de Warshal descrito na página 553 do livro do Rosen
    W = [[e for e in l] for l in MatrizR]
    for k in range(len(W)):
        for i in range(len(W)):
            for j in range(len(W[i])):
                if W[i][j] == 0 and (W[i][k] == 1 and W[k][j] == 1):
                    W[i][j] = 1
    return W


def menorREquivalencia(MatrizR):
    # Calcula o fecho de equivalência de uma matrizR
    return fechoSimetrico(fechoReflexivo(fechoTransitivoWarshall(MatrizR)))


def imprimeParesOrdenados(A, MatrizR, prt=True):
    # Imprime uma lista de pares ordenados representados em uma matriz de zero-um
    # @arg prt - Pode ser definido para False então a função apenas retornará a lista sem imprimir
    paresR = [(A[i], A[j]) for i in range(len(MatrizR))
              for j in range(len(MatrizR[i])) if MatrizR[i][j] == 1]
    if prt:
        print(paresR)
    return paresR


if __name__ == "__main__":
    A = [1, 2, 5, 12]
    R = [(1, 2), (1, 12), (5, 1), (5, 2), (12, 5)]
    print(f"A = {A}\nR = {R}")

    M = repMatriz(A, R)
    print(f"M = {M}")
    print(f"M = {imprimeParesOrdenados(A, M, False)}")

    FR = fechoReflexivo(M)
    FR = imprimeParesOrdenados(A, FR, False)
    print(f"({conj.reflexiva(set(FR), A)})FR = {FR}")

    FS = fechoSimetrico(M)
    FS = imprimeParesOrdenados(A, FS, False)
    print(f"({conj.simetrica(set(FS))})FS = {FS}")

    FT = fechoTransitivoRosen(M)
    FT = imprimeParesOrdenados(A, FT, False)
    print(f"({conj.transitiva(set(FT))})FT = {FT}")

    FTW = fechoTransitivoWarshall(M)
    FTW = imprimeParesOrdenados(A, FTW, False)
    print(f"({conj.transitiva(set(FTW))})FTW = {FTW}")

    FE = menorREquivalencia(M)
    FE = imprimeParesOrdenados(A, FE, False)
    print(f"({conj.equivalencia(set(FE), A)})FE = {FE}")
