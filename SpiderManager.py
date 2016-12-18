# -*- coding: utf-8 -*-
from Spiders import PaopaoSpider,WeixinSpider,ItHomeSpider,HXSpider,FHSpider,PWSpider,GGSpider
import threading
import requests
import time

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
def startSpider():
    '''
    开启爬虫
    :return: None
    '''
    WXThread = myThread(1,'微信科技公众号',WeixinSpider.WX())
    ITThread = myThread(2,'IT之家',ItHomeSpider.IT())
    PPThread = myThread(3,'泡泡网',PaopaoSpider.PP())
    HXThread = myThread(4,'虎嗅网',HXSpider.HX())
    FHThread = myThread(5,'凤凰科技',FHSpider.FH())
    PWThread = myThread(6,'品玩',PWSpider.PW())
    GGThread = myThread(7, '硅谷密探', GGSpider.GG())
    PPThread.start()  # 泡泡网
    WXThread.start()  # 微信科技
    ITThread.start()  # IT之家
    HXThread.start()  # 虎嗅网
    FHThread.start()  # 凤凰科技
    PWThread.start()  # 品玩网
    GGThread.start()  # 硅谷密探

    PPThread.join()
    WXThread.join()
    ITThread.join()
    HXThread.join()
    FHThread.join()
    PWThread.join()
    GGThread.join()

if __name__=='__main__':
    # 开启所有爬虫线程
    startSpider()
    print('''

                 ▍ ★∴
                　　．．．．▍▍．..．█▍ ☆ ★∵ ..../
                　　◥█▅▅██▅▅██▅▅▅▅▅███◤
                 　 ．◥███████████████◤
                ～～～～◥█████████████◤～～～～''')


















