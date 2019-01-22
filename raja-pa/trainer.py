import cv2,os
import numpy as np
from PIL import Image

def train():
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	cascadePath = "Classifiers/face.xml"
	faceCascade = cv2.CascadeClassifier(cascadePath);
	path = 'dataSet'

	def get_images_and_labels(path):
		 image_paths = [os.path.join(path, f) for f in os.listdir(path)]
		 images = []
		 labels = []
		 for image_path in image_paths:
			 image_pil = Image.open(image_path).convert('L')
			 image = np.array(image_pil, 'uint8')
			 nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
			 faces = faceCascade.detectMultiScale(image)
			 for (x, y, w, h) in faces:
				 images.append(image[y: y + h, x: x + w])
				 labels.append(nbr)
				 cv2.waitKey(10)
		 return images, labels

	images, labels = get_images_and_labels(path)
	recognizer.train(images, np.array(labels))
	recognizer.save('trainer/trainer.yml')
	cv2.destroyAllWindows()

if __name__=="__main__":
	train()