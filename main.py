from src.services.scryfall import pull
from src.core.traduzir import traduzir
from src.core.formatador import Formatador
from src.core.limpar import limpar
from src.core.escrever import escrever

baralho= '20 Black Lotus\n10 Lightning Bolt\n15 Brainstorm\n8 Eternal Witness\n12 Glorybringer\n6 Counterspell\n9 Sol Ring\n14 Dark Ritual\n7 Path to Exile\n11 Llanowar Elves'
# baralho = "2 battlee cry goblin" 

#tratamento do input
deck = Formatador(baralho)
quantidades = deck.quantidades()
titulos = deck.titulos()

for carta in titulos:
    
    print('------------------------------------')
    #tratamento de carta a carta
    pos = titulos.index(carta)
    carta = (pull(carta))
    nome_en = carta['nome']
    quantidade = quantidades[pos]
    
    #tradução
    nome_pt = traduzir(nome_en)
    tipo_pt = traduzir(carta['tipo'])
    texto_pt = traduzir(carta['texto'])

    #print
    for chave, valor in carta.items():
        print(f"{chave}: {valor}")

    #visual}
    limpar(carta)
    escrever(carta)

    print('------------------------------------')
    
''

#  {1}{r}