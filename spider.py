import requests
from bs4 import BeautifulSoup
import json

def get_html(url):#获取网页源码
    html = requests.get(url)
    html.encoding = 'gb2312'
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

def get_text(url):#获取章节标题和内容
    result={ }
    soup=get_html(url)
    book_list_soup=soup.find('div',attrs={'class':'box_con' })
    book_list=[]
    for book_li in book_list_soup:
        title = book_list_soup.find('div', attrs={'class': 'bookname'}).find('h1').getText()#章节标题
        text = book_list_soup.find('div', attrs={'id': 'content'}).getText()#章节内容
        book_list.append(title+'\n'+text)#标题后换行再接内容
    print(book_list[0])

def get_next_url(url):
    soup=get_html(url)
    next_url=soup.find('div',attrs={'class':'bottem1'}).find_all('a')#这里可以获取到3个url，我们需要下一章节的url，所以可以新建一个列表提取第三个url
    url_list=[]
    for next_url_ in next_url:
        url_list.append(next_url_)
    next_url=url_list[3].get('href')
    print(next_url)

#get_text(url)
#get_next_url(url)
url='http://www.biquge5200.com/37_37683/14583622.html'#第一章节网站
text_total=[]
for i in range (1,21):
    text=get_text(url)
    next_url=get_next_url(url)
    url=next_url
    print(url)