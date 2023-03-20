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
            return ""
    return "S"


def transitiva(relacao):
    # Função para verificar se uma relação é transitiva
    for (a, b) in relacao:
        for (c, d) in relacao:
            if b == c and (a, d) not in relacao:
                return ""
    return "T"


def reflexiva(relacao, A):
    # Verifica se uma relação é reflexiva
    for a in A:
        if (a, a) not in relacao:
            return ""
    return "R"


def equivalencia(relacao):
    # Funções para verificar se uma relação é equivalência
    if reflexiva(relacao) == "" or simetrica(relacao) == "" or transitiva(relacao) == "":
        return ""
    return "E"


def equivalencia2(R, S, T):
    # Funções para verificar se uma relação é equivalência
    if R == "" or S == "" or T == "":
        return ""
    return "E"


def irreflexiva(relacao, A):
    # Verifica se uma relação é irreflexiva
    for a in A:
        if (a, a) in relacao:
            return ""
    return "I"


def funcao(relacao):
    # Verifica se é uma função, cada domínio só pode ter uma imagem
    if len(set(a for (a, b) in relacao for (c, d) in relacao if a == c and b != d)) != 0:
        return ""
    return "Fu"


def fInjetora(relacao, Fu):
    # Verifica se é uma função injetora, cada imagem só pode ter um domínio
    if Fu == "" or len(set((a, c, b) for (a, b) in relacao for (c, d) in relacao if a != c and b == d)) != 0:
        return ""
    return "Fi"


def fBijetora(relacao, A, Fu):
    # Verifica se é uma função bijetora, todas os elementos de A estão contidos na imagem
    if Fu == "" or len(set(b for (a, b) in relacao)) != len(A):
        return ""
    return "Fb"


def fSobrejetora(relacao, A, Fu):
    # Verifica se é uma função sobrejetora, injetora e bijetora
    if fInjetora(relacao, Fu) == "" or fBijetora(relacao, A, Fu) == "":
        return ""
    return "Fs"


def defRelacoes(A, arquivo):
    # Calcula as relações em A e salva em um arquivo
    n = len(A)
    with open(arquivo, 'w') as file:
        iniciar_contador()
        for i in range(2**(n**2)):
            Poti = {(j//n, j % n) for j in range(n**2) if i & 1 << j != 0}
            S = simetrica(Poti)
            T = transitiva(Poti)
            R = reflexiva(Poti, A)
            E = equivalencia2(R, S, T)
            I = irreflexiva(Poti, A)
            Fu = funcao(Poti)
            Fi = fInjetora(Poti, Fu)
            Fb = fBijetora(Poti, A, Fu)
            Fs = fSobrejetora(Poti, A, Fu)

            if Poti == set():
                Poti = "{}"
            file.write(f"{Poti} {S}{T}{R}{E}{I}{Fu}{Fi}{Fb}{Fs}\n")
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
