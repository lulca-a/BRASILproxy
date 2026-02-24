import cv2
import numpy as np
from PIL import Image,ImageFilter
from io import BytesIO

# ===== COORDENADAS DO TEXTO =====
img = cv2.imread("karlov.png")
x1, y1 = 58,593
x2, y2 = 622,635
h, w = img.shape[:2]

bloco_texto = np.array([
    [int(0.08*w), int(0.63*h)],
    [int(0.92*w), int(0.63*h)],
    [int(0.08*w), int(0.88*h)],
    [int(0.92*w), int(0.88*h)]
])


bloco_tipo=[(58,593),(622,635)]

bloco_nome=[(60,60),(610,100)]


def recorte(bloco):
    # caminho da carta
    

    # cria máscara preta (mesmo tamanho da imagem)
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask = cv2.GaussianBlur(mask, (21,21), 0)

    # desenha retângulo branco na máscara (área a remover)
    cv2.fillPoly(mask, [bloco], 255)
    # aplica inpainting
    resultado = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    alpha = 0.6  # força do inpainting (0 = original, 1 = total)
    suave = cv2.addWeighted(resultado, alpha, img, 1-alpha, 0)


    # cv2.imshow("Original", img)
    # cv2.imshow("Mascara", mask)
    # cv2.imshow("Inpainting", resultado)
    cv2.imwrite("resultado.png", resultado)

recorte(bloco_texto)

# cv2.waitKey(0)
# cv2.destroyAllWindows()