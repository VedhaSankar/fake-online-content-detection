
from PIL import Image
from pytesseract import pytesseract
  

# path_to_tesseract = r"/home/ishita/miniconda3/envs/ml38/bin/pytesseract"

image_path = "test2.jpg"
  
img = Image.open(image_path)

  

# pytesseract.tesseract_cmd = path_to_tesseract

# extract the text from the image
text = pytesseract.image_to_string(img)
  
print(text[:-1])

