# -*- coding: utf-8 -*-
from Spiders import PaopaoSpider, BiliSpider
from ContentSpider import ContentHtmlSpider

url = 'http://www.bilibili.com/mobile/list/default-95-3-2016-12-03~2016-12-10.html'
#主入口
if __name__=='__main__':
    #爬取哔哩哔哩的科技栏位推荐内容
    # BiliSpider.biliSpider()
    #爬取泡泡网手机端新闻
    PaopaoSpider.PaopaoSpider()
