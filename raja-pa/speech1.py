import functions
import time
import speech
#from sys import executable
#from subprocess import Popen
#Popen([executable, 'checkalarm.py'], shell=True)
#Popen([executable, 'eventknow.py'], shell=True)
def callback(phrase, listener):
	print(phrase)
	if "hello raja" in phrase.lower():
		functions.command(phrase)
#		else:		
listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)