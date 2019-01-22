import cv2
import name as nmi
import os
#import speech
import trainer
import pyodbc

db = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost\sqlexpress;'
    r'DATABASE=mine;'
    r'UID=sa;'
    r'PWD=6461'
    )

cur = db.cursor()
cur.execute("SELECT * from face")
favail=cur.fetchall()

def addfaceid(namei,idi):
	cur.execute("USE [mine] INSERT INTO [dbo].[face]([name], [id]) VALUES ('"+namei+"','"+str(idi)+"')")
	cur.commit()

def addface(nam):
	cam = cv2.VideoCapture(0)
	detector=cv2.CascadeClassifier('Classifiers/face.xml')
	i=0
	offset=50
	path = 'dataSet'
	image_paths = [os.path.join(path, f) for f in os.listdir(path)]
	flag=1
	num=nmi.retnum()
	if favail is not None:
		for na in favail:
			if na[0]==nam:
				flag=0
				num=na[1]
				for image_path in image_paths:
					if int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))==num:
						i+=1
	print(image_paths)
	
	tot=0
	print(nam,num)
	if flag==1:
		addfaceid(nam,num)
	while True:
		tot+=1
		ret, im =cam.read()
		gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
		for(x,y,w,h) in faces:
			i=i+1
			cv2.imwrite("dataSet/face-"+str(num)+'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
			cv2.imshow("Adding faces to traning set...", im[y: y + h, x: x + w])
			cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
			cv2.waitKey(100)
		if tot>20:
			cam.release()
			cv2.destroyAllWindows()
			break
	print("face successfully added")
	trainer.train()
if __name__=="__main__":
	addface('sowri')