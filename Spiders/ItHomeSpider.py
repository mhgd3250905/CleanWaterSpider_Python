# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from ContentSpider import ContentHtmlSpider
from HtmlUtils import HtmlGetUtils
from ListHtmlSpider import ItHomeHtmlDealUtils


#http://wap.ithome.com/ithome/getajaxdata.aspx?page=2&type=wapcategorypage
def itHomeSpider():
    '''
    针对IT之家的爬虫
    :return:
    '''
    #首先删除表
    BmobUtils.deleteBmobClass("ItBean")
    BmobUtils.deleteBmobClass("ItContentBean")

    # 爬虫正式开始
    for i in range(1, 2):
        url = 'http://www.ithome.com/ithome/getajaxdata.aspx?page=%d&type=indexpage' % (i)
        print(url)
        html = HtmlGetUtils.getHtml(url)
        # print(html)
        datalist = ItHomeHtmlDealUtils.dealHtml(html)
        contentList=ContentHtmlSpider.getContentIndex(datalist,'WX')
        BmobUtils.insertListBmob('ItBean', datalist)
        BmobUtils.insertContentBmob('ItContentBean',contentList)
        print("经过不懈的努力，开哥爬下了IT之家第 %d 页" % i)



