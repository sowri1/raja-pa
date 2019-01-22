import cv2,os
import name
import numpy as np
from PIL import Image
#	import greet
import csv
from datetime import datetime as dt
import subprocess,sys
#import speech
import addcsv

def detect():

	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read('trainer/trainer.yml')
	cascadePath = "Classifiers/face.xml"
	faceCascade = cv2.CascadeClassifier(cascadePath)
	path = 'dataSet'
	font=cv2.FONT_HERSHEY_SIMPLEX
	cam = cv2.VideoCapture(0)
	lst=[]

	while True:
		ret, im =cam.read()
		gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
		for(x,y,w,h) in faces:
			nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
			cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
			nam=name.retname(nbr_predicted)
			if nam is not None:
				if nam not in lst:
					lst.append(nam)
#					print(nam)
#					speech.say(nam)
			for ppre in lst:
				if nam!=ppre:
					addcsv.addlastseen(ppre)

def detectothers():
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read('trainer/trainer.yml')
	cascadePath = "Classifiers/face.xml"
	faceCascade = cv2.CascadeClassifier(cascadePath)
	path = 'everything/dataSet'
	cam = cv2.VideoCapture(0)
	lst=[]
	a=0
	while a<20:
		a+=1
		ret, im =cam.read()
		gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
		for(x,y,w,h) in faces:
			nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
			cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
			nam=name.retname(nbr_predicted)
			if nam is not None:
				if nam not in lst:
					lst.append(nam)
	return lst
	
def whoarehere():
	l=detectothers()
	for ppl in l:
		addcsv.addlastseen(ppl)
	for i in l:
		speech.say(str(i)	+' is here')
	
def gtwishes(name):
	f=open('people.csv','r')
	fr=csv.reader(f)
	speech.say("Hello "+name)
	for row in fr:
		if row[0]==name:
			now=dt.now()
			greet.retgreet(int(now.month-int(row[6])),int(now.day-int(row[7])),int(now.hour-int(row[8])))
			print(int(row[6]))

if __name__=="__main__":
	detectothers()
#	gtwishes