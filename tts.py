# coding:utf-8
import requests
import urllib
import os
def tts(str):
    s = requests.Session()
    s.get("http://tts.baidu.com/text2audio?lan=zh&pid=101&ie=UTF-8&text=" + urllib.quote(str))
    res = s.get("http://tts.baidu.com/text2audio?lan=zh&pid=101&ie=UTF-8&text=" + urllib.quote(str)).content
    f = open("tts-temp.mp3", "w")
    f.write(res)
    f.close()

def say():
    os.system("play tts-temp.mp3")

def over():
    os.system("rm tts-temp.mp3")

def TTS(str):
    tts(str)
    say()
    over()

