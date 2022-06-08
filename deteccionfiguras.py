import cv2

image = cv2.VideoCapture(0)  

while(True):
    ret, frame = image.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convierte a escala de grises
    canny = cv2.Canny(gray, 10, 150) #Imagen binarizada 
    canny = cv2.dilate(canny, None, iterations=1) #Agrega dilatación a la imagen
    canny = cv2.erode(canny, None, iterations=1) #Agrega erosión a la imagen
    cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4 Encontrar los contornos 

    for c in cnts:
        epsilon = 0.009*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True) 
        x,y,w,h = cv2.boundingRect(approx) #Se utiliza para dibujar un rectangulo aproximado alrededor de la imagen binaria

        if len(approx)==3: #cantidad de puntos o vertices obtenidos
            cv2.putText(frame,'Triangulo', (x,y-5),1,1,(0,255,0),1)

        if len(approx)==4:
            aspect_ratio = float(w)/h #aspect ratio se obtiene de la relación de alto y ancho
            print('aspect_ratio= ', aspect_ratio)
            if 0.95 <= aspect_ratio <= 1.20:
                cv2.putText(frame,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
            else:
                cv2.putText(frame,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

        if len(approx)==5:
            cv2.putText(frame,'Pentagono', (x,y-5),1,1,(0,255,0),1)

        if len(approx)==6:
            cv2.putText(frame,'Hexagono', (x,y-5),1,1,(0,255,0),1)
        
        if len(approx)==10:
            cv2.putText(frame,'Estrella', (x,y-5),1,1,(0,255,0),1)

        if len(approx)>=13:
            cv2.putText(frame,'Circulo', (x,y-5),1,1,(0,255,0),1)

        cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
        cv2.imshow('frame',frame)
        
    if cv2.waitKey(1) == ord('x'):
        break

image.release()
cv2.destroyAllWindows()