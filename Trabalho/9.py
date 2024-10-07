import cv2
import numpy as np

# Caminho para a imagem
img_path = "s14.jpg"

# Leitura da imagem
img = cv2.imread(img_path)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
else:
    # Conversão para escala de cinza
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar um desfoque gaussiano
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Aplicar um threshold para criar uma imagem binária
    _, binary_img = cv2.threshold(blurred_img, 127, 255, cv2.THRESH_BINARY)

    # Exibir as imagens processadas
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem Binarizada", binary_img)

    # Salvar as imagens processadas
    cv2.imwrite("original_image.jpg", img)  # Salvar imagem original
    cv2.imwrite("gray_image.jpg", gray_img)  # Salvar imagem em escala de cinza
    cv2.imwrite("blurred_image.jpg", blurred_img)  # Salvar imagem borrada
    cv2.imwrite("binary_image.jpg", binary_img)  # Salvar imagem binarizada

    print("Imagens salvas com sucesso.")

    # Espera por uma tecla para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
