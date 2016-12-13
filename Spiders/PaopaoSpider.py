# -*- coding: utf-8 -*-
from Bmob import BmobUtils
from ListHtmlSpider import HtmlGetUtils, PaopaoHtmlDealUtils
from ContentSpider import ContentHtmlSpider


#http://m.pcpop.com/IndexHandler.ashx?page=1&size=20&tag=all&method=bottom

def PaopaoSpider():
    '''
    泡泡网资讯爬虫统筹地
    :return:
    '''
    #清空一下数据表
    BmobUtils.deleteBmobClass('PaopaoBean')
    BmobUtils.deleteBmobClass('PaopaoContentBean')

    #开始爬
    for i in range(1,11):
        #&lastDate=2016/12/12 0:03:00
        url='http://m.pcpop.com/handlers/IgeekHandler.ashx'
        params={
            'page': '1',
            'size': '20',
            'tag':'all',
            'method':'bottom'
        }
        params['page']="%d" % i
        print(params)
        html= HtmlGetUtils.getHtml(url,params)
        datalist= PaopaoHtmlDealUtils.dealHtml(html)
        contentList=ContentHtmlSpider.getContentIndex(datalist)
        BmobUtils.insertListBmob('PaopaoBean', datalist)
        BmobUtils.insertContentBmob('PaopaoContentBean',contentList)
        print("经过不懈的努力，开哥爬下了泡泡网第 %d 页" % i)