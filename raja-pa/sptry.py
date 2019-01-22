import speech_recognition as sr
import speech
import lang
import functions
import checkinternet as ci
r = sr.Recognizer()
def listen(on):
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		if on==True:
			a=str(r.recognize_google(audio))
		else:
			a=str(r.recognize_sphinx(audio))
		print(a)
		flag=1
		if a.lower() is 'i am not talking to you':
			flag=0
		elif a.lower() is 'listen to me':
			flag=1
		if flag==1:
			listento(a)
	except:
		None
def listento(a):
	if "raja" in a.lower():
		a=a.lower()
		a=a.lstrip("raja")
		functions.command(a)
	else:
		lang.reply(a)
if __name__=="__main__":
	b=1
	inon=ci.in_on()
	speech.say("Started listening")
	while b:
		listen(inon)