import pytesseract
import cv2


# COMO INSTALAR TESSERACT EN WINDOWS:
# https://linuxhint.com/install-tesseract-windows/


filename = 'img.png'
img = cv2.imread(filename)
# img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)


# print(img)
print(text)