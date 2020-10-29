import cv2

imagen_i = cv2.imread("imagen.jpg")
imagen = cv2.cvtColor(imagen_i,cv2.COLOR_BGR2RGB)
imagen2 = cv2.cvtColor(imagen_i,cv2.COLOR_BGR2GRAY)


imagen = cv2.resize(imagen,(256,256))

cv2.imwrite("resizeimagen.jpg",imagen)
#cv2.imshow("image",imagen)
#cv2.waitKey(0)

cv2.imwrite("grayimagen.jpg",imagen2)
#cv2.imshow("image",imagen2)
#cv2.waitKey(0)