import cv2

#Storing sample images of person
image1 = cv2.imread('Samples/1.jpg')
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

image2 = cv2.imread('Samples/2.jpg')
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

image3 = cv2.imread('Samples/3.jpg')
gray3 = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)

image4 = cv2.imread('Samples/4.jpg')
gray4 = cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY)

image5 = cv2.imread('Samples/5.jpg')
gray5 = cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY)

#storing image to test
image_test = cv2.imread('Samples/test.jpg')
gray_test = cv2.cvtColor(image_test,cv2.COLOR_BGR2GRAY)

#filter size
rows = 300
cols = 200

#averaging out the weights of sample images
final = gray1 + gray2 + gray3 + gray4 + gray5
final = final/5

#comparing the weights and giving a score
test = gray_test
count = 0
for i in range(rows):
	for j in range(cols):
		if final[i][j]-test[i][j]<10:
			count = count + 1

#printing the score in %
print(count/(rows*cols))




