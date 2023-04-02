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


if __name__ == "__main__":
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
