import cv2
import numpy as np
import os

# Lista de caminhos para as imagens que você deseja testar
image_paths = [
    "s14.jpg",  # Substitua pelos caminhos corretos das suas imagens
    "gtr.jpg",
    "180.jpg",
    "SKYLINE.jpg"
]

# Função para processar e validar cada imagem
def process_image(img_path):
    # Leitura da imagem
    img = cv2.imread(img_path)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem {img_path}.")
        return

    # Processamento: Conversão para escala de cinza
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicação de um desfoque gaussiano
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Binarização
    _, binary_img = cv2.threshold(blurred_img, 127, 255, cv2.THRESH_BINARY)

    # Detecção de contornos
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Criar máscara para segmentação
    marker_img = np.zeros(gray_img.shape, dtype=np.int32)
    for i in range(len(contours)):
        cv2.drawContours(marker_img, contours, i, (i + 1), -1)

    # Definir a borda (com valor 0) para a máscara
    marker_img[marker_img == 0] = -1

    # Aplicação do algoritmo Watershed
    cv2.watershed(img, marker_img)
    img[marker_img == -1] = [255, 0, 0]  # Marcar bordas

    # Salvar as imagens processadas
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    cv2.imwrite(f"{base_name}_original.jpg", img)
    cv2.imwrite(f"{base_name}_gray.jpg", gray_img)
    cv2.imwrite(f"{base_name}_blurred.jpg", blurred_img)
    cv2.imwrite(f"{base_name}_binary.jpg", binary_img)
    cv2.imwrite(f"{base_name}_segmented.jpg", img)

    print(f"Imagens processadas para {img_path} salvas com sucesso.")

# Testar cada imagem na lista
for image_path in image_paths:
    process_image(image_path)
