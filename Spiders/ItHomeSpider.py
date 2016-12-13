# -*- coding: utf-8 -*-
import datetime
import time

from Bmob import BmobUtils
from ListHtmlSpider import HtmlGetUtils, BiliHtmlDealUtils,ItHomeHtmlDealUtils

#http://wap.ithome.com/ithome/getajaxdata.aspx?page=2&type=wapcategorypage
def itHomeSpider():
    '''
    针对IT之家的爬虫
    :return:
    '''
    #首先删除表
    BmobUtils.deleteBmobClass("ItBean")

    # 爬虫正式开始
    for i in range(1, 2):
        url = 'http://www.ithome.com/ithome/getajaxdata.aspx?page=%d&type=indexpage' % (i)
        print(url)
        html = HtmlGetUtils.getHtml(url)
        # print(html)
        datalist = ItHomeHtmlDealUtils.dealHtml(html)
        # BmobUtils.insertListBmob('ItBean', datalist)
        print("经过不懈的努力，开哥爬下了IT之家第 %d 页" % i)



