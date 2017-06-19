# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# cont = 0 
# gray_img = cv2.imread('hand.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('GoldenGate',gray_img)
# hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
# plt.hist(gray_img.ravel(),256,[0,256])
# histA = hist;
# print(histA)

# gray_img = cv2.imread('hand.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('GoldenGate',gray_img)
# hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
# plt.hist(gray_img.ravel(),256,[0,256])





import cv2
import numpy as np
from matplotlib import pyplot as plt
countA = 0
countB = 0
countC = 0
finalResult = ""





imgA = cv2.imread('S1.png',0)
#imgB = cv2.imread('S1.png',0)
imgC = cv2.imread('S2.png',0)





edgesA = cv2.Canny(imgA,100,200)
#edgesB = cv2.Canny(imgB,100,200)
edgesC = cv2.Canny(imgC,100,200)



totalBrancoA = 0
totalBrancoC = 0


for i in range (0 ,239):
	for j in range (0 ,319):
		if(edgesA[i][j] == 255):
			totalBrancoA = totalBrancoA + 1


for i in range (0 ,239):
	for j in range (0 ,319):
		if(edgesC[i][j] == 255):
			totalBrancoC = totalBrancoC + 1
			





cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read() #ret means is true or false
	
	ret = cap.set(3,320)
	ret = cap.set(4,240)
	
	#cv2.imwrite("S2.png",frame);


	width = cap.get(3)
	height = cap.get(4)

	#print(frame[0].size, width , height)
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	frameEdge = cv2.Canny(frame,100,200)
	# print(frameEdge.size)
	# print(edgesA.size)


	for i in range (0 ,239):
		for j in range (0 ,319):
			if(edgesA[i][j] == 255 and frameEdge[i][j] == 255):
				countA = countA + 1
			
	

	for i in range (0 ,239):
		for j in range (0 ,319):
			if(edgesC[i][j] == 255 and frameEdge[i][j] == 255):
				countC = countC + 1
			

	

	# plt.subplot(121),plt.imshow(edgesA,cmap = 'gray')
	# plt.title('Image A'), plt.xticks([]), plt.yticks([])
	# plt.subplot(121),plt.imshow(edgesB,cmap = 'gray')
	# plt.title('Image B'), plt.xticks([]), plt.yticks([])
	# plt.subplot(122),plt.imshow(frameEdge,cmap = 'gray')
	# plt.title('Image '), plt.xticks([]), plt.yticks([])
	# plt.show()



	print("A:" , countA )
	#print("B:" , countB )
	print("C:" , countC )

	# maior = countA
	# finalResult = "A"
	# # if(countB>maior):
	# # 	maior = countB 
	# # 	finalResult = "B"
	# if(countC > maior):
	# 	maior = countC 
	# 	finalResult = "C"

	percentoA = countA/totalBrancoA
	percentoC = countC/totalBrancoC

	if(percentoA > percentoC):
		finalResult = "OPEN HAND"
	
	else :
		finalResult = "NUMBER TWO"
	print("MAIOR:", finalResult)
	
	
	countA = 0
	countB = 0
	countC = 0
	# Display the resulting frame
	# cv2.imshow('frame',frameEdge)
	# cv2.imshow('OPEN HAND',edgesA)
	# cv2.imshow('NUMBER TWO',edgesC)
	# if cv2.waitKey(0) & 0xFF == ord('q'):
	# 	break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()







# imgA = cv2.imread('handA.jpg',0)
# imgB = cv2.imread('handB.jpg',0)

# edgesA = cv2.Canny(imgA,100,200)
# edgesB = cv2.Canny(imgB,100,200)

# plt.subplot(121),plt.imshow(edgesA,cmap = 'gray')
# plt.title('Image A'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edgesB,cmap = 'gray')
# plt.title('Image B'), plt.xticks([]), plt.yticks([])
#plt.show()






# for i in range (0 ,258):
# 	for j in range (0 ,193):
# 		if(edgesA[i][j] == 255 and edgesB[i][j] == 255):
# 			count = count + 1
			
		
	
# print(count)



# while True:
#     k = cv2.waitKey(0) & 0xFF     
#     if k == 27: break             # ESC key to exit 
# cv2.destroyAllWindows()













# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('hand.jpg',0)

# edges = cv2.Canny(img,100,200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()