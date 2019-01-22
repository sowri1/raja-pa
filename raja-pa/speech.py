import speech_recognition as sr
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
def say(text):
	speak.Speak(text)
def input():
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		a=str(r.recognize_google(audio))
		return a
	except:
		None