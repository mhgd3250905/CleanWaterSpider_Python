# -*- coding: utf-8 -*-
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
}

#获取目标Html
def getBiliHtml(url):
    return requests.get(url,headers=headers)






