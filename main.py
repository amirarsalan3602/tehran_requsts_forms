import requests
import re
import json
from bs4 import BeautifulSoup
import html_to_json


# completed
def verification_token():
    url = "https://eforms.tehran.ir/sport-Champion/Individual-competition"
    header = {
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Linux',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.get(url=url, headers=header)
    pattern = r'__RequestVerificationToken=([^;]+);'
    pattern2 = r'.ASPXANONYMOUS=([^;]+);'
    match = re.search(pattern, response.headers['Set-Cookie'])
    match2 = re.search(pattern2, response.headers['Set-Cookie'])
    if match:
        verifier_token = match.group(1)
        if match2:
            anonymous_token = match2.group(1)
            return [anonymous_token, verifier_token]
    else:
        return None


# completed
def sports_field():
    tokens = verification_token()
    # Gender (زن) (مرد)
    while True:
        i = int(input("Gender selection : \n 1 - زن \n 2 - مرد \n enter a number : Ex. 1"))
        if i == 1:
            Gender = 'زن'
            break
        elif i == 2:
            Gender = 'مرد'
            break
        else:
            print('Enter a friend number !!')
    url = "https://eforms.tehran.ir/DesktopModules/DnnSharp/ActionForm/GetItems.ashx?_portalId=0&openMode=Always&_tabId=99&_alias=eforms.tehran.ir&_mid=518&language=fa-IR&fieldId=5266&fieldName=sport"
    header = {
        'Cookie': f'.ASPXANONYMOUS=m-ChniPk6jVu6aTZresTMxkbMKcwbiJ0kWdNxP9f9wqcFGTYGAKBVBnUyF_qRuCHVzkQ7CYoo-8qte-OLia_Tkq8gR9NuNYP_EOu8gokQ6GjVE3g0; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken=aSOZPelYnP9lFaaPV9Ot0d6uSpcL5sP5PACigABySmXC3TwLezvoF86v6osJ-hDjKlYNKw2; _pk_ses.429.2640=1',
        'Content-Length': '0',
        'Tabid': '99',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Requestverificationtoken': "IixrTLahZIeB8Po8idggBQtN1PiP8nFpb0Tr6L_iFzC2W2q0ApZnbThapZ8Fd57xj65OiA2",
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Moduleid': '518',
        'Dnnsf-Time-Offset': '-210',
        'Sec-Ch-Ua-Platform': "Linux",
        'Origin': 'https://eforms.tehran.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,',
    }

    # header2 = {
    #     'Cookie': f'.ASPXANONYMOUS={a}; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken={tokens}; _pk_ses.429.2640=1',
    #     'Content-Length': '0',
    #     'Tabid': '99',
    #     'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    #     'Requestverificationtoken': f"{tokens}",
    #     'Sec-Ch-Ua-Mobile': '?0',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Accept': 'application/json, text/plain, */*',
    #     'Moduleid': '518',
    #     'Dnnsf-Time-Offset': '-210',
    #     'Sec-Ch-Ua-Platform': "Linux",
    #     'Origin': 'https://eforms.tehran.ir',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'en-US,en;q=0.9,',
    # }
    Data = {
        'StaticText': '<div class="header"> <h2> <img src="/Portals/0/Images/form-icons/icons-form.png">قهرمان شهر (مسابقه انفرادی)</h2></div>',
        'gender': Gender,
        'sport': '',
        'age': '',
        'name': '',
        'family': '',
        'codemeli': '',
        'mobile': '',
        'code': '',
        'sayer': '',
        'region': '',
        'nahie': '',
        'mahale': '',
        'date': '',
        'StaticText1': '<p class="uploat-text">** خواهشمند است عکس خود را در این بخش آپلود نمایید.<br />با فرمت jpg، jpeg، png و نهایتا با حجم 1 مگابایت </p>',
        'TrueFalseCheckbox': 'False',
        'TrueFalseCheckbox2': 'False',
        'CAPTCHAcaptchaenc': 'EA2A8DDEDA4CBD0100DC668A4EB1B69A9A957AFEA54209786EC25256E8A197A5CC53E7E350889D0F48FBC8263679E67E00AD4AD6787E29BFEA569F64A805EF680B5B74764C3EFA05B07A18621DDC054E6473E283790026FD2AAAA4F02E118ECE361B4F4D863BCED6651D489EC73A72D9C60A085153CDD53FBB2CE9C4',
        'CAPTCHA': '',
        'Submit': '',
        'SingleFileUpload': '{"name":"","state":""}'
    }

    response = requests.post(url=url, headers=header, data=Data)
    data_json = json.loads(response.text)
    counter = 0
    for i in data_json:
        counter += 1
        print(f"{i['text']} - {counter}")
    i = int(input("Please enter a number : "))
    if i > len(data_json):
        print('error')
    else:
        return {'sport': data_json[i - 1]['path'], 'gender': Gender}


# completed
def ages():
    sports = sports_field()
    url = 'https://eforms.tehran.ir/DesktopModules/DnnSharp/ActionForm/GetItems.ashx?_portalId=0&openMode=Always&_tabId=99&_alias=eforms.tehran.ir&_mid=518&language=fa-IR&fieldId=5267&fieldName=age'
    header = {
        'Cookie': '.ASPXANONYMOUS=m-ChniPk6jVu6aTZresTMxkbMKcwbiJ0kWdNxP9f9wqcFGTYGAKBVBnUyF_qRuCHVzkQ7CYoo-8qte-OLia_Tkq8gR9NuNYP_EOu8gokQ6GjVE3g0; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken=aSOZPelYnP9lFaaPV9Ot0d6uSpcL5sP5PACigABySmXC3TwLezvoF86v6osJ-hDjKlYNKw2; _pk_ses.429.2640=1',
        'Content-Length': '1428',
        'Tabid': '99',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Requestverificationtoken': 'WQ7Q0Sud9iVoafDxFEWgiErZE_wNb7gJ6vUjCne10-Q67wW1Qcg_PVTPyiQmLb4-Xoz7LQ2',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Moduleid': '518',
        'Dnnsf-Time-Offset': '-210',
        'Sec-Ch-Ua-Platform': "Linux",
        'Origin': 'https://eforms.tehran.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    Data = {
        'StaticText': '<div class="header"> <h2> <img src="/Portals/0/Images/form-icons/icons-form.png">قهرمان شهر (مسابقه انفرادی)</h2></div>',
        'gender': sports['gender'],
        'sport': sports['sport'],
        'age': '',
        'name': '',
        'family': '',
        'codemeli': '',
        'mobile': '',
        'code': '',
        'sayer': '',
        'region': '',
        'nahie': '',
        'mahale': '',
        'date': '',
        'StaticText1': '<p class="uploat-text">** خواهشمند است عکس خود را در این بخش آپلود نمایید.<br />با فرمت jpg، jpeg، png و نهایتا با حجم 1 مگابایت </p>',
        'TrueFalseCheckbox': 'False',
        'TrueFalseCheckbox2': 'False',
        'CAPTCHAcaptchaenc': 'EA2A8DDEDA4CBD0100DC668A4EB1B69A9A957AFEA54209786EC25256E8A197A5CC53E7E350889D0F48FBC8263679E67E00AD4AD6787E29BFEA569F64A805EF680B5B74764C3EFA05B07A18621DDC054E6473E283790026FD2AAAA4F02E118ECE361B4F4D863BCED6651D489EC73A72D9C60A085153CDD53FBB2CE9C4',
        'CAPTCHA': '',
        'Submit': '',
        'SingleFileUpload': '{"name":"","state":""}'
    }
    response = requests.post(url=url, headers=header, data=Data)
    data_json = json.loads(response.text)
    counter = 0
    for i in data_json:
        counter += 1
        print(f"{i['text']} - {counter}")
    i = int(input("Please enter a number : "))
    if i > len(data_json):
        print('error')
    else:
        return {'age': data_json[i - 1]['path'], 'gender': sports['gender'], 'sport': sports['sport']}


captcha = {}  # {'src': #, "completed": #}


# completed
def area():
    d = ages()
    url = 'https://eforms.tehran.ir/API/DnnSharp/ActionForm//settings/initializeForm?_portalId=0&referrer=&openMode=Always&_tabId=99&_alias=eforms.tehran.ir&_mid=518&_url=https%3A%2F%2Feforms.tehran.ir%2Fsport-Champion%2FIndividual-competition&language=fa-IR'
    header = {
        'Cookie': '.ASPXANONYMOUS=m-ChniPk6jVu6aTZresTMxkbMKcwbiJ0kWdNxP9f9wqcFGTYGAKBVBnUyF_qRuCHVzkQ7CYoo-8qte-OLia_Tkq8gR9NuNYP_EOu8gokQ6GjVE3g0; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken=aSOZPelYnP9lFaaPV9Ot0d6uSpcL5sP5PACigABySmXC3TwLezvoF86v6osJ-hDjKlYNKw2',
        'Content-Length': '0',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Requestverificationtoken': '0ZeEnuVXuiZpDFVf-h-876fGC6RGarLW3tIwJ71ffUZKa19MHN2Pp9c9GXv87n0XCF0nzg2',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Dnnsf-Time-Offset': '-210',
        'Sec-Ch-Ua-Platform': "Linux",
        'Origin': 'https://eforms.tehran.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.post(url=url, headers=header)
    data_json = json.loads(response.text)
    counter = 0
    soup = BeautifulSoup(data_json['Html'], "html.parser")
    captcha['src'] = html_to_json.convert(str(soup.find('img')))['img'][0]['_attributes']['src']
    captcha['Acaptchaenc'] = captcha['src'].replace('/ImageChallenge.captcha.aspx?captcha=', '')
    captcha['Acaptchaenc'] = captcha['Acaptchaenc'].replace('&alias=eforms.tehran.ir', '')
    for i in data_json['Data']['fields']['region']['options']:
        counter += 1
        print(f"{i['text']} - {counter}")
    i = int(input("Please enter a number : "))
    if i > len(data_json['Data']['fields']['region']['options']):
        print('error')
    else:
        return {'region': data_json['Data']['fields']['region']['options'][i - 1]['path'], 'gender': d['gender'],
                'sports': d['sport'], 'age': d['age']}


# completed
def district():
    d = area()
    url = "https://eforms.tehran.ir/DesktopModules/DnnSharp/ActionForm/GetItems.ashx?_portalId=0&openMode=Always&_tabId=99&_alias=eforms.tehran.ir&_mid=518&language=fa-IR&fieldId=5273&fieldName=nahie"
    header = {
        'Cookie': '.ASPXANONYMOUS=m-ChniPk6jVu6aTZresTMxkbMKcwbiJ0kWdNxP9f9wqcFGTYGAKBVBnUyF_qRuCHVzkQ7CYoo-8qte-OLia_Tkq8gR9NuNYP_EOu8gokQ6GjVE3g0; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken=aSOZPelYnP9lFaaPV9Ot0d6uSpcL5sP5PACigABySmXC3TwLezvoF86v6osJ-hDjKlYNKw2',
        'Content-Length': '1325',
        'Tabid': '99',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Requestverificationtoken': '0ZeEnuVXuiZpDFVf-h-876fGC6RGarLW3tIwJ71ffUZKa19MHN2Pp9c9GXv87n0XCF0nzg2',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Moduleid': '518',
        'Dnnsf-Time-Offset': '-210',
        'Sec-Ch-Ua-Platform': "Linux",
        'Origin': 'https://eforms.tehran.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    Data = {
        'StaticText': '<div class="header"> <h2> <img src="/Portals/0/Images/form-icons/icons-form.png">قهرمان شهر (مسابقه انفرادی)</h2></div>',
        'gender': d['gender'],
        'sport': d['sports'],
        'age': d['age'],
        'name': '',
        'family': '',
        'codemeli': '',
        'mobile': '',
        'code': '',
        'sayer': '',
        'region': d['region'],
        'nahie': '',
        'mahale': '',
        'date': '',
        'StaticText1': '<p class="uploat-text">** خواهشمند است عکس خود را در این بخش آپلود نمایید.<br />با فرمت jpg، jpeg، png و نهایتا با حجم 1 مگابایت </p>',
        'TrueFalseCheckbox': 'False',
        'TrueFalseCheckbox2': 'False',
        'CAPTCHAcaptchaenc': d['captcha_token'],
        'CAPTCHA': '',
        'Submit': '',
        'SingleFileUpload': '{"name":"","state":""}'
    }
    response = requests.post(url=url, headers=header, data=Data)
    data_json = json.loads(response.text)
    counter = 0
    for i in data_json:
        counter += 1
        print(f"{i['text']} - {counter}")
    i = int(input("Please enter a number : "))
    if i > len(data_json):
        print('error')
    else:
        return {'region': d['region'], 'gender': d['gender'],
                'sports': d['sports'], 'age': d['age'], 'district': data_json[i - 1]['path'],
                "captcha_token": d['captcha_token'], "captcha_src": d['captcha_src']}


# completed
def parish():
    d = district()
    url = "https://eforms.tehran.ir/DesktopModules/DnnSharp/ActionForm/GetItems.ashx?_portalId=0&openMode=Always&_tabId=99&_alias=eforms.tehran.ir&_mid=518&language=fa-IR&fieldId=5274&fieldName=mahale"
    header = {
        'Cookie': '.ASPXANONYMOUS=m-ChniPk6jVu6aTZresTMxkbMKcwbiJ0kWdNxP9f9wqcFGTYGAKBVBnUyF_qRuCHVzkQ7CYoo-8qte-OLia_Tkq8gR9NuNYP_EOu8gokQ6GjVE3g0; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken=aSOZPelYnP9lFaaPV9Ot0d6uSpcL5sP5PACigABySmXC3TwLezvoF86v6osJ-hDjKlYNKw2; _pk_ses.429.2640=1',
        'Content-Length': '1334',
        'Tabid': '99',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Requestverificationtoken': '6BaTP5e-onGLuBy8EtwOrHuReu3A6vvDqCVYJ7xb37Gc3WCkHFqOwysfiA-8TkrlQUdNBA2',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'Moduleid': '518',
        'Dnnsf-Time-Offset': '-210',
        'Sec-Ch-Ua-Platform': "Linux",
        'Origin': 'https://eforms.tehran.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    Data = {
        'StaticText': '<div class="header"> <h2> <img src="/Portals/0/Images/form-icons/icons-form.png">قهرمان شهر (مسابقه انفرادی)</h2></div>',
        'gender': d['gender'],
        'sport': d['sports'],
        'age': d['age'],
        'name': '',
        'family': '',
        'codemeli': '',
        'mobile': '',
        'code': '',
        'sayer': '',
        'region': d['region'],
        'nahie': d['district'],
        'mahale': '',
        'date': '',
        'StaticText1': '<p class="uploat-text">** خواهشمند است عکس خود را در این بخش آپلود نمایید.<br />با فرمت jpg، jpeg، png و نهایتا با حجم 1 مگابایت </p>',
        'TrueFalseCheckbox': 'False',
        'TrueFalseCheckbox2': 'False',
        'CAPTCHAcaptchaenc': 'EA2A8DDEDA4CBD0100DC668A4EB1B69A9A957AFEA54209786EC25256E8A197A5CC53E7E350889D0F48FBC8263679E67E00AD4AD6787E29BFEA569F64A805EF680B5B74764C3EFA05B07A18621DDC054E6473E283790026FD2AAAA4F02E118ECE361B4F4D863BCED6651D489EC73A72D9C60A085153CDD53FBB2CE9C4',
        'CAPTCHA': '',
        'Submit': '',
        'SingleFileUpload': '{"name":"","state":""}'
    }
    response = requests.post(url=url, headers=header, data=Data)
    data_json = json.loads(response.text)
    counter = 0
    for i in data_json:
        counter += 1
        print(f"{i['text']} - {counter}")
    i = int(input("Please enter a number : "))
    if i > len(data_json):
        print('error')
    else:
        return {'region': d['region'], 'gender': d['gender'],
                'sports': d['sports'], 'age': d['age'], 'district': d['district'],
                "parish": data_json[i - 1]['path'], "captcha_token": d['captcha_token'],
                "captcha_src": d['captcha_src']}


# Not completed
def submit():
    d = parish()
    lname = input("Enter a name  :")
    fname = input("Enter a Family name : ")
    melicode = input("enter a codemeli : ")
    phone_N = input("Enter a phone Number : ")
    Date = input("Enter a birthday : ")

    url = "https://eforms.tehran.ir/DesktopModules/DnnSharp/ActionForm/Submit.ashx?_portalId=0&openMode=Always&_tabId=99&_alias=eforms.tehran.ir&_mid=518&language=fa-IR&event=click&b=5281&referrer=&_url=https%3A%2F%2Feforms.tehran.ir%2Fsport-Champion%2FIndividual-competition"
    header = {
        'Cookie': '.ASPXANONYMOUS=m-ChniPk6jVu6aTZresTMxkbMKcwbiJ0kWdNxP9f9wqcFGTYGAKBVBnUyF_qRuCHVzkQ7CYoo-8qte-OLia_Tkq8gR9NuNYP_EOu8gokQ6GjVE3g0; _pk_id.429.2640=0e0b90cd7d72cb27.1689094065.; dnn_IsMobile=False; language=fa-IR; __RequestVerificationToken=aSOZPelYnP9lFaaPV9Ot0d6uSpcL5sP5PACigABySmXC3TwLezvoF86v6osJ-hDjKlYNKw2',
        'Content-Length': '1638',
        'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
        'Requestverificationtoken': 'WQ7Q0Sud9iVoafDxFEWgiErZE_wNb7gJ6vUjCne10-Q67wW1Qcg_PVTPyiQmLb4-Xoz7LQ2',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Dnnsf-Time-Offset': '-210',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
        'Sec-Ch-Ua-Platform': "Linux",
        'Accept': '*/*',
        'Origin': 'https://eforms.tehran.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://eforms.tehran.ir/sport-Champion/Individual-competition',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    Data = {
        'StaticText': '<div class="header"> <h2> <img src="/Portals/0/Images/form-icons/icons-form.png">قهرمان شهر (مسابقه انفرادی)</h2></div>',
        'gender': d['gender'],
        'sport': d['sports'],
        'age': d['age'],
        'name': lname,
        'family': fname,
        'codemeli': melicode,
        'mobile': phone_N,
        'code': '',
        'sayer': '',
        'region': d['region'],
        'nahie': d['district'],
        'mahale': d['parish'],
        'date': Date,
        'StaticText1': '<p class="uploat-text">** خواهشمند است عکس خود را در این بخش آپلود نمایید.<br />با فرمت jpg، jpeg، png و نهایتا با حجم 1 مگابایت </p>',
        'TrueFalseCheckbox': 'False',
        'TrueFalseCheckbox2': 'False',
        'CAPTCHAcaptchaenc': captcha['Acaptchaenc'],
        'CAPTCHA': ...,
        'Submit': '',
        'SingleFileUpload': '{"name":"","state":""}'
    }
    response = requests.post(url=url, headers=header, data=Data)
