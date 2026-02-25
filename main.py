from scrypull import pull
from traduzir import traduzir
from formatador import Formatador
from limpar import limpar

baralho= 'aakroma angel'  
deck = Formatador(baralho)

quantidades = deck.quantidades()
titulos = deck.titulos()


for carta in titulos:
    
    print('------------------------------------')
    pos = titulos.index(carta)
    carta = (pull(carta))

    imagem_original = carta['imagem']
    nome_en = carta['nome']
    quantidade = quantidades[pos]

    nome_pt = traduzir(nome_en)
    tipo_pt = traduzir(carta['tipo'])
    texto_pt = traduzir(carta['texto'])
    
    limpar(imagem_original)
    print(f'Nome EN/PT: {nome_en} / {nome_pt}\nQuantidade: {quantidade}\nTipo: {tipo_pt}\nTexto: {texto_pt}')
    
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