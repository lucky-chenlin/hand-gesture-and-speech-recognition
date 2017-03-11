import cv2
import numpy as np
import util as ut

cam=int(raw_input("Enter Camera Index : "))
cap=cv2.VideoCapture(cam)
train_folder=raw_input("Enter Train Folder name : ")
i=1
j=161
name=""

while(cap.isOpened()):
	_,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,th1 = cv2.threshold(gray.copy(),100,255,cv2.THRESH_BINARY)
	_,contours,hierarchy = cv2.findContours(th1.copy(),cv2.RETR_EXTERNAL, 2)
	cnt=ut.getMaxContour(contours,4000)
	if cnt!=None:
		x,y,w,h = cv2.boundingRect(cnt)
		imgT=img[y:y+h,x:x+w]
		imgT=cv2.bitwise_and(imgT,imgT,mask=th1[y:y+h,x:x+w])
		imgT=cv2.resize(imgT,(200,200))
		imgTG=cv2.cvtColor(imgT,cv2.COLOR_BGR2GRAY)
		cv2.imshow('Trainer',imgTG)
	cv2.imshow('Frame',img)
	cv2.imshow('Thresh',th1)
	k = 0xFF & cv2.waitKey(10)
	if k == 27:
		break
	if k == ord('s'):
		name=str(i)+"_"+str(j)+".jpg"
		cv2.imwrite(train_folder+'/'+name,imgTG)
		if(j<200):
			j+=1
		else:
			while(0xFF & cv2.waitKey(0)!=ord('n')):
				j=161
			j=161
			i+=1
		

cap.release()        
cv2.destroyAllWindows()
