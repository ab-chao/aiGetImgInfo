from flask import Flask, request
from werkzeug.utils import secure_filename
from getImgInfo.getImgInfoCtl import GetImgInfoCtl
import os

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'\\img\\'
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
            ctl = GetImgInfoCtl()
            text = ctl.getinfo('img/' + secure_filename(file.filename))
            print(text)
            return text
    return '未能识别出图片中的文字'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
