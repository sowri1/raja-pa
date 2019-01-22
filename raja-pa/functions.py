import os
import speech
import mapfinal
import subprocess
from datetime import datetime as dt
import eventadd
import month
import calc
import num
import swc
import rempassword
import detector
cyear=dt.now().year
cmonth=dt.now().month
cday=dt.now().day
uname=os.getlogin()
myname="Raja"
whoami="I am your Personal Assistant"
def command(text):
	text=text.lower()
	if "what is my name" in text or "who am i" in text:
		speech.say("You are "+uname)
	elif "how are you" in text:
		speech.say("Great! How are you?")
	elif "what is your name" in text:
		speech.say("I am Raja")
	elif text == "goodbye":
		listener.stoplistening()
	elif "goto" in text:
		a=text - "goto"
		mapfinal.destination=a
	elif "shutdown" in text or "shut down" in text:
		subprocess.call(["shutdown","\s"])
	elif "restart" in text:
		subprocell.call[("restart","\r")]
	elif "log out" in text or "sign out" in text :
		subprocell.call[("shutdown"," \l")]
	elif "tomorrow" in text:
		know=text.split()
		st=''
		print(know)
		for l in range(3,len(know)):
			st+=str(know[l])+" "
		eventadd.addevent(cyear,cmonth,cday+1,st,know[2])
	elif "note an event" in text:
		left=text.lstrip("note an event ")
		fin=left.split()
		dv=fin[0].lower()
		day=num.text2int(fin[1])
		mon=int(month.retmon(dv))
		eventadd.addevent(cyear,mon,day,fin[4],fin[3])
	elif "navigate to" in text:
		destination=text.lstrip("navigate to")
		mapfinal.route(destination)
	elif "note a paragraph" in text:
		subprocell.call(["notepad.exe"])
	elif "play songs" in text or "play music" in text or "open music" in text:
		os.system("start mswindowsmusic:")
	elif "how much is" in text:
		fin=text.lstrip("how much is")
		calc.find(fin)
	elif "what is" in text:
		fin=text.lstrip("what is")
		calc.find(fin)
	elif "start counter" in text:
		speech.say("okay. starting counter.")
		speech.say("how many hours?")
		hourdur=speech.input('')
		speech.say("how many minutes?")
		mindur=speech.input('')
		speech.say("how many seconds?")
		secdur=speech.input('')
		swc.counter(secdur,mindur,hourdur)
	elif "wake me up in " in text:
		speech.say("Definitely!")
		wk=text.lstrip("wake me up in")
		a=wk.split()
		count=0
		hourdur=0
		mindur=0
		secdur=0
		for i in a:
			count+=1
		for i in range(0,count):
			if a[i]=="minutes":
				mindur=int(a[i-1])
			if a[i]=="seconds":
				secdur=int(a[i-1])
			if a[i]=="hours":
				hourdur=int(a[i-1])
		swc.counter(secdur,mindur,hourdur)
	elif "set an alarm for" in text:
		al=text.lstrip("set an alarm for")
		count=0
		hrs=None
		min=None
		if "in the morning" in al:
			ap=1
		elif "in the evening" in al or "in the night":
			ap=2
		if "o'clock" in text:
			min=0
		tt=al.split()
		for i in tt:
			count+=1
		for i in range(0,count):
			if tt[i]=="o'clock":
				hrs=int(tt[i-1])
				break
			if tt[i]=="hours":
				hrs=int(tt[i-1])
			if tt[i]=="minutes":
				min=int(tt[i-1])
		swc.addalarm(hrs,min,ap,dt.now().day,dt.now().month)
	elif "tell me a password" in text:
		rempassword.tellpassword()
	elif "who are here" in text:
		detector.whoarehere()
if __name__=="__main__":
	command("note an event june 22 is my birthday")