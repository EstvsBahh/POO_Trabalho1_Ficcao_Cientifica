from Entidade.entidade import Entidade
from Vocacao.vocacao import Vocacao
from Raca.raca import Raca

kree = Raca("Kree", 15, 3)

class Base_monstro:
    def __init__(self,vida,defesa,ataque,esquiva):
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva
        pass
    
jogador = Base_monstro(
    nome = "Kree",
    poder = 10,
    vida_maxima = 200,
    vida_atual = 200,
    esquiva = 5,
    raca = kree,
    vocacao = atirador
)