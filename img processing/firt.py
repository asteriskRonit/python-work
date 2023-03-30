import cv2
img=cv2.imread(r'G:\core\python\img processing\ggh.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey()
if k==27:
   exit
cv2.destroyAllWindows()