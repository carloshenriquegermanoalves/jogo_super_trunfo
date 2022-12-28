from random import randint

def gera_valores(): 
    """
    Retorna os valores das características das cartas
    """
    ninjutsu = randint(1, 20) 
    genjutsu = randint(1, 20)
    taijutsu = randint(1, 20)
    atributos = [ninjutsu, genjutsu, taijutsu] #Os valores dos atributos das cartas são adicionados nesta lista
    return atributos


def gera_baralho(personagens): 
    """
    Retorna o baralho
    parâmetro:
        a lista dos personagens:
            Para que suas cartas sejam formadas
    """
    baralho = []
    for cartas in range(len(personagens)):
        atributos_carta = gera_valores() #Usamos a função anterior para gerar os atributos
        carta = [personagens[cartas],atributos_carta[0], atributos_carta[1], atributos_carta[2]] #Faz com que o personagem receba seus atributos, gerando uma carta
        baralho.append(carta) #Na lista do baralho é adicionado a carta que é uma sub-lista
    return baralho

