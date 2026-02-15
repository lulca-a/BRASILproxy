#tipo de entrada: 20 MOuntain
                #10 SOl ring                  
    #nome vai pro scry-google -card conjurer


    #qunatidade vai pra pasta e copia e cola colocando o (1) como o windows já faz
#variaveis principais
    #nome_en
    #nome_pt
    #quantidade
    #tipo (pt)
    #texto (pt)

#str -> list -> str

a = 'a\nb'
print(a.split())
class tratar:
    def __init__(self,deck : list[str]) -> None:
        self.deck = deck
    def quant(self):
        for carta in self.deck:
            return carta.split()[0]    
    def titulo(self):
        for carta in self.deck:
            return (' '.join(carta.split()[1:]))

