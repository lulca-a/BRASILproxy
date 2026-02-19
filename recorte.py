from PIL import Image,ImageFilter
from scrypull import pull
from io import BytesIO
import requests

card = pull('karlov ghost')
url = card['imagem']

r = requests.get(url)
img = Image.open(BytesIO(r.content)).convert("RGBA")

raio  = 0.0005

bloco_texto =[(60, 656, 679,918),(58,870,560,940)]
textura_texto = (668,656, 684,668)

bloco_tipo=(58,593,622,635)
textura_tipo=(165,591,186,597)

bloco_nome=(60,60,610,100)
textura_nome=(257,57,332,61)


def recorte(bloco,textura):
        
        textura = img.crop(textura).filter(ImageFilter.GaussianBlur(raio))
        largura = bloco[2] - bloco[0]
        altura = bloco[3] - bloco[1]

        camada = Image.new("RGBA", (largura, altura))
        
        # repetir textura
        for x in range(0, largura, textura.width):
            for y in range(0, altura, textura.height):
                camada.paste(textura, (x, y))

        # colar na carta
        img.paste(camada, (bloco[0], bloco[1]))

recorte(bloco_texto[0],textura_texto)
recorte(bloco_texto[1],textura_texto)
recorte(bloco_nome,textura_nome)
recorte(bloco_tipo,textura_tipo)

img.save("karlov_limpo.png")
print("Imagem limpa salva.")