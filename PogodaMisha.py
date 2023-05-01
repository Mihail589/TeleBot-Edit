import cv2
def cartina(ib, out, name, name_out):
	fase_cas = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
	img = cv2.imread(f"{ib}/{name}")
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	fase = fase_cas.detectMultiScale(img_gray, 1.1, 19)
	for (x, y, w, h) in fase:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imwrite(f"{out}/{name_out}", img)