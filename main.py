from scrypull import pull
from traduzir import traduzir
from formatador import Formatador
from limpar import limpar
from escrever import escrever

baralho= '1 lightning bolt'

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

    #visual
    imagem_original = carta['imagem']
    limpar(imagem_original)
    escrever(carta)

    print('------------------------------------')
    
'''
variaveis:
deck:titulos e quantidades (input)
nome_en (scry)
quantidade (input)
nome_pt (trad)
texto_pt (trad)
tipo_pt (trad)
'''