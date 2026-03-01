from Entidade.entidade import Entidade
from Vocacao.vocacao import Vocacao
from Raca,raca import Raca

humano = Raca("Humano", 10, 5)

class Base_jogador:
    def __init__(self, vida, defesa, ataque, esquiva):
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva
        self.raca.aplicar_bonus(self)
        pass
    
jogador = Base_jogador(
    nome = "Star Lord",
    poder = 10,
    vida_maxima = 200,
    vida_atual = 200,
    esquiva = 5,
    raca = humano,
    vocacao = atirador
)