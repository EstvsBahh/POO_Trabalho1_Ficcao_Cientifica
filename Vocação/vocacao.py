class Vocacao:
    def __init__(self, nome, bonus_poder, bonus_desefa):
        self.nome = nome
        self.bonus_poder = bonus_poder
        self.bonus_defesa = bonus_defesa
    
    def aplicar_bonus(self, entidade):
        entidade.poder += self.bonus_poder
        entidade.defesa += self.bonus_defesa

    def __str__(self):
        return self.nome
    
atirador = Vocacao("Atirador", 15, 2)
tanque = Vocacao("Tanque", 5, 20)
assassino = Vocacao("Assassino, 20, 1")