from scrypull import pull
from trad import traduzir
from tratar_entrada import tratar

carta= tratar(["20 Sol Ring"])
carta_pull = pull(carta.titulo())#input tratado, carta encontrada
print(carta_pull)
print(' ')
titulo_en = carta_pull['nome']
print(titulo_en)
print('')
titulo_pt = traduzir(carta_pull)
print(titulo_pt)