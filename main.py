from scrypull import pull
from traduzir import traduzir
from formatador import Formatador
user_deck = 'a\n'
'b'

carta= Formatador(["1 Daybreak Ranger"])
carta_pull = pull(carta())#sem funcionamento até o formatador estar completo

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
    
    '''
    A FAzer:
    ambiente virtual (env)
    '''