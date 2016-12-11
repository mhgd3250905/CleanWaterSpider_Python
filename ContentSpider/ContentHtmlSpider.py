# -*- coding: utf-8 -*-

from EveryBean import ContentBean
from ListHtmlSpider import HtmlGetUtils
from bs4 import BeautifulSoup

def getContentIndex(list):
    '''
    把处理好的contentBean加入到List中进行返回
    :param list:
    :return:
    '''
    contentBeanList=[]
    for item in list:
        contentUrl=item.getContentUrl()
        # print(contentUrl)
        contentHtml=getContent(contentUrl)
        # print(contentHtml)
        contentBean=ContentBean.ContentBean(contentUrl,contentHtml)
        contentBeanList.append(contentBean)

    return contentBeanList


def getContent(url):
    '''
    访问目的网页然后去广告之后返回过来
    :param url:
    :return: 处理之后的html文本
    '''
    content=HtmlGetUtils.getHtml(url)
    # print(content)
    soup = BeautifulSoup(content, 'html.parser')

    head=soup.find('head').prettify()
    # print(head)

    #网页不存在然后报错~
    print(url)
    print(soup.find('div', 'title3').prettify())
    divTitle=soup.find('div', 'title3').prettify()
    print(type(divTitle))

    divMain=soup.find('div', 'main').prettify()
    # print(divMain)
    divBottom=soup.find('div', 'tit').prettify()

    contentHtml='<!DOCTYPE HTML><html>'+\
                head+\
                '<body>'+\
                divTitle+\
                divMain+\
                divBottom+\
                '</body></html>'
    # print(contentHtml)
    return contentHtml