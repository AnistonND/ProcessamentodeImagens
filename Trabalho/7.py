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

    # Aplicar um threshold para binarizar a imagem
    _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

    # Definir um kernel para as operações morfológicas
    kernel = np.ones((5, 5), np.uint8)

    # Erosão
    eroded_img = cv2.erode(binary_img, kernel, iterations=1)

    # Dilatação
    dilated_img = cv2.dilate(binary_img, kernel, iterations=1)

    # Exibir os resultados
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem Binarizada", binary_img)
    cv2.imshow("Imagem Erodida", eroded_img)
    cv2.imshow("Imagem Dilatada", dilated_img)

    # Espera por uma tecla para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Opcionalmente, salvar as imagens processadas
    cv2.imwrite("binary_s14.jpg", binary_img)
    cv2.imwrite("eroded_s14.jpg", eroded_img)
    cv2.imwrite("dilated_s14.jpg", dilated_img)

    print("Imagens binarizada, erodida e dilatada salvas com sucesso.")
