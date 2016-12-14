# -*- coding: utf-8 -*-
from Spiders import PaopaoSpider, BiliSpider,WeixinSpider,ItHomeSpider,HXSpider
from ContentSpider import ContentHtmlSpider
import threading

url = 'http://www.bilibili.com/mobile/list/default-95-3-2016-12-03~2016-12-10.html'
#主入口
class myThread(threading.Thread):
    def __init__(self, threadID, name, func):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func=func
    def run(self):
        print("开始线程：" + self.name)
        self.func()
        print("退出线程：" + self.name)

PpThread = myThread(1,'泡泡网',PaopaoSpider.PaopaoSpider())
WxThread = myThread(2,'微信公众号',WeixinSpider.WeixinSpider())
ITThread = myThread(3,'IT之家',ItHomeSpider.itHomeSpider())
HXThread = myThread(4,'虎嗅网',HXSpider.huXiuSpider())

if __name__=='__main__':
    #爬取哔哩哔哩的科技栏位推荐内容
    # BiliSpider.biliSpider()
    #爬取泡泡网手机端新闻
    # PaopaoSpider. PaopaoSpider()
    #爬区搜狗微信
    # WeixinSpider.WeixinSpider()
    # #爬取IT之家
    # ItHomeSpider.itHomeSpider()
    #爬取虎嗅网

    PpThread.start()
    WxThread.start()
    ITThread.start()
    HXThread.start()

    PpThread.join()
    WxThread.join()
    ITThread.join()
    HXThread.join()

















