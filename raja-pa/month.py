def retmon(text):
	try:	
		return{
			"january":1,
			"february":2,
			"march":3,
			"april":4,
			"may":5,
			"june":6,
			"july":7,
			"august":8,
			"sptember":9,
			"october":10,
			"november":11,
			"december":12
		}[text]
	except:
		return ""
if __name__=="__main__":
	print(retmon("june"))