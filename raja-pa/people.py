import csv
import speech
class adddetails:
	def __init__(self):
		self.name=None
		self.gender=None
		self.nickname=None
		self.birthday=None
		self.number=None
		self.rest=None
		self.email=None
		self.lastseen=None
	def printdetails(self):
		print(self.name,self.gender,self.nickname,self.birthday,self.number,self.rest)
def fetchdetails(name):
	with open('people.csv') as f:
		r=csv.DictReader(f)
		ls=[]
		for row in r:
			ls.append(dict(row))
		for n in ls:
			if n['name']==name or n['nickname']==name:
				return n['name']+' is '+n['rest']
person=adddetails()
person.name="VAMSI"
person.number="9490416461"
person.nickname="japan"
person.nickname="male"
details=[[str(person.name),str(person.gender),int(person.number),str(person.email),str(person.rest)]]
f=open('people.csv','a+')
#with f:
#	wr=csv.writer(f)
#	wr.writerows(details)
speech.say(fetchdetails('sowri'))