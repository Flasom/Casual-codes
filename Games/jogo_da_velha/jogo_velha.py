from funcs_jogo_velha import *

simbolo = 1
jogando = True
tabuleiro = criar_tabuleiro()

print("Escreva 'help' para tutorial, 'quit' para sair ou dê sua jogada.")


def jogo(jogando, simbolo):
    while jogando:
        mostrar_jogo(tabuleiro)
        jogada = input("Dê sua jogada: ")
        if jogada == "help":
            tutorial()
        elif jogada == "quit":
            break
        else:
            marcar_tabuleiro(tabuleiro, jogada, simbolo)
            jogando = checar_jogo(tabuleiro, simbolo)
            simbolo *= -1


jogo(jogando, simbolo)
