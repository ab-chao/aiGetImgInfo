import os

import pytesseract
from PIL import Image
from flask import Flask, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/ai/ocr/uploadImg', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = UPLOAD_FOLDER + filename
            file.save(filename)
            pytesseract.pytesseract.tesseract_cmd = 'D:\\devSft\\Tesseract-OCR\\tesseract'
            image = Image.open('img/' + secure_filename(file.filename))
            text = pytesseract.image_to_string(image, lang='chi_sim',
                                               config='--tessdata-dir "D:\\devSft\\Tesseract-OCR\\tessdata"')
            text = pytesseract.image_to_string(image, lang='chi_sim')
            print(text)
            return text
    return 'Sorry, I can\'t get the information'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
