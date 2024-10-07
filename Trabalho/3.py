import cv2
img_path = "s14.jpg"

img = cv2.imread(img_path)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
else:
   
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray_img, (300, 300))

    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem em Escala de Cinza", gray_img)
    cv2.imshow("Imagem Redimensionada", resized_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("gray_resized_s14.jpg", resized_img)
    print("Imagem em escala de cinza e redimensionada salva com sucesso.")
