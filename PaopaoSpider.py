# -*- coding: utf-8 -*-
import HtmlGetUtils
import PaopaoHtmlDealUtils
import BmobUtils
#http://m.pcpop.com/IndexHandler.ashx?page=1&size=20&tag=all&method=bottom

def PaopaoSpider():
    '''
    泡泡网资讯爬虫统筹地
    :return:
    '''
    #清空一下数据表
    BmobUtils.deleteBmobClass('PaopaoBean')

    #开始爬
    for i in range(1,11):
        url='http://m.pcpop.com/IndexHandler.ashx?page=%d&size=20&tag=all&method=bottom' % i
        html=HtmlGetUtils.getBiliHtml(url).text
        datalist=PaopaoHtmlDealUtils.dealHtml(html)
        BmobUtils.insertBmob('PaopaoBean',datalist)
        print("经过不懈的努力，开哥爬下了第 %d 页" % i)