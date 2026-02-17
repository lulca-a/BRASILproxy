
class Formatador:
    
    def __init__(self,deck :str):
        deck_formatado = []
        self.card_quant = []
        self.card_title = []
        
        for card in deck.splitlines():
            deck_formatado.append(tuple(card.split()))
        self.deck_formatado = deck_formatado

        for card in self.deck_formatado:
            self.card_quant.append(card[0])
        
        for card in self.deck_formatado:
            self.card_title.append(' '.join(card[1:]))
    
    def quantidades(self):
        return self.card_quant
    def titulos(self):
        return self.card_title 
       


'''
A fazer:
Dar join com ' ' nas palavras do nome
Tratamento de erro

após isso, remover os prints, variavle baralho e a instacia no final do codigo
'''