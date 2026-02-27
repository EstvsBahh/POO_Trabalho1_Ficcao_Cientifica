from Entidade.entidade import Entidade
from Vocacao.vocacao import Vocacao
from Raca,raca import Raca

class Base_monstro:
    def __init__(self,vida,defesa,ataque,esquiva):
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva
        pass
    