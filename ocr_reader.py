import cv2
import pytesseract
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = 'sample_text.png'
if not os.path.exists(img_path):
    dummy_img = np.zeros((200, 500, 3), dtype=np.uint8)
    dummy_img.fill(255) 
    cv2.putText(dummy_img, 'INVOICE #0042', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
    cv2.imwrite(img_path, dummy_img)

image = cv2.imread(img_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

custom_config = r'--oem 3 --psm 11'
extracted_text = pytesseract.image_to_string(thresh, config=custom_config)

print("--- Machine Perception Output ---")
print(extracted_text.strip())