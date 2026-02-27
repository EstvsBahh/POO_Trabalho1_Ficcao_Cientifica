class Raca:
    def __init__(self, nome, bonus_vida, bonus_esquiva):
        self.nome = nome
        self.bonus_vida = bonus_vida
        self.bonus_esquiva = bonus_esquiva

    def aplicar_bonus(self, entidade):
        entidade.vida_maxima += self.bonus_vida
        entidade.esquiva += self.bonus_esquiva