from selenium import webdriver
from bs4 import BeautifulSoup
from aip import AipNlp
import numpy as np
import time
import requests
import json
import xlwt

url_login = 'https://yuqing.bigcloudsys.cn/apps/nganalysis/home'
url_news = 'https://yuqing.bigcloudsys.cn/apps/analysis/topics/getYqList'
chromedriver = "/Users/piento28/Desktop/MediaMonitor/chromedriver"
Cookie=""

number_all_news=0

def get_cookie():
    return_cookie=""
    driver = webdriver.Chrome(chromedriver)
    time.sleep(1)
    driver.get(url_login)

    elem_user = driver.find_element_by_xpath('//input[@id="username"]')
    elem_user.send_keys('dfswxcb')
    elem_pwd = driver.find_element_by_xpath('//input[@id="password"]')
    elem_pwd.send_keys('df111111')

    commit = driver.find_element_by_xpath('//button[@type="submit"]')
    commit.click()
    time.sleep(1)

    for elem in driver.get_cookies():
        return_cookie=return_cookie+elem['name']+"="+elem['value']+";"
    # print(return_cookie)
    return(return_cookie)

def get_all_news(time_days,Cookie):
    my_params = {
        'params[id]': '844',
        'params[type]': '1',
        # 'params[attribute]': '-1', #-1=negative news;1=positive news;0=neutral news;
        'params[dates]': str(time_days),
        'params[industry]': '',
        'params[is_read]': '0',
        'params[sort_type]': '1',
        'params[abstract_type]': '0',
        'params[merge]': '1',
        'params[comment]': '0',
        'params[page_count]': '1000',
        'params[page_index]': '1'
    }
    
    my_header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ja;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '270',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': Cookie,
        'Host': 'yuqing.bigcloudsys.cn',
        'Origin': 'https://yuqing.bigcloudsys.cn',
        'Referer': 'https://yuqing.bigcloudsys.cn/apps/nganalysis/main/news',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/70.0.3538.102 Safari/537.36',
    }
    r = requests.post(url_news,headers=my_header,data=my_params)
    soup = BeautifulSoup(r.text,features="html5lib")
    # 先检查text是什么类型
    # 如果type(text) is bytes，那么text.decode('unicode_escape')
    # 如果type(text) is str，那么text.encode('latin-1').decode('unicode_escape')
    # 在Python 2中才会出现unicode type，直接text.decode('unicode_escape')
    return(soup)

def handle_json_data(json_data,number_all_news):
    f_web_content=list()
    f_tmp_dict=dict()
    number_all_news=0
    for elm in json_data['data']['dataList']:
        f_tmp_dict=dict()
        f_tmp_dict['stamp']=number_all_news
        number_all_news+=1
        f_tmp_dict['id']=int(elm['id'])
        f_tmp_dict['url']=elm['url']
        f_tmp_dict['pubtime']=elm['pubtime']
        f_tmp_dict['title']=("".join(elm['title'].split())).replace('</em>', '')
        f_tmp_dict['abstract']=("".join(elm['abstract'].split())).replace('</em>', '')
        f_tmp_dict['source']=elm['source']
        
        f_tmp_dict['attribute']=int(elm['attribute'])
        f_web_content.append(f_tmp_dict)
    return(f_web_content,number_all_news)

def baidu_execl(web_content):
    APP_ID = '14812878'
    API_KEY = 'HxGQXVmxbwHU6YtE3uKAqWCN'
    SECRET_KEY = 'ujqAHGoIMXCXkzmrLED2KRw83qAsnYCC'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)#creat execl file
    sheet = book.add_sheet('Media Monitor', cell_overwrite_ok=True) #creat a sheet in the file named "Media Monitor"
    
    sheet.write(0, 0, '舆情标题')
    sheet.write(0, 1, '原文地址')
    sheet.write(0, 2, '来源媒体')
    sheet.write(0, 3, '舆情通的分类')
    sheet.write(0, 4, '情绪分类')
    sheet.write(0, 5, '情绪得分（百分制，满分完全正面）')
    sheet.write(0, 6, '预测的置信度（百分制，满分完全自信）')
    
    for elm in web_content:
        text = elm['title']+'。'+elm['abstract']
        baidu_result=client.sentimentClassify(text)
        # print(baidu_result)
        sheet.write(elm['stamp']+1, 0, elm['title'])
        sheet.write(elm['stamp']+1, 1, elm['url'])
        sheet.write(elm['stamp']+1, 2, elm['source'])
        
        if elm['attribute']==-1:
            sheet.write(elm['stamp']+1, 3, '负面')
        elif elm['attribute']==0:
            sheet.write(elm['stamp']+1, 3, '中立')
        elif elm['attribute']==1:
            sheet.write(elm['stamp']+1, 3, '正面')
            
            
        if baidu_result['items'][0]['sentiment']==0:
            sheet.write(elm['stamp']+1, 4, '负面')
        elif baidu_result['items'][0]['sentiment']==1:
            sheet.write(elm['stamp']+1, 4, '中立')
        elif baidu_result['items'][0]['sentiment']==2:
            sheet.write(elm['stamp']+1, 4, '正面')
        sheet.write(elm['stamp']+1, 5, baidu_result['items'][0]['positive_prob']*100)
        sheet.write(elm['stamp']+1, 6, baidu_result['items'][0]['confidence']*100)
        print("%d Done!\n"%(elm['stamp']+1))
        time.sleep(0.25)
    book.save('data/testexcel.xls')
    
Cookie = get_cookie()

web_content_soup = get_all_news(1,Cookie)
json_data = json.loads(web_content_soup.text)

number_all_news = 0
web_content,number_all_news = handle_json_data(json_data,number_all_news)
# print(number_all_news)

baidu_execl(web_content)
# print(web_content)
# f = open("data/test.txt",'w')
# for elm in web_content:
#     f.write(elm['title']+"\n")
# f.close
