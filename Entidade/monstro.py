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
monstro = {'id': '1', 'facil'{
    'nome': 'Kree', 'poder': 20, 'esquiva': 10, 'defesa' : 15, 'vida_maxima' : 100, 'vida_atual' : 100
    },
{'id': '2','medio'{'nome': 'soberanos', 'poder': 25, 'esquiva': 5, 'defesa': 20, 'vida_maxima': 150, 'vida_atual': 150
},}
{'id': '3','dificil'{'nome': 'sociedade perfeita', 'poder': 35, 'esquiva': 15, 'defesa': 25, 'vida_maxima': 250, 'vida_atual': 250
}}
    }