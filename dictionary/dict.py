#! /usr/bin/env python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import random
from colorama import init,Fore
import chardet
# chardet.__version__
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

init(autoreset=True)
root_url = 'http://www.iciba.com/'
while True:
    word = raw_input(u'请输入想要查询的单词(或"q"退出) : \n')
    if word == 'q':
        break
    else:
        url = root_url + urllib.quote(word)
        # 此请求头破解盗链
        start_html = requests.get(url)
        # start_html.encoding = 'utf-8'
        soup = BeautifulSoup(start_html.text, 'lxml')
        tag_soup = soup.find(class_='base-list switch_part')
        if tag_soup == None:
            print(Fore.GREEN + u'输入的单词不存在，重新输入.')
        else:
            meanings = tag_soup.find_all(class_='clearfix')
            for i in range(len(meanings)):
                translation = meanings[i].get_text()
                print(Fore.CYAN+translation.strip())
                print(Fore.RED+'=' * 30)
