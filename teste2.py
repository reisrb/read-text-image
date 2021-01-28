from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

output = pytesseract.image_to_string(PIL.Image.open('god.jpeg').convert("RGB"))
print(output)