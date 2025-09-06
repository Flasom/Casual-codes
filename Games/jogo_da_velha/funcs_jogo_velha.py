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
    print("Para jogar, insira o local a ser marcado por Coluna e Linha(C, L). Ex.: '0, 0'.")
    print("OBS: ambas as colunas e linhas são contadas apartir de 1.")


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
    if tabuleiro[indices[0]][indices[1]] in ["X", "O"]:
        print("Esse local já está marcado, jogue em um local ainda vazio!")
        return True
    else:
        tabuleiro[indices[0]][indices[1]] = marcacao(simbolo)


def vitoria(contador, marca):
    if contador == 3:
        mostrar_jogo(tabuleiro)
        print(f"O {marca} ganhou!")
        return True


def checar_linhas(simbolo, marca, tabuleiro):
    for linha in tabuleiro:
        if linha.count(marca) == 3:
            mostrar_jogo(tabuleiro)
            print(f"O {marca} ganhou!")
            return True


def checar_colunas(tabuleiro, marca, contador):
    for l in range(0, 3):
        for c in range(0, 3):
            if tabuleiro[c][l] == marca:
                contador += 1
            else:
                contador = 0

            if vitoria(contador, marca):
                return True


def checar_diagonais(tabuleiro, marca, contador):
    c = [0, 1, 2]
    for r in range(0, 2):
        for i in range(0, 3):
            if tabuleiro[i][c[i]] == marca:
                contador += 1
        if vitoria(contador, marca):
            return True
        contador = 0
        c.reverse()


def checar_jogo(tabuleiro, simbolo, contador=0):
    marca = marcacao(simbolo)

    if checar_linhas(simbolo, marca, tabuleiro):
        return False

    if checar_colunas(tabuleiro, marca, contador):
        return False

    contador = 0

    if checar_diagonais(tabuleiro, marca, contador):
        return False

    return True
