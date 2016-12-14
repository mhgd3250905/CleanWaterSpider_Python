# -*- coding: utf-8 -*-

from Bmob import BmobUtils
from HtmlUtils import HtmlGetUtils,HtmlPostUtils
from ListHtmlSpider import HXHtmlDealUtils
from ContentSpider import ContentHtmlSpider


#http://wap.ithome.com/ithome/getajaxdata.aspx?page=2&type=wapcategorypage
def huXiuSpider():
    '''
    针对虎嗅网的爬虫
    :return:
    '''
    #首先删除表
    BmobUtils.deleteBmobClass("HXBean")

    # 爬虫正式开始
    for i in range(1, 2):
        #虎嗅网分为两个部分：
        #第一部分  当日新闻爬取
        #   主要是对URL：https://m.huxiu.com/  【get】的分析
        #第二部分  往期新闻爬取
        #   主要是对URl：https://m.huxiu.com/maction/article_list 【post {page：'i'}】的分析

        HXSecondListSpider(2)
        for i in range(1,11):
            if i==1:
                dataList=HXFirstListSpider()
            else:
                dataList=HXSecondListSpider(i)

                contentList = ContentHtmlSpider.getContentIndex(dataList, 'WX')
                BmobUtils.insertListBmob('HXBean', dataList)
                BmobUtils.insertContentBmob('HXContentBean', contentList)
                print("经过不懈的努力，开哥爬下了虎嗅网第 %d 页" % i)

        # for data in dataList:
        #     print(data.getTitle())




def HXFirstListSpider():
    '''
    虎嗅网第一部分爬虫
    :param url:
    :return: List<HXBean>
    '''
    url = 'https://m.huxiu.com/'
    print(url)
    html = HtmlGetUtils.getHtml(url)
    # print(html)
    datalist = HXHtmlDealUtils.dealFirstHtml(html)
    return datalist



def HXSecondListSpider(index):
    '''
    虎嗅网第二部分爬虫
    :param url:
    :return: List<HXBean>
    '''
    url='https://m.huxiu.com/maction/article_list'
    data={
        'page':index
    }
    html= HtmlPostUtils.postHtml(url,data)
    dataList=HXHtmlDealUtils.dealSecondHtml(html)
    return dataList



