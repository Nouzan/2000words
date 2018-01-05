import random
import hashlib
import urllib
import http.client
import json
from keys import KEYS


def translate(word):
    data = None
    appid = KEYS['baidu']['appid']
    secretKey = KEYS['baidu']['secretKey']
    url = '/api/trans/vip/translate'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid + word + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = url + '?appid=' + appid + '&q=' + urllib.parse.quote(word) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        response = httpClient.getresponse()
        raw_data = response.read()
        # print(raw_data)
        data = json.loads(raw_data)
        # print(data)
    except Exception:
        print('error')
    finally:
        if httpClient:
            httpClient.close()
    return data
# translate('test')


def translate2(word):
    data = None
    appKey = KEYS['youdao']['appKey']
    secretKey = KEYS['youdao']['secretKey']
    url = '/api'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appKey + word + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = url + '?appKey=' + appKey + '&q=' + urllib.parse.quote(word) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)

        response = httpClient.getresponse()
        raw_data = response.read()
        # print(raw_data)
        data = json.loads(raw_data)
        # print(data)
    except Exception:
        print('error')
    finally:
        if httpClient:
            httpClient.close()
    return data
# translate('test')
