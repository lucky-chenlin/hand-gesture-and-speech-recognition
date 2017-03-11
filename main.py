# coding:utf-8
from svm_train import * 
from hand_pose3 import *
from voice import *
from tts import *
from ui import *
import sys
from PyQt4 import QtGui, QtCore

class MyClient(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self._hand)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()'), self._picture)
        
    def _hand(self):
    	hand_pose(model,move_text)
    def _picture(self):
    	baidu_asr()

if __name__ == '__main__':
	model=trainSVM(9,200,'traindata4')
	move_text={'1':' ','2':'谌林','3':'是','4':'看见','5':'非常','6':'开心','7':'好','8':'你','9':'我'}
	print "欢迎使用手语交流宝"
	TTS("欢迎使用手语交流宝")
	app = QtGui.QApplication(sys.argv)
	my = MyClient()
	my.show()
	sys.exit(app.exec_())