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
    # --- Transformação Geométrica: Rotacionamento ---
    # Obter dimensões da imagem
    (h, w) = img.shape[:2]
    # Definir o ponto de rotação (centro da imagem)
    center = (w // 2, h // 2)
    # Criar a matriz de rotação (ângulo em graus, ex: 45º)
    angle = 45
    scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    # Aplicar a rotação
    rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

    # --- Transformação Geométrica: Translação ---
    # Definir a matriz de translação (shift de 50 pixels à direita e 30 pixels para baixo)
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
    # Aplicar a translação
    translated_img = cv2.warpAffine(img, translation_matrix, (w, h))

    # --- Operações Aritméticas: Soma e Subtração de Imagens ---
    # Criar uma segunda imagem para as operações aritméticas (imagem branca do mesmo tamanho)
    img2 = np.ones_like(img) * 50  # Uma imagem com brilho de 50 em todos os canais

    # Soma das imagens (brilho adicional)
    img_sum = cv2.add(img, img2)

    # Subtração das imagens (escurecer)
    img_sub = cv2.subtract(img, img2)

    # Exibir os resultados
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem Rotacionada", rotated_img)
    cv2.imshow("Imagem Transladada", translated_img)
    cv2.imshow("Soma de Imagens", img_sum)
    cv2.imshow("Subtração de Imagens", img_sub)

    # Espera por uma tecla para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Opcionalmente, salvar as imagens processadas
    cv2.imwrite("rotated_s14.jpg", rotated_img)
    cv2.imwrite("translated_s14.jpg", translated_img)
    cv2.imwrite("sum_s14.jpg", img_sum)
    cv2.imwrite("sub_s14.jpg", img_sub)

    print("Imagens rotacionada, transladada, somadas e subtraídas salvas com sucesso.")
