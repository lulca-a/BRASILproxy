from PIL import Image, ImageDraw, ImageFont
from src.core.traduzir import traduzir
import re
import os


# ==============================
# ÁREA DO TEXTO
# ==============================

x_min = 66
x_max = 666
y_min = 661
y_max = 915

largura_texto_max = x_max - x_min
altura_texto_max = y_max - y_min


# ==============================
# UTILIDADES
# ==============================

def separar_simbolos(texto):
    return [p for p in re.split(r'(\{.*?\})', texto) if p]


def quebrar_texto(draw, texto, fonte, largura_max):
    paragrafos = texto.split("\n")
    linhas_finais = []

    for paragrafo in paragrafos:

        if paragrafo.strip() == "":
            linhas_finais.append("")
            continue

        palavras = paragrafo.split()
        linha_atual = ""

        for palavra in palavras:
            teste = linha_atual + (" " if linha_atual else "") + palavra
            largura = draw.textlength(teste, font=fonte)

            if largura <= largura_max:
                linha_atual = teste
            else:
                linhas_finais.append(linha_atual)
                linha_atual = palavra

        if linha_atual:
            linhas_finais.append(linha_atual)

    return linhas_finais


def calcular_altura_total(fonte, linhas):
    altura_total = 0
    for linha in linhas:
        if linha == "":
            altura_total += 12
        else:
            bbox = fonte.getbbox(linha)
            altura_linha = bbox[3] - bbox[1]
            altura_total += altura_linha + 6
    return altura_total


# ==============================
# AJUSTE INTELIGENTE DE FONTE
# ==============================

def ajustar_fonte_texto(draw, texto, caminho_fonte, tamanho_base):

    tamanho_min = 16
    tamanho_max = tamanho_base + 4

    melhor_fonte = None
    melhor_linhas = None
    melhor_altura = None

    # Primeiro tenta crescer
    for tamanho in range(tamanho_base, tamanho_max + 1):

        fonte = ImageFont.truetype(caminho_fonte, tamanho)
        linhas = quebrar_texto(draw, texto, fonte, largura_texto_max)
        altura_total = calcular_altura_total(fonte, linhas)

        if altura_total > altura_texto_max:
            break

        melhor_fonte = fonte
        melhor_linhas = linhas
        melhor_altura = altura_total

        if altura_total > altura_texto_max * 0.65:
            break

    # Se não conseguiu nem no base, começa a diminuir
    if melhor_fonte is None:
        for tamanho in range(tamanho_base - 1, tamanho_min - 1, -1):

            fonte = ImageFont.truetype(caminho_fonte, tamanho)
            linhas = quebrar_texto(draw, texto, fonte, largura_texto_max)
            altura_total = calcular_altura_total(fonte, linhas)

            if altura_total <= altura_texto_max:
                return fonte, linhas, altura_total

    return melhor_fonte, melhor_linhas, melhor_altura


# ==============================
# DESENHAR TEXTO + SÍMBOLOS
# ==============================

def desenhar_texto_com_simbolos(draw, img, x, y, texto, fonte):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(BASE_DIR)

    SIMBOLOS_DIR = os.path.join(PROJECT_ROOT, "assets", "simbolos")

    partes = separar_simbolos(texto)
    x_atual = x

    altura_fonte = fonte.size
    simbolo_tamanho = int(altura_fonte * 0.9)

    for parte in partes:

        if parte.startswith("{") and parte.endswith("}"):

            codigo = parte[1:-1].replace("/", "_")
            caminho = os.path.join(SIMBOLOS_DIR, f"{codigo}.png")

            if os.path.exists(caminho):

                simbolo_img = Image.open(caminho).convert("RGBA")
                simbolo_img = simbolo_img.resize(
                    (simbolo_tamanho, simbolo_tamanho),
                    Image.LANCZOS
                )

                y_offset = y + (altura_fonte - simbolo_tamanho) // 2
                img.paste(simbolo_img, (int(x_atual), int(y_offset)), simbolo_img)

                x_atual += simbolo_tamanho + 2

            else:
                x_atual += simbolo_tamanho

        else:
            draw.text((x_atual, y), parte, fill=(20, 20, 20), font=fonte)
            largura = draw.textlength(parte, font=fonte)
            x_atual += largura


# ==============================
# FUNÇÃO PRINCIPAL
# ==============================

def escrever(carta):

    img = Image.open("src/testes/resultado.png").convert("RGBA")
    draw = ImageDraw.Draw(img)

    nome = traduzir(carta['nome'])
    tipo = traduzir(carta['tipo'])
    texto = traduzir(carta['texto'])

    # FONTES
    fonte_nome = ImageFont.truetype("src/assets/fonts/Beleren2016-Bold.ttf", 40)
    fonte_tipo = ImageFont.truetype("src/assets/fonts/Matrix-Bold.ttf", 38)

    # Ajuste automático do tipo
    largura_tipo_max = 544
    bbox_tipo = fonte_tipo.getbbox(tipo)
    largura_tipo = bbox_tipo[2] - bbox_tipo[0]

    if largura_tipo > largura_tipo_max:
        escala = largura_tipo_max / largura_tipo
        novo_tamanho = int(38 * escala)
        fonte_tipo = ImageFont.truetype("src/assets/fonts/Matrix-Bold.ttf", novo_tamanho)

    # Desenha nome e tipo
    if carta['frame'] == '2003':
        draw.text((68, 68), nome, fill=(20, 20, 20), font=fonte_nome)
    else:
        draw.text((58, 60), nome, fill=(20, 20, 20), font=fonte_nome)

    if carta['frame'] == '1993':
        draw.text((86, 584), tipo, fill=(20, 20, 20), font=fonte_tipo)
    else:
        draw.text((66, 600), tipo, fill=(20, 20, 20), font=fonte_tipo)

    # Ajuste inteligente do texto
    fonte_texto, linhas, altura_total = ajustar_fonte_texto(
        draw,
        texto,
        "src/assets/fonts/Mplantin.ttf",
        28
    )

    # Centralização vertical suave
    espaco_sobrando = altura_texto_max - altura_total

    if espaco_sobrando > altura_texto_max * 0.3:
        y = y_min + espaco_sobrando // 3
    else:
        y = y_min

    # Desenha linhas
    for linha in linhas:

        if linha == "":
            y += 12
            continue

        desenhar_texto_com_simbolos(draw, img, x_min, y, linha, fonte_texto)

        bbox = fonte_texto.getbbox(linha)
        altura_linha = bbox[3] - bbox[1]
        y += altura_linha + 6

    img.save(f"src/testes/{carta['nome']}.png")