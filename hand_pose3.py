# coding:utf-8
import cv2
import numpy as np
import util as ut
import svm_train as st 
import time
import tts
def hand_pose(model,move_text):
	#Camera and font initialization
	cap=cv2.VideoCapture(1)
	array=[]
	array1=[]
	#The main event loop
	while(cap.isOpened()):
		move=''
		_,img=cap.read()
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		ret,th1 = cv2.threshold(gray.copy(),100,255,cv2.THRESH_TOZERO)
		_,contours,hierarchy = cv2.findContours(th1.copy(),cv2.RETR_EXTERNAL, 2)
		cnt=ut.getMaxContour(contours,4000)
		if cnt!=None:
			gesture,res=ut.getGestureImg(cnt,img,th1,model)
			cv2.imshow('PredictedGesture',gesture)
			move=move_text[res]
			array.append(move)
			if len(array)==30:
				array1.append(move)
				print move
				if len(array1)>=5:
					a=''.join(array1)
					tts.TTS(a)
					array1=[]
				array=[]  
		cv2.imshow('Frame',img)
		k = 0xFF & cv2.waitKey(10)
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()

