import pyodbc

db = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost\sqlexpress;'
    r'DATABASE=mine;'
    r'UID=sa;'
    r'PWD=6461'
    )

cur = db.cursor()
def retnum():
	import os
	path = 'dataSet'
	image_paths = [os.path.join(path, f) for f in os.listdir(path)]
	nbr=0
	for image_path in image_paths:
		nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
	nbr=nbr+1
	return nbr
def retname(num):
	cur.execute("SELECT * FROM [dbo].[face]")
	nid=cur.fetchall()
	print(nid)
	cur.commit()
	for id in nid:
		if id[1]==num:
			return id[0]

if __name__=="__main__":
	retname(1)