import cv2
from PIL import Image;
print(cv2.__version__)

hog = cv2.HOGDescriptor()
image = cv2.imread("1")

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


foundLocations, weight = hog.detectMultiScale(image)
print(foundLocations)

for (x,y,w,h) in foundLocations:
	cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
	
cv2.imshow('Image', image)
rgb_img = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)

ims = Image.fromarray(rgb_img)
ims.save('cv2_result_pre.jpg', format="JPEG", quality=90)
cv2.waitKey(0)
cv2.destroyAllWindows()
