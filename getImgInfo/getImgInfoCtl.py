import pytesseract
from PIL import Image


class GetImgInfoCtl(object):

    tessdata_dir_config = '--tessdata-dir "D:\\devSft\\Tesseract-OCR\\tessdata"'

    def getinfo(self, filename):
        pytesseract.pytesseract.tesseract_cmd = 'D:\\devSft\\Tesseract-OCR\\tesseract'
        image = Image.open(filename)
        text = pytesseract.image_to_string(image, lang='chi_sim', config=self.tessdata_dir_config)
        return text
