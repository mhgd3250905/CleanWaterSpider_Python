# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from EveryBean import Bean
# 返回DataBeanList
def dealHtml(html):
    '''
    处理html
    :param html:
    :return:返回Bilibili List
    '''
    itList=[]

    soup=BeautifulSoup(html,'html.parser')
    # print(soup)
    items=soup.find_all('li')

    for item in items:

        #获取标题
        title =item.find('div','block').text
        print(title)
        # 获取内容链接
        firstUrl=item.find('a','list_thumbnail')['href']
        urlLen=len(firstUrl)
        #http://wap.ithome.com/html/280459.htm
        urlId = firstUrl[(urlLen-10):(urlLen-4)]
        contentUrl="http://wap.ithome.com/html/%s.htm" % urlId
        print(contentUrl)
        #获取图片链接
        imgUrl=item.find('img')['src']
        print(imgUrl)

        # 生成DataBean并加入到列表中
        weixinBean=Bean.DataBean(title, contentUrl, imgUrl)
        itList.append(weixinBean)
        print('==================================================================')


    return itList