baralho= '20 mountain\n10 swamp\n2 Shock\n1 Aangs JOurney'  

class Formatador:
    
    def __init__(self,deck):
        deck_formatado = []
        self.card_quant = []
        self.card_title = []
        
        for card in deck.splitlines():
            deck_formatado.append(tuple(card.split()))
        self.deck_formatado = deck_formatado
        
        print(self.deck_formatado)

        for i in self.deck_formatado:
            self.card_quant.append(i[0])
        print(self.card_quant)
        
        for i in self.deck_formatado:
            self.card_title.append(' '.join(i[1:]))
        print(self.card_title)
        
    def quantidades(self):
        return self.card_quant
    def titulos(self):
        return self.card_title 
       
ex = Formatador(baralho)
'''

A fazer:
Fazer com que capitalize cada palavra no nome
Dar join com ' ' nas palavras do nome

após isso, remover os prints, variavle baralho e a instacia no final do codigo
'''