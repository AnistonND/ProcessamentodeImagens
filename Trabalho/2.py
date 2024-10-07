import cv2

img_path = "s14.jpg"

img = cv2.imread(img_path)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do arquivo.")
else:

    cv2.imshow("Imagem Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
