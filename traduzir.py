from googletrans import Translator


#oracle_text = resultado['oracle_text']
def traduzir(carta :dict):
    t = Translator()
    print(t.translate(carta['nome'],src='en',dest='pt').text)
    print(t.translate(carta['type_line'],src='en',dest='pt').text)
    print(t.translate(carta['oracle_text'],src='en',dest='pt').text)
