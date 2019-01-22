import num
import speech
from num2words import num2words
def retop(text,a,b):
	try:
		return{
			"into ":a*b,
			"by ":a/b,
			"plus ":a+b,
			"minus ":a-b,
			"multiplied by ":a*b,
			"times ":a*b,
			"divided by ":a/b
		}[text]
	except:
		speech.say("Sorry. but i ain't capable of doing the operation")
def find(text):
	text=num.text2int(text)
	fin=text.split()
	a=int(fin[0])
	b=int(fin[-1])
	c=''
	for i in range(1,len(fin)-1):
		c+=str(fin[i])
		c+=" "
	st=str(text)+' = '+str(num2words(retop(c,a,b)))
	speech.say(st)
if __name__=="__main__":
	find('5 multiplied by 2')