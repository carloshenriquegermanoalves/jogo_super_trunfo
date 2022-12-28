import os
import sys
from random import choice

def ler_1_2_3(valor):
    """
    Objetivo:
        - Observando que as opções dos jogadores resumem-se a apertar 1, 2 ou 3 e verificando que esse padrão se repete em todas as opções, decidiu-se criar uma função que só permita ao usuário digitar esse valores
    Parâmetros:
        valor:
            Uma string que a função tentará transformar em um inteiro
            Se o valor digitado puder ser convertido para um inteiro:
                Se o valor convertido for 1, 2 ou 3:
                    - A função retorna a opção escolhida
            Caso contrário:
                Um loop se inicia para que o usuário digite somente uma das opções (1, 2 ou 3)
    """
    if (valor.isnumeric()):
        valor_inteiro = int(input(valor).strip(" "))
        if (valor_inteiro in [1, 2, 3]):
            return valor_inteiro
    else:
        erro = True
        while (erro == True):
            valor_inteiro = str(input("Digite uma opção válida: "))
            if (valor_inteiro.isnumeric()):
                valor_inteiro = int(valor_inteiro)
                if (valor_inteiro in [1, 2, 3]):
                    erro = False #Muda a condição para queo loop termine
                    return valor_inteiro


def limpa_tela():
    """
    Função sem parâmetro:
        Serve para limpar o terminal quando o jogo acabar
    """
    if sys.platform == 'linux': #Essa linha é necessária pois o comando para se limpar uma tela varia de acordo com o sistema operacional do usuário
        clear = lambda: os.system('clear')
    else:
        clear = lambda: os.system('cls')
    clear()

def distribui_cartas(baralho, quantidade_cartas):
    """
    Parâmetros:
        baralho:
            Pilha que se deseja retirar a ou as cartas.
        quantidade_cartas:
            Quantidade de cartas que se deseja retornar do baralho passado como parâmetro.
    """
    cartas_selecionadas = []
    for i in range(quantidade_cartas):
        carta = choice(baralho)#Escolhe uma carta
        cartas_selecionadas.append(carta)
        del baralho[baralho.index(carta)]#Deleta a carta escolhida
    
    return cartas_selecionadas    

def empilha_cartas(baralho):
    #Inverte a ordem das cartas
    for indice in range(len(baralho)):
        #Reposiciona a carta
        baralho.insert(indice,baralho[-1])
        #Retira o carta reposicionada de onde estava anteriormente
        del baralho[-1]

def caso_empate(baralho, baralho_jogador):
    #Para descartar a carta usada
    del baralho_jogador[0]
    #Para pegar uma nova carta da pilha
    baralho_jogador.append(baralho[0])
    del baralho[0]

def carta_usada(baralho):
    #Para colar a carta usada no fim do baralho
    baralho.append(baralho[0])#Coloca na ultima posição
    del baralho[0]#Apaga oque ficou na primeira

def adicionar_carta_de_outro_baralho(baralho_retira_carta, baralho_recebe_carta):
    """
    Parâmetros:
        baralho_retira_carta:
            O baralho do jogador perdedor cuja carta deve ser retirada e entregue ao jogador vencedor
        baralho_recebe_carta:
            O baralho do jogador vencedor que receberá a carta do jogador perdedor
    """
    baralho_recebe_carta.append(baralho_retira_carta[0])
    del baralho_retira_carta[0]

def calcula_pontos_jogador(pontos_jogador, habilidade_vencedora, habilidade_perdedora, resultado=True): 
    """
    Calcula os pontos do jogador:
        Parâmetros:
            pontos_jogador:
                Os pontos atual do jogador que se quer calcular
            habilidade_vencedora:
                Pontos da característica vencedora da rodada
            habilidade_perdedora:
                Pontos da característica perdedora da rodada
            resultado:
                Se o resultado for True:
                    Calcula os pontos do vencedor:
                        Soma-se a habilidade vencedora aos pontos do vencedor
                Se o resultador não for True:
                    Calcula os pontos do perdedor:
                        Subtrai-se a diferença aos pontos do perdedor
        Retorno:
            Pontos_jogador informado
    """
    pontos = pontos_jogador
    if (resultado):
        pontos += habilidade_vencedora
        return pontos
    else:
        diferenca_habilidade = habilidade_vencedora - habilidade_perdedora #Calcula a diferença entre as habilidades
        pontos -= diferenca_habilidade
        return pontos

def cria_jogador(baralho, quantidade_pontos=1000):
    """
    Parâmetros:
        baralho: Pilha que se deseja retirar as cartas.
        quantidade_pontos: Número de pontos que o jogador vai ter que por padrão é 1000.
    Retorno:
        Retorna uma lista com as cartas e com a quantidade de pontos do jogador 
    """
    cartas_do_jogador = distribui_cartas(baralho, 4)
    return [cartas_do_jogador, quantidade_pontos]
