from datetime import datetime as dt
import random
import csv
import speech
def retgreet(durmons,durdays,durhours):
	if durmons>=1:
		return [" long time no see ","it's been a long while since we met?"," months passed since we talked "][random.randint(0,2)]
	elif durdays>1:
		return [" how is it going"," where have you been all the time?"," how's your day?"][random.randint(0,2)]
	elif durhours>1:
		return [" are you busy in doing something?"," how do you do?"][random.randint(0,1)]
def greet(name):
	f=open('people.csv','r')
	rd=csv.reader(f)
	for row in rd:
		if row[0]==name:
			ls=row[6]