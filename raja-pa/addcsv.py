import csv
import pandas as pd
from datetime import datetime as dt
import sys
import subprocess,os
df = pd.read_csv("people.csv")
def addlastseen(name):
	ii=-1
	f=open('people.csv','r')
	r=csv.DictReader(f)
	for row in r:
		ii+=1
		if row['name']==name:
			df.set_value(ii,'mon',int(dt.now().month))
			df.set_value(ii,'day',int(dt.now().day))
			df.set_value(ii,'hour',int(dt.now().hour))
			df.set_value(ii,'min',int(dt.now().minute))
			df.to_csv("people.csv", index=False)
if __name__=="__main__":
	name=sys.argv[1]
	addlastseen(name)