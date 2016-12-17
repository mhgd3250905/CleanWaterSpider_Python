# -*- coding: utf-8 -*-
from Spiders import PaopaoSpider,WeixinSpider,ItHomeSpider,HXSpider,FHSpider,PWSpider
import threading
import requests

#主入口

class myThread(threading.Thread):

    def __init__(self, threadID, name,spiderClass):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.spiderClass=spiderClass

    def run(self):
        print("开始线程：" + self.name)
        self.spiderClass.startSpider()
        print("退出线程：" + self.name)

# 分别初始化各种爬虫的线程实例
WXThread = myThread(1,'微信科技公众号',WeixinSpider.WX())
ITThread = myThread(2,'IT之家',ItHomeSpider.IT())
PPThread = myThread(3,'泡泡网',PaopaoSpider.PP())
HXThread = myThread(4,'虎嗅网',HXSpider.HX())
FHThread = myThread(5,'凤凰科技',FHSpider.FH())
PWThread = myThread(6,'品玩',PWSpider.PW())

if __name__=='__main__':
    # 开启所有爬虫线程
    # PPThread.start()#泡泡网
    WXThread.start()#微信科技
    # ITThread.start()#IT之家
    # HXThread.start()#虎嗅网
    # FHThread.start()#凤凰科技
    # PWThread.start()#品玩网

    # PPThread.join()
    WXThread.join()
    # ITThread.join()
    # HXThread.join()
    # FHThread.join()
    # PWThread.join()

    print('''

                 ▍ ★∴
                　　．．．．▍▍．..．█▍ ☆ ★∵ ..../
                　　◥█▅▅██▅▅██▅▅▅▅▅███◤
                 　 ．◥███████████████◤
                ～～～～◥█████████████◤～～～～''')

    # headers={
    #     'X-Bmob-Application-Id':'9e16e39fa5374f446e5c928da0f83d62',
    #     'X-Bmob-REST-API-Key':'42db163cd4c45884279b914e1c2a4e75',
    #     'Content-Type':'application/json'
    # }
    # response=requests.get('https://api.bmob.cn/1/classes/HXContentBean/d55794c2f5',headers=headers).text
    # print(response)
















