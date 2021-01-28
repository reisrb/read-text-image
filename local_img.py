import pytesseract
import cv2
import sys

def image_string(argv):
  img = cv2.imread(argv[1])
  print(pytesseract.image_to_string(img))

if __name__ == '__main__':
  image_string(sys.argv)

# Run the command for execute script " python3 local_img.py 'img.*' "