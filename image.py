# from PIL import Image
# import pytesseract
# import numpy as np
# import cv2
# import os


# filename = 'image.png'
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)


# print(text)


from PIL import Image
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe 
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"csv\d.jpg"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract 
# executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to 
# image_to_string() function
# This function will
# extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])