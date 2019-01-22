import speech
import MySQLdb
import detector
def retname(name):
	try:
		return{'your':'my','you':'my','yours':'mine'}[name]
	except:
		if name=="my":
			lst=detector.detectothers()
			print(lst)
			if len(lst)>1:
				speech.say("many people are there")
				speech.say("Whose is it?")
				name=speech.input("")
			else:
				name=lst[0]
			return name
		else:
			return name
def addevent(year,month,day,event_type,name):
	db = MySQLdb.connect(host="localhost",
						user="root",
						passwd="6461",
						db="mine")
	cur = db.cursor()
	name=retname(name)
	print(year,month,day)
	cur.execute("INSERT INTO `event_manager`(`year`, `month`, `day`, `event_type`, `name`) VALUES (%d,%d,%d,'%s','%s')"%(int(year),int(month),int(day),event_type,name))
	db.close()
	speech.say("Alright. Noted.")