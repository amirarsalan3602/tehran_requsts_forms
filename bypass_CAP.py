import pytesseract
import cv2
import requests
from os import remove, listdir


def get_path(url):
    return url[url.find('captcha=') + 8:url.find('&alias')]


def bypass_captcha(url):
    for i in listdir('./imgs'):
        remove('./imgs/' + i)
    url = 'https://eforms.tehran.ir' + url
    with open(f'./imgs/' + get_path(url) + '.jpg', 'wb') as f:
        f.write(requests.get(url).content)
    image = cv2.imread('./imgs/' + get_path(url) + '.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(gray, lang='eng')
    return text.lower()


print(bypass_captcha(
    "/ImageChallenge.captcha.aspx?captcha=09AD94A3E3820CA4FD645EBD3243733220204763A1145AD835DABC856CE130509070B5834B174CD53C9665928F4307DF349529C746B702E4587AD4ADC6276EBFE83FA350C04A1C1EDFBCE3BC4F9739394BFCF92F25C285EA5EA1112ADF12D959A6C632ABD4069019081C8C6DB5641DF406156A4D0F799B78E0A04EAC&alias=eforms.tehran.ir"))
