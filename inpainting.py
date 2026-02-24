import cv2
import numpy as np
from PIL import Image,ImageFilter
from io import BytesIO

# ===== COORDENADAS DO TEXTO =====
img = cv2.imread("karlov.png")
x1, y1 = 58,593
x2, y2 = 622,635

bloco_texto = np.array([
    [60,656],    # 1 topo esquerdo
    [680,656],   # 2 topo direito
    [680,915],
    [570,915],   
    [570,935],   # 4 canto inferior direito inclinado
    [60,935],    # 5 canto inferior esquerdo
         # 6 subindo lado esquerdo
], dtype=np.int32)

bloco_tipo=[(58,593),(622,635)]

bloco_nome=[(60,60),(610,100)]

def recorte(bloco):

    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    # desenha polígono
    cv2.fillPoly(mask, [bloco], 255)

    # suaviza borda
    # mask = cv2.GaussianBlur(mask, (21,21), 0)

    # inpainting
    resultado = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    debug = img.copy()
    cv2.polylines(debug, [bloco_texto], True, (0,0,255), 3)
    # mistura pra ficar natural
    alpha = 0.6
    # suave = cv2.addWeighted(resultado, alpha, img, 1-alpha, 0)

    cv2.imwrite("resultado.png", resultado)
    cv2.imwrite("polly.png", debug)
recorte(bloco_texto)

# cv2.waitKey(0)
# cv2.destroyAllWindows()