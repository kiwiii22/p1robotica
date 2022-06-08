import cv2

image = cv2.imread('figuras.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4


for c in cnts:
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)   

	x,y,w,h = cv2.boundingRect(approx)

	if len(approx)==3:
		cv2.putText(image,'Triangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio == 1:
			cv2.putText(image,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
		else:
			cv2.putText(image,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(image,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==6:
		cv2.putText(image,'Hexagono', (x,y-5),1,1,(0,255,0),1)
	
	if len(approx)==10:
		cv2.putText(image,'Estrella', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>=13:
		cv2.putText(image,'Circulo', (x,y-5),1,1,(0,255,0),1)	

	cv2.drawContours(image, [approx], 0, (0,255,0),2)
	cv2.imshow('image',image)
	cv2.imshow('canny',canny)
	cv2.waitKey(0)