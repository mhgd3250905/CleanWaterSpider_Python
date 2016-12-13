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
    biliList=[]

    soup=BeautifulSoup(html,'html.parser')
    # print(soup)
    items=soup.find_all('li')
    print(len(items))
    for item in items:

        #获取标题
        title = item.find('div', 'news_txt_box2').text
        # print(title)
        # 获取内容链接
        contentUrl=item.find('a')['href']
        # print(contentUrl)
        #获取图片链接
        imgUrl=item.find('div','news_lst_thumb2').find('img')['src']
        # print(imgUrl)

        # 生成DataBean并加入到列表中
        weixinBean=Bean.DataBean(title, contentUrl, imgUrl)
        biliList.append(weixinBean)

    print("这一页的资源有 %d 条，现在开始爬虫！" % len(biliList))

    return biliList