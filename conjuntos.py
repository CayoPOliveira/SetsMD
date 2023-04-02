import time
import matplotlib.pyplot as plt


def iniciar_contador():
    # Inicia um contador para o tempo
    global inicio
    inicio = time.time()


def terminar_contador():
    # Termina o contador e retorna
    global inicio
    fim = time.time()
    tempo_decorrido = fim - inicio
    return tempo_decorrido


def simetrica(relacao):
    # Função para verificar se uma relação é simétrica
    for (a, b) in relacao:
        if (b, a) not in relacao:
            return False
    return True


def transitiva(relacao):
    # Função para verificar se uma relação é transitiva
    for (a, b) in relacao:
        for (c, d) in relacao:
            if b == c and (a, d) not in relacao:
                return False
    return True


def reflexiva(relacao, A):
    # Verifica se uma relação é reflexiva
    for a in A:
        if (a, a) not in relacao:
            return False
    return True


def equivalencia(relacao, A):
    # Funções para verificar se uma relação é equivalência
    if reflexiva(relacao, A) == False or simetrica(relacao) == False or transitiva(relacao) == False:
        return False
    return True


def equivalencia2(R, S, T):
    # Funções para verificar se uma relação é equivalência
    if R == False or S == False or T == False:
        return False
    return True


def irreflexiva(relacao, A):
    # Verifica se uma relação é irreflexiva
    for a in A:
        if (a, a) in relacao:
            return False
    return True


def funcao(relacao, A):
    # Verifica se é uma função, cada domínio só pode ter uma imagem
    B = [a for (a, b) in relacao]
    if len(B) != len(A) or len(B) != len(set(B)):
        return False
    return True


def fInjetora(relacao, A):
    # Verifica se é uma função injetora, cada imagem só pode ter um domínio
    if funcao(relacao, A) == False or len(set(a for (a, b) in relacao for (c, d) in relacao if a != c and b == d)) != 0:
        return False
    return True


def fSobrejetora(relacao, A):
    # Verifica se é uma função sobrejetora, injetora e bijetora
    B = [b for (a, b) in relacao]
    if funcao(relacao, A) == False or len(B) != len(A) or len(B) != len(set(B)):
        return False
    return True


def fBijetora(relacao, A):
    # Verifica se é uma função bijetora, todas os elementos de A estão contidos na imagem
    if fInjetora(relacao, A) == False or fSobrejetora(relacao, A) == False:
        return False
    return True


def defRelacoes(A, arquivo):
    # Calcula as relações em A e salva em um arquivo
    n = len(A)
    with open(arquivo, 'w') as file:
        iniciar_contador()
        for i in range(2**(n**2)):
            Poti = {(A[j//n], A[j % n])
                    for j in range(n**2) if i & 1 << j != 0}
            str = ""
            S = simetrica(Poti)
            if S:
                str += "S"
            T = transitiva(Poti)
            if T:
                str += "T"
            R = reflexiva(Poti, A)
            if R:
                str += "R"
            if equivalencia2(R, S, T):
                str += "E"
            if irreflexiva(Poti, A):
                str += "I"
            if funcao(Poti, A):
                str += "Fu"
            if fInjetora(Poti, A):
                str += "Fi"
            if fBijetora(Poti, A):
                str += "Fb"
            if fSobrejetora(Poti, A):
                str += "Fs"

            if Poti == set():
                Poti = "{}"
            file.write(f"{Poti} {str}\n")
        time = terminar_contador()
    return time


def Tarefa01():
    n = 5
    A = []
    Times = []
    arquivo = "ConjuntoPotencia"
    for i in range(n):
        A.append(i)
        Times.append(defRelacoes(A, arquivo+f"{len(A)}.txt"))
    # Plotando o gráfico
    plt.plot([i for i in range(1, n+1)], Times,
             color='blue', linewidth=2, linestyle='-')

    # Personalizando o gráfico
    plt.title('Relações Binárias de um conjunto')
    plt.xlabel('Tamanho do Conjunto')
    plt.ylabel('Tempo(s)')
    plt.xticks(range(1, n + 1))

    plt.savefig('TimexN.svg', bbox_inches='tight')
    with open("Tempos.txt", 'w') as fileTime:
        fileTime.write(str(Times))


def repMatriz(A, R):
    # A partir de uma relação R de um conjunto A é montado e retornada a matriz de zero-um que representa os pares ordenados de R
    n = len(A)
    MatrizR = [[0 for i in range(n)] for j in range(n)]
    for (i, j) in R:
        MatrizR[i][j] = 1
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


def Tarefa02():
    A = [0, 1, 2]
    R = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 1)]
    print(f"A = {A}\nR = {R}")

    M = repMatriz(A, R)
    print(f"M = {M}")
    print(f"M = {imprimeParesOrdenados(A, M, False)}")

    FR = fechoReflexivo(M)
    FR = imprimeParesOrdenados(A, FR, False)
    print(f"({reflexiva(set(FR), A)})FR = {FR}")

    FS = fechoSimetrico(M)
    FS = imprimeParesOrdenados(A, FS, False)
    print(f"({simetrica(set(FS))})FS = {FS}")

    FT = fechoTransitivoRosen(M)
    FT = imprimeParesOrdenados(A, FT, False)
    print(f"({transitiva(set(FT))})FT = {FT}")

    FTW = fechoTransitivoWarshall(M)
    FTW = imprimeParesOrdenados(A, FTW, False)
    print(f"({transitiva(set(FTW))})FTW = {FTW}")

    FE = menorREquivalencia(M)
    FE = imprimeParesOrdenados(A, FE, False)
    print(f"({equivalencia(set(FE), A)})FE = {FE}")


if __name__ == "__main__":
    Tarefa02()
