from scrypull import pull
from traduzir import traduzir
from tratar_entrada import 
user_deck = 'a\n'
'b'

carta= tratar(["1 Daybreak Ranger"])
carta_pull = pull(carta.titulo())#input tratado, carta encontrada

if carta_pull != None:
    print(carta_pull)
    print(' ')
    titulo_en = carta_pull['nome']
    print(titulo_en)
    print('')
    titulo_pt = traduzir(carta_pull)#carta traduzida
    print(titulo_pt)
else:
    print('carta nao encontrada')