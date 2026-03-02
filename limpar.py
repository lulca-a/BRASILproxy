import cv2
import numpy as np
import requests

def limpar(carta):
    url = carta['imagem']
    r = requests.get(url)
    img_array = np.frombuffer(r.content, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (745, 1040))

    texto = np.array([
    [60,656],[680,656], 
    [680,915],[586,920],  
    [570,935],[60,935]], dtype=np.int32)

    tipo = np.array([(58,593),(610,593),
                       (610,635),(58,635)], dtype=np.int32)
    
    custo = [i for i in carta['custo'] if i == '{']#isso adapta o tamanho do recorte dependendo dos espaços de símbolos de custo
    espaço_custo = 48*len(custo)
    
    nome = np.array([(60,60),(690-espaço_custo,60),
                       (690-espaço_custo,100),(60,100)], dtype=np.int32)

    
    mask = np.zeros(img.shape[:2], dtype=np.uint8)


    cv2.fillPoly(mask, [texto], 255)
    cv2.fillPoly(mask, [tipo], 255)
    cv2.fillPoly(mask, [nome], 255)

    carta_limpa = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

  
    debug = img.copy()
    cv2.polylines(debug, [texto], True, (0,0,255), 2)
    cv2.polylines(debug, [tipo], True, (0,0,255), 2)
    cv2.polylines(debug, [nome], True, (0,0,255), 2)
    cv2.imwrite("polly.png", debug)

    cv2.imwrite("resultado.png", carta_limpa)


#criatura
#terreno sem texto
#encantamento, artefato, feietiço, instantanea
#planeswalker
#saga


'''
COORDENADAS = {
    "2015": {
        "normal": {
            "nome": (x1, y1, x2, y2),
            "arte": (x1, y1, x2, y2),
            "tipo": (x1, y1, x2, y2),
            "texto": (x1, y1, x2, y2),
            "mana": (x1, y1, x2, y2)
        }
    },
    "2003": {
        ...
    },
    "1993": {
        ...
    }
}'''