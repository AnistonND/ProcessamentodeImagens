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

    # Aplicar um desfoque gaussiano para reduzir ruídos
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Aplicar o threshold para criar uma imagem binária
    _, binary_img = cv2.threshold(blurred_img, 127, 255, cv2.THRESH_BINARY_INV)

    # Encontrar os contornos na imagem binária
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar uma máscara para a segmentação
    marker_img = np.zeros(gray_img.shape, dtype=np.int32)  # Mudança para tipo int32

    # Preencher a máscara com os contornos encontrados
    for i in range(len(contours)):
        cv2.drawContours(marker_img, contours, i, (i + 1), -1)

    # Definir a borda (com valor 0) para a máscara
    marker_img[marker_img == 0] = -1  # Marcar fundo como -1

    # Aplicar a transformação watershed
    cv2.watershed(img, marker_img)
    img[marker_img == -1] = [255, 0, 0]  # Marcar bordas com vermelho

    # Exibir resultados
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem Binarizada", binary_img)

    # Converter a máscara de marcadores para tipo uint8 para exibição
    marker_img_display = np.zeros(gray_img.shape, dtype=np.uint8)
    marker_img_display[marker_img == -1] = 255  # Marcar bordas como branco

    cv2.imshow("Máscara de Segmentação", marker_img_display)

    # Espera por uma tecla para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Opcionalmente, salvar as imagens processadas
    cv2.imwrite("binary_watershed_s14.jpg", binary_img)
    cv2.imwrite("marker_watershed_s14.jpg", marker_img_display)  # Salvar máscara convertida
    cv2.imwrite("segmented_watershed_s14.jpg", img)

    print("Imagens binarizada, máscara de segmentação e segmentação salvas com sucesso.")
