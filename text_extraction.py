'''
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-all
sudo apt-get install imagemagick
'''
from PIL import Image
from pytesseract import pytesseract

def image_to_string(image):

    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    result = text.strip().lower().replace('\n', ' ')

    return result

def main():

    image_path = "handwritten.jpeg"
    print(image_to_string(image_path))


if __name__=='__main__':
    main()
