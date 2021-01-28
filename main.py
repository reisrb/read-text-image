import pytesseract
from flask import Flask, request, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import cv2
# from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/image', methods=['POST'])
def image_to_string():
  file = request.files['file']

  filename = secure_filename(file.filename)
  path = os.path.join('./temp', filename)
  file.save(path)

  # img = Image.open(path)
  img = cv2.imread(path)
  environment_clean_up()
  return pytesseract.image_to_string(img)

def environment_clean_up():
  try:
    path = './temp'
    dir = os.listdir(path)
    for file in dir:
      os.remove(os.path.join(path, '{0}'.format(file)))
  except Exception as error:
    raise Exception('Error on environmentCleanUp: %s ' % str(error))

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)