class Vocacao:
    def __init__(self, nome, bonus_poder, bonus_desefa):
        self.nome = nome
        self.bonus_poder = bonus_poder
        self.bonus_defesa = bonus_defesa
    
    def aplicar_bonus(self, entidade):
        entidade.poder += self.bonus_poder
        entidade.defesa += self.bonus_defesa
        