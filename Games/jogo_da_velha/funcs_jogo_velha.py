tabuleiro = []


def criar_tabuleiro():
    for i in range(0, 3):
        linha = []
        for j in range(0, 3):
            linha.append(0)
        tabuleiro.append(linha)
    return tabuleiro


def mostrar_jogo(tabuleiro):
    for linha in tabuleiro:
        print(linha)


def tutorial():
    print("Para jogar, insira o local a ser marcado por Coluna e Linha(C, L). Ex.: '0, 0'.\nOBS: ambas as colunas e linhas são contadas apartir de 1.")


def separar_indices(jogada):
    indices = jogada.split(',')
    i = 0
    for valor in indices:
        indices[i] = int(valor) - 1
        i += 1
    return indices


def marcacao(simbolo):
    if simbolo == 1:
        return "X"
    else:
        return "O"


def marcar_tabuleiro(tabuleiro, jogada, simbolo):
    indices = separar_indices(jogada)
    tabuleiro[indices[0]][indices[1]] = marcacao(simbolo)


def vitoria(contador, marca):
    if contador == 3:
        mostrar_jogo(tabuleiro)
        print(f"O {marca} ganhou!")
        return True


def checar_jogo(tabuleiro, simbolo, contador=0):
    # checa linhas
    marca = marcacao(simbolo)
    for linha in tabuleiro:
        if linha.count(marca) == 3:
            mostrar_jogo(tabuleiro)
            print(f"O {marca} ganhou!")
            return False

    # checa colunas
    for l in range(0, 3):
        for c in range(0, 3):
            if tabuleiro[c][l] == marca:
                contador += 1
            else:
                contador = 0

            if vitoria(contador, marca):
                return False

    contador = 0

    # checa diagonais
    for i in range(0, 3):
        if tabuleiro[i][i] == marca:
            contador += 1
        else:
            contador = 0
    if vitoria(contador, marca):
        return False

    contador = 0
    c = 2

    for i in range(3):
        if tabuleiro[i][c] == marca:
            contador += 1
        else:
            contador = 0
        c -= 1
    if vitoria(contador, marca):
        return False

    return True