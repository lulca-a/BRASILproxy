from PIL import Image,ImageDraw,ImageFont
from scrypull import pull
from traduzir import traduzir

def quebrar_texto(draw, texto, fonte, largura_max):
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = linha_atual + (" " if linha_atual else "") + palavra
        largura = draw.textlength(teste, font=fonte)

        if largura <= largura_max:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas

def escrever(carta):
    
    nome = traduzir(carta['nome'])
    tipo = traduzir(carta['tipo'])
    texto = traduzir(carta['texto'])

    img = Image.open("resultado.png").convert("RGBA")
    draw = ImageDraw.Draw(img)
    fonte = ImageFont.truetype("fonts/Beleren2016-Bold.ttf", 40)
    fonte_tipo = ImageFont.truetype("fonts/Matrix-Bold.ttf", 37)
    fonte_texto = ImageFont.truetype("fonts/Mplantin.ttf", 28)

    draw.text((58,60), nome, fill=(20,20,20), font=fonte)
    draw.text((65,600), tipo, fill=(20,20,20), font=fonte)

    linhas = quebrar_texto(draw, texto, fonte_texto, largura_max=520)

    y = 660
    for linha in linhas:
        draw.text((66, y), linha, fill=(20,20,20), font=fonte_texto)
        y += 40


    img.save(f'{carta['nome']}.png')