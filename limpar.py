import cv2
import numpy as np
import requests

def limpar(url):


    r = requests.get(url)
    img_array = np.frombuffer(r.content, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    texto = np.array([
    [60,656],[680,656], 
    [680,915],[570,915],   
    [570,935],[60,935]], dtype=np.int32)

    tipo = np.array([(58,593),(622,593),
                       (622,635),(58,635)], dtype=np.int32)

    nome = np.array([(60,60),(610,60),
                       (610,99),(60,105)], dtype=np.int32)

    
    mask = np.zeros(img.shape[:2], dtype=np.uint8)


    cv2.fillPoly(mask, [texto], 255)
    cv2.fillPoly(mask, [tipo], 255)
    cv2.fillPoly(mask, [nome], 255)

    carta_limpa = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    if __name__ == '__main__':
        debug = img.copy()
        cv2.polylines(debug, [texto], True, (0,0,255), 2)
        cv2.polylines(debug, [tipo], True, (0,0,255), 2)
        cv2.polylines(debug, [nome], True, (0,0,255), 2)

        cv2.imwrite("polly.png", debug)

    cv2.imwrite('resultado.png', carta_limpa)

# limpar('karlov.png')