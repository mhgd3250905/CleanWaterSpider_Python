# -*- coding: utf-8 -*-


from Bmob import BmobUtils
from ListHtmlSpider import HtmlGetUtils, PaopaoHtmlDealUtils,WeixinHtmlDealUtils
from ContentSpider import ContentHtmlSpider


#http://weixin.sogou.com/wapindex/wap/0612/wap_9/0.html




def WeixinSpider():
    '''
    微信资讯爬虫统筹地
    :return:
    '''
    #清空一下数据表
    BmobUtils.deleteBmobClass('WeixinBean')
    BmobUtils.deleteBmobClass('WeixinContentBean')

    headers={
        'Accept':'*/*',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'X-Requested-With':'XMLHttpRequest'
    }

    #开始爬
    for i in range(1,2):
        #&lastDate=2016/12/12 0:03:00
        url='http://weixin.sogou.com/wapindex/wap/0612/wap_9/%d.html' % i
        html= HtmlGetUtils.getHtml(url,headers=headers)
        # print(html)
        datalist= WeixinHtmlDealUtils.dealHtml(html)
        contentList=ContentHtmlSpider.getContentIndex(datalist)
        BmobUtils.insertListBmob('WeixinBean', datalist)
        BmobUtils.insertContentBmob('WeixinContentBean',contentList)
        print("经过不懈的努力，开哥爬下了第 %d 页" % i)