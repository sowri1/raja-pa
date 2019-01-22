import datetime
import time
from playsound import playsound
import speech
import winsound
import os
import MySQLdb
db = MySQLdb.connect(host="localhost",
					user="root",
					passwd="6461",
					db="mine")
def counter(dursec,durmin,durhour):
	a=dursec
	a+=durmin*60
	a+=durhour*3600
	time.sleep(a)
	speech.say("time up")
	playsound('audios/timup.mp3')
def addalarm(hrs,min,dur,date,mon):
	cur = db.cursor()
	cur.execute("INSERT INTO `alarm`(`hrs`, `min`, `dur`, `date`, `mon`) VALUES (%d,%d,%d,%d,%d)"%(hrs,min,dur,date,mon))
	db.close()
	speech.say("Alarm successfully added")
def checkalarm():
	now=datetime.datetime.now()
	cur = db.cursor()
	cur.execute("SELECT * FROM `alarm`")
	alarms=cur.fetchall()
	a=1
	while a:
		for ev in alarms:
			if int(ev[4])==datetime.datetime.now().month and int(ev[3])==datetime.datetime.now().day and int(ev[2])==int(datetime.datetime.now().hour)//12+1 and int(ev[1])==int(datetime.datetime.now().minute) and int(ev[0])==int(datetime.datetime.now().hour)%12:
				speech.say("wake up")
				playsound("audios/timup.mp3")
				a=0
if __name__=="__main__":
	addalarm(9,0,1,12,4)