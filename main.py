from scrypull import pull
from traduzir import traduzir
from formatador import Formatador
from limpar import limpar
from escrever import escrever

# baralho= '20 Black Lotus\n10 Lightning Bolt\n15 Brainstorm\n8 Eternal Witness\n12 Glorybringer\n6 Counterspell\n9 Sol Ring\n14 Dark Ritual\n7 Path to Exile\n11 Llanowar Elves'
baralho = '1 gandalf the grey'

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
    
    #texto
    nome_pt = traduzir(nome_en)
    tipo_pt = traduzir(carta['tipo'])
    texto_pt = traduzir(carta['texto'])
    print(f'Nome EN/PT: {nome_en} / {nome_pt}\nQuantidade: {quantidade}\nTipo: {tipo_pt}\nTexto: {texto_pt}')

    #visual}
    limpar(carta)
    escrever(carta)

    print('------------------------------------')
    
''

#  {1}{r}