import requests
import os
from wand.image import Image
from wand.color import Color

def baixar_simbolos():
    url = "https://api.scryfall.com/symbology"
    response = requests.get(url)
    data = response.json()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SIMBOLOS_DIR = os.path.join(BASE_DIR, "simbolos")

    os.makedirs(SIMBOLOS_DIR, exist_ok=True)

    for simbolo in data["data"]:
        codigo = simbolo["symbol"].replace("{","").replace("}","").replace("/","_")

        if "svg_uri" not in simbolo:
            continue

        svg_url = simbolo["svg_uri"]

        img_data = requests.get(svg_url).content

        with open(os.path.join(SIMBOLOS_DIR, f"{codigo}.svg"), "wb") as f:
            f.write(img_data)

    print("Símbolos baixados!")
def converter_svg_para_png():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SIMBOLOS_DIR = os.path.join(BASE_DIR, "simbolos")

    for arquivo in os.listdir(SIMBOLOS_DIR):

        if arquivo.endswith(".svg"):

            caminho_svg = os.path.join(SIMBOLOS_DIR, arquivo)
            caminho_png = os.path.join(
                SIMBOLOS_DIR,
                arquivo.replace(".svg", ".png")
            )

            try:
                with Image(filename=caminho_svg, resolution=600) as img:

                    # Força canal alfa
                    img.alpha_channel = "activate"

                    # Garante que é RGBA
                    img.format = "png"
                    img.background_color = Color("none")

                    # Remove qualquer cor sólida aplicada
                    img.transparent_color(Color("white"), alpha=0.0, fuzz=0)

                    img.save(filename=caminho_png)

                print("Convertido:", arquivo)

            except Exception as e:
                print("Erro ao converter:", arquivo, e)

    print("Finalizado.")

def deletar_svgs():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SIMBOLOS_DIR = os.path.join(BASE_DIR, "simbolos")

    removidos = 0

    for arquivo in os.listdir(SIMBOLOS_DIR):
        if arquivo.lower().endswith(".svg"):
            caminho = os.path.join(SIMBOLOS_DIR, arquivo)
            os.remove(caminho)
            removidos += 1
            print("Removido:", arquivo)

    print(f"Total removido: {removidos}")
def deletar_pngs():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SIMBOLOS_DIR = os.path.join(BASE_DIR, "simbolos")

    removidos = 0

    for arquivo in os.listdir(SIMBOLOS_DIR):
        if arquivo.lower().endswith(".png"):
            caminho = os.path.join(SIMBOLOS_DIR, arquivo)
            os.remove(caminho)
            removidos += 1
            print("Removido:", arquivo)

    print(f"Total removido: {removidos}")

deletar_pngs()
baixar_simbolos()
converter_svg_para_png()
deletar_svgs()