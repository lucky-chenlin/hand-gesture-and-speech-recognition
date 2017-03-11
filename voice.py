# coding:utf-8
import uuid
import base64
import json
import urllib2
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PyQt4 import QtGui, QtCore
def baidu_asr():
	asr_server='http://vop.baidu.com/server_api'
	Api_Key='ZiGDlOiZc2Q4K64wTfgRNtDSwpZKrd8C'
	Secrect_Key='kGv5G5a04IVfQjMo5cAUjd3srGbSMKFS'
	url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+Api_Key+'&client_secret='+Secrect_Key
	res=urllib2.urlopen(url).read().decode('utf-8')
	data=json.loads(res)
	access_token=data['access_token']
	mac_address=uuid.UUID(int=uuid.getnode()).hex[-12:]
	os.system('arecord -D "plughw:1,0" -f S16_LE -d 3 -r 8000 file.wav')
	#print 'done..'
	speech_file='file.wav'
	with open(speech_file,'rb') as f:
		speech_data=f.read()
	speech_base64=base64.b64encode(speech_data).decode('utf-8')
	speech_length=len(speech_data)
	data_dict={'format':'wav','rate':8000,'channel':1,'cuid':mac_address,'token':access_token,'lan':'zh','speech':speech_base64,'len':speech_length}
	json_data=json.dumps(data_dict).encode('utf-8')
	json_length=len(json_data)
	request=urllib2.Request(url=asr_server)
	request.add_header("Content-Type","application/json")
	request.add_header("Content-Length",json_length)
	fs=urllib2.urlopen(url=request,data=json_data)
	result_str=fs.read().decode('utf-8')
	json_resp=json.loads(result_str)
	if json_resp['err_msg']=='success.':
		print json_resp['result'][0]
		length=len(json_resp['result'][0])
		plt.figure(1)
		a=u'陈玲' in json_resp['result'][0]
		if a:
			img = mpimg.imread('traindata4/2_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'陈玲')+1))
			plt.imshow(img)
			plt.axis('off')
		b=u'是' in json_resp['result'][0]
		if b:
			img = mpimg.imread('traindata4/3_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'是')+1))
			plt.imshow(img)
			plt.axis('off')
		c=u'看见' in json_resp['result'][0]
		if c:
			img = mpimg.imread('traindata4/4_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'看见')+1))
			plt.imshow(img)
			plt.axis('off')
		d=u'非常' in json_resp['result'][0]
		if d:
			img = mpimg.imread('traindata4/5_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'非常')+1))
			plt.imshow(img)
			plt.axis('off')
		e=u'开心' in json_resp['result'][0]
		if e:
			img = mpimg.imread('traindata4/6_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'开心')+1))
			plt.imshow(img)
			plt.axis('off')
		f=u'好' in json_resp['result'][0]
		if f:
			img = mpimg.imread('traindata4/7_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'好')+1))
			plt.imshow(img)
			plt.axis('off')
		g=u'你' in json_resp['result'][0]
		if g:
			img = mpimg.imread('traindata4/8_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'你')+1))
			plt.imshow(img)
			plt.axis('off')
		h=u'我' in json_resp['result'][0]
		if h:
			img = mpimg.imread('traindata4/9_1.jpg')
			plt.subplot('1'+str(length)+str(json_resp['result'][0].find(u'我')+1))
			plt.imshow(img)
			plt.axis('off')
		plt.show()

