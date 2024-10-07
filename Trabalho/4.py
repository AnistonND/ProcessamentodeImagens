import cv2

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

    # Aplicação do filtro GaussianBlur (suavização)
    gaussian_blur = cv2.GaussianBlur(gray_img, (7, 7), 1.5)

    # Aplicação do filtro Canny (detecção de bordas)
    canny_edges = cv2.Canny(gaussian_blur, 100, 200)

    # Aplicação do filtro Sobel (detecção de gradientes)
    sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)  # Gradiente na direção x
    sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=5)  # Gradiente na direção y

    # Exibição dos resultados
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem em Escala de Cinza", gray_img)
    cv2.imshow("Gaussian Blur", gaussian_blur)
    cv2.imshow("Canny Edges", canny_edges)
    cv2.imshow("Sobel X", sobelx)
    cv2.imshow("Sobel Y", sobely)

    # Espera por uma tecla para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Opcionalmente, salvar as imagens processadas
    cv2.imwrite("gaussian_blur_s14.jpg", gaussian_blur)
    cv2.imwrite("canny_edges_s14.jpg", canny_edges)
    cv2.imwrite("sobelx_s14.jpg", sobelx)
    cv2.imwrite("sobely_s14.jpg", sobely)

    print("Imagens filtradas salvas com sucesso.")
