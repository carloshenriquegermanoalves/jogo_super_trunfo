from bibliotecas.bib_cartas import *
from bibliotecas.bib_funcionalidades import *
from bibliotecas.bib_menus import *
from time import sleep
from colorama import Fore

def jogada(vez_do_jogador):
    menu_combate(jogador1[-1], jogador2[-1])
    if (vez_do_jogador == 1): #A vez do jogador é feito vendo se o número é ímpar ou não
        print("Qual opção o jogador 1 escolhe? ")
    else:
        print("Qual opção o jogador 2 escolhe? ")
    atributo_escolhido = ler_1_2_3(">>> ")
    limpa_tela()
    menu_cartas_combate(jogador1[0], jogador2[0])

    sleep(1)

    # Se o jogador 1 ganhar entra nesse if
    if jogador1[0][0][atributo_escolhido] > jogador2[0][0][atributo_escolhido]:
        print(f"{jogador1[0][0][0]} ganha de {jogador2[0][0][0]}. {Fore.GREEN}Jogador 1 venceu.{Fore.RESET}")
        sleep(1)
        print("Pressione Enter para a próxima rodada...")
        input()

        jogador1[-1] = calcula_pontos_jogador(jogador1[-1], jogador1[0][0][atributo_escolhido], jogador2[0][0][atributo_escolhido]) # Soma o atributo vencedor ao vencedor da rodada
        jogador2[-1] = calcula_pontos_jogador(jogador2[-1], jogador1[0][0][atributo_escolhido], jogador2[0][0][atributo_escolhido], resultado=False) # Subtrai a diferença entre os atributos vencedor e perdedor dos pontos do jogador que perdeu por causa do atributo resultado receber o valor False

        carta_usada(jogador1[0])
        adicionar_carta_de_outro_baralho(jogador2[0], jogador1[0])


    # Se o jogador 2 ganhar entra nesse elif
    elif jogador2[0][0][atributo_escolhido] > jogador1[0][0][atributo_escolhido]:
        print(f"{jogador2[0][0][0]} ganha de {jogador1[0][0][0]}. {Fore.GREEN}Jogador 2 venceu.{Fore.RESET}")
        sleep(1)
        print("Pressione Enter para a próxima rodada...")
        input()

        jogador2[-1] = calcula_pontos_jogador(jogador2[-1], jogador2[0][0][atributo_escolhido], jogador1[0][0][atributo_escolhido]) # Soma o atributo vencedor ao vencedor da rodada
        jogador1[-1] = calcula_pontos_jogador(jogador1[-1], jogador2[0][0][atributo_escolhido], jogador1[0][0][atributo_escolhido], resultado=False) # Subtrai a diferença entre os atributos vencedor e perdedor dos pontos do jogador que perdeu

        carta_usada(jogador2[0])
        adicionar_carta_de_outro_baralho(jogador1[0], jogador2[0])

    # Se der empate entra no else
    else:
        print(f"{jogador1[0][0][0]} empata com {jogador2[0][0][0]}")
        caso_empate(baralho_principal, jogador1[0])
        caso_empate(baralho_principal, jogador2[0])
        while jogador1[0][0][atributo_escolhido] == jogador2[0][0][atributo_escolhido]:
            jogada(vez_do_jogador = vez_do_jogador)
        sleep(1)


escolha = 0 #O 0 inicial é apenas uma variável de controle
while (escolha != 3): #3 é o número que o usuário tem que digitar para sair do jogo, portanto enquanto a escolha for diferente de 3, o jogo acontecerá.
    personagens = ["Naruto", "Sakura", "Sasuke", "Itachi", "Madara", "Obito", "Hidan", "Sasori", "Pain", "Konan", "Jiraya", "Yamato", "Gaara", "Kiba", "Hinata", "Choji", "Neji", "Temari", "Asuma", "Kakuzu"]

    baralho_principal = gera_baralho(personagens)

    jogador1 = cria_jogador(baralho_principal)
    jogador2 = cria_jogador(baralho_principal)

    menu_inicial()

    jogar_ou_ver_regras = 0
    while jogar_ou_ver_regras not in [1, 2, 3]:
        jogar_ou_ver_regras = ler_1_2_3(">>> ")

    limpa_tela()

    if jogar_ou_ver_regras == 1:
        primeira_rodada = 1
        rodada_limite = 5
        for i in range(primeira_rodada, rodada_limite):
            if (i % 2 == 1):
                menu_vez_jogador_1()
                sleep(1)
                limpa_tela()
                jogada(1)

                sleep(1.5)
                limpa_tela()

            if (i % 2 == 0):
                menu_vez_jogador_2()
                sleep(1)
                jogada(2)
                
                sleep(1.5)
                limpa_tela()

        if jogador1[-1] > jogador2[-1]:
            menu_jogador_1_venceu()
            input()
            limpa_tela()
        elif jogador2[-1] > jogador1[-1]:
            menu_jogador_2_venceu()
            input()
            limpa_tela()
        else:
            menu_empate()
            input()
            limpa_tela()


    elif jogar_ou_ver_regras == 2:
        menu_regras()
        input()
        limpa_tela()

    else:
        escolha = jogar_ou_ver_regras
        print("Esperamos que tenha se divertido com o nosso jogo. Volte sempre. . .")
        exit()
