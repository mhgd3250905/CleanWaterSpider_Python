# -*- coding: utf-8 -*-
import HtmlGetUtils
import BiliHtmlDealUtils
import BmobUtils
# 引入time模块
import time
import datetime

def biliSpider():
    '''
    对哔哩哔哩进行爬虫程序，这里大概是一个统筹地
    :return:
    '''

    #获取url中需要的日期参数
    date1=time.strftime("%Y-%m-%d", time.localtime())
    date2=(datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")

    #首先删除表
    BmobUtils.deleteBmobClass("BiliBean")

   #爬虫正式开始
    for i in range(1,11):
        url='http://www.bilibili.com/mobile/list/default-95-%d-%s~%s.html' % (i,date2,date1)
        print(url)
        html=HtmlGetUtils.getBiliHtml(url).text
        datalist=BiliHtmlDealUtils.dealHtml(html)
        BmobUtils.insertBmob('BiliBean',datalist)
        print("经过不懈的努力，开哥爬下了第 %d 页" % i)