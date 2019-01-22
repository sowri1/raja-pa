import speech
import MySQLdb
import char
db = MySQLdb.connect(host="localhost",
					user="root",
					passwd="6461",
					db="mine")
cur = db.cursor()
def adminpassword(text):
	cur.execute("INSERT INTO `adminpasswd`(`onlypassword`) VALUES('%s')"%(text))
	x=cur.execute("SELECT `onlypassword` FROM `adminpasswd` ")
	x=cur.fetchone()
	x=x[0]
	if x is 0:
		speech.say("there is no default password to access accounts. Would you like to activate the password?")
		inp=speech.input('')
		inp=inp.lower()
		if inp=='yes':
			speech.say("Say the password")
			passwd=speech.input()
			passwd=passwd.lower()
			speech.say("To activate the accounts say it again")
			passwd1=speech.input()
			passwd1=passwd1.lower()
			if passwd==passwd1:
				adminpassword(passwd)
				speech.say("password activate successfully")
def rempassword():
	speech.say("Which password would you like to add?")
	act=speech.input()
	print(act)
	speech.say("Say COMPLETED when you say password completely")
	speech.say("Now say the password letter by letter")
	passwd=speech.input()
	passwd=passwd.lower()
	fr=''
	while passwd!="completed" and passwd!="Completed":
		fr=fr+char.retchar(passwd.lower())
		print(fr)	
		speech.say("next")
		passwd=speech.input()
		print(passwd)
	print(passwd)
	speech.say("to confirm say the password again by following the previous steps")
	speech.say("start saying the password again")
	passwd1=speech.input()
	passwd1=passwd1.lower()
	sr1=''
	while passwd1!="completed" or passwd1!="Completed":
		sr1=sr1+char.retchar(passwd1)
		print(sr1)
		speech.say("next")
		passwd1=speech.input()
		passwd1=passwd1.lower()
	if fr==sr1:
		cur.execute("INSERT INTO `act_password`(`account`,`password`) VALUES('%s','%s')"%(act,sr))
	else:
		speech.say("Sorry, the passwords do not match.")
		speech.say("try again later")
def tellpassword():
	x=cur.execute("SELECT `onlypassword` FROM `adminpasswd` ")
	x=cur.fetchone()
	x=x[0]
#	speech.say("In order to view passwords, first verify your identity")
	speech.say("Say admin password")
	admpass=speech.input()
	print(admpass)
	x=x.lower()
	if admpass.lower()==x:
		speech.say("identity verified")
		speech.say("which password do you want to view?")
		act=speech.input()
		print(act)
		cur.execute("SELECT * from `act_password`")
		acts=cur.fetchall()
		flag=1
		for ac in acts:
			if ac[0]==act.lower():
				speech.say("The password for "+str(act)+" is "+str(ac[1]))
				flag=0
		if flag:
			speech.say("Sorry. Account not found")
	else:
		speech.say("Identity unverified")
		speech.say("Try again after some time")