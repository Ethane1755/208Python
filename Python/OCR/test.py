from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (r"C:/Program Files/Tesseract-OCR/tesseract.exe")
TESSDATA_PREFIX=("C:/Program Files/Tesseract-OCR/tessdata")
img = Image.open("D:/USER/Desktop/test6.png")
text = pytesseract.image_to_string(img,lang='chi_tra+eng')
print(text)
