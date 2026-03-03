import cv2
import numpy as np
import requests
from src.database.coordenadas import escolha_layout
def limpar(carta):
    url = carta['imagem']
    r = requests.get(url)
    img_array = np.frombuffer(r.content, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (745, 1040))

    texto = np.array(escolha_layout(carta), dtype=np.int32)

    tipo = np.array([(58,595),(610,595),
                       (610,635),(58,635)], dtype=np.int32)
    
    custo = [i for i in carta['custo'] if i == '{']#isso adapta o tamanho do recorte dependendo dos espaços de símbolos de custo
    espaço_custo = 48*len(custo)
    
    nome = np.array([(60,59),(690-espaço_custo,59),
                       (690-espaço_custo,98),(60,98)], dtype=np.int32)

    
    mask = np.zeros(img.shape[:2], dtype=np.uint8)


    cv2.fillPoly(mask, [texto], 255)
    cv2.fillPoly(mask, [tipo], 255)
    cv2.fillPoly(mask, [nome], 255)

    carta_limpa = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

  
    debug = img.copy()
    cv2.polylines(debug, [texto], True, (0,0,255), 2)
    cv2.polylines(debug, [tipo], True, (0,0,255), 2)
    cv2.polylines(debug, [nome], True, (0,0,255), 2)
    cv2.imwrite("src/testes/polly.png", debug)

    cv2.imwrite("src/testes/resultado.png", carta_limpa)


#criatura
#terreno sem texto
#encantamento, artefato, feietiço, instantanea
#planeswalker
#saga


'''


}'''