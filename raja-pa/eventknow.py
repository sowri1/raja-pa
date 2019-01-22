import datetime
import MySQLdb
import speech
import time
def remindevent():
	db = MySQLdb.connect(host="localhost",
						 user="root",
						 passwd="6461",
						 db="mine")

	now=datetime.datetime.now()
	cyear=now.year
	cmonth=now.month
	cday=now.day
	cur = db.cursor()
	cur.execute("SELECT * FROM `event_manager`")
	events=cur.fetchall()
	for ev in events:
		if ev[1] is cmonth:
			if ev[2] is cday:
				speech.say("Today is "+ev[4]+" "+ev[3])
a=1
while(a):
	remindevent()
	time.sleep(300)