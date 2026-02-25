class Entidade:
    def __init__(self,nome:str, poder:int, defesa:int, vida_maxima:int, vida_atual:int, esquiva:int):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima =  vida_maxima
        self.vida_atual = vida_atual
        self.esquiva = esquiva
    
    def estar_vivo(self):
        return self.vida_atual > 0
    def receber_dano(self, dano):
        self.vida_atual -= 0
        if self.vida_atual < 0:
            self.vida_atual = 0
    def curar(self, valor):
        self.vida_atual += valor
        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_atual