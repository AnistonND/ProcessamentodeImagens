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

    # Detecção de cantos com Harris Corner Detector
    gray_img_float = np.float32(gray_img)
    harris_corners = cv2.cornerHarris(gray_img_float, 2, 3, 0.04)

    # Dilatar os pontos de canto para melhor visualização
    harris_corners = cv2.dilate(harris_corners, None)

    # Criar uma cópia da imagem original para marcar os cantos
    img_with_corners = img.copy()

    # Marcar os cantos detectados (pontos onde o valor do Harris Corner Detector é maior que 0.01 * valor máximo)
    img_with_corners[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

    # Detecção de contornos
    # Aplicar Canny para detectar as bordas
    edges = cv2.Canny(gray_img, 100, 200)
    
    # Encontrar os contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhar os contornos na imagem original
    img_with_contours = img.copy()
    cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)

    # Exibir resultados
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Cantos Detectados", img_with_corners)
    cv2.imshow("Contornos Detectados", img_with_contours)

    # Espera por uma tecla para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Opcionalmente, salvar as imagens processadas
    cv2.imwrite("harris_corners_s14.jpg", img_with_corners)
    cv2.imwrite("contours_s14.jpg", img_with_contours)

    print("Imagens com cantos e contornos salvas com sucesso.")
