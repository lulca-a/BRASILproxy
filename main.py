from src.services.scryfall import pull
from src.core.traduzir import traduzir
from src.core.formatador import Formatador
from src.core.limpar import limpar
from src.core.escrever import escrever

deck_1993 = '''4 Black Lotus
4 Lightning Bolt
4 Shivan Dragon'''

deck_2003 = '''4 Darksteel Colossus
4 Eternal Witness
4 Decree of Justice'''

deck_modern = '''4 Fable of the Mirror-Breaker
4 The One Ring
4 Sheoldred, the Apocalypse'''


baralho = '1 black lotus'

deck = Formatador(baralho)
quantidades = deck.quantidades()
titulos = deck.titulos()

for carta in titulos:
    carta = pull(carta)
    print(carta['nome'])
    print('------------------------------------')
    limpar(carta)
    escrever(carta)
  