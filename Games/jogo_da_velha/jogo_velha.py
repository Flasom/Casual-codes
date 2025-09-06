from funcs_jogo_velha import *

simbolo = 1
jogando = True
tabuleiro = criar_tabuleiro()

print("Escreva 'help' para tutorial, 'quit' para sair ou dê sua jogada.")


while jogando:
    mostrar_jogo(tabuleiro)
    jogada = input("Dê sua jogada: ")
    if jogada == "help":
        tutorial()
    elif jogada == "quit":
        break
    else:
        if marcar_tabuleiro(tabuleiro, jogada, simbolo):
            simbolo *= -1
        jogando = checar_jogo(tabuleiro, simbolo)
        simbolo *= -1
