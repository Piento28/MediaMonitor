import requests
from bs4 import BeautifulSoup

url_original = 'https://yuqing.bigcloudsys.cn/apps/nganalysis/main/news'
url_adjusted = 'https://yuqing.bigcloudsys.cn/apps/analysis/topics/getYqList'

Cookie = "UM_distinctid=167111cebca3a5-0569c3c4a65b19-35607401-fa000-167111cebcca3d; CNZZDATA1259942426=579134594-1542177337-%7C1542177337; sentiment_session=21f9483b93e56e43e358821d53f8e1d98fa85bc3; yq_access_token=eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJjbXNzIiwiaWQiOiJNWTllSGVpbyIsImlwIjoiNDkuODMuNjIuNTMiLCJpYXQiOjE1NDIxODAzNjMsImFwcCI6IllRIn0.Cfex0_DILWxX0O76u80cXtHaqcgJPc8y-Vv8T61opw4"

# eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJjbXNzIiwiaWQiOiJNWTllSGVpbyIsImlwIjoiNDkuODMuNjIuNTMiLCJpYXQiOjE1NDIxODAzNjMsImFwcCI6IllRIn0.Cfex0_DILWxX0O76u80cXtHaqcgJPc8y-Vv8T61opw4
# 21f9483b93e56e43e358821d53f8e1d98fa85bc3
# 1579134594-1542177337-%7C1542177337
# 167111cebca3a5-0569c3c4a65b19-35607401-fa000-167111cebcca3d

# my_params = 'params%5Bid%5D=844&params%5Btype%5D=1&params%5Battribute%5D=1&params%5Bdates%5D=1&params%5Bindustry%5D=&params%5Bis_read%5D=0&params%5Bsort_type%5D=1&params%5Babstract_type%5D=0&params%5Bmerge%5D=1&params%5Bcomment%5D=0&params%5Bpage_count%5D=15&params%5Bpage_index%5D=2'

my_params = {
    'params[id]': '844',
    'params[type]': '1',
    'params[attribute]': '1',
    'params[dates]': '1',
    'params[industry]': '',
    'params[is_read]': '0',
    'params[sort_type]': '1',
    'params[abstract_type]': '0',
    'params[merge]': '1',
    'params[comment]': '0',
    'params[page_count]': '15',
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
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}

r = requests.post(url_adjusted,headers=my_header,data=my_params)
# print(r.content)
# print(r.cookies)
# print(r.headers)
soup = BeautifulSoup(r.text,features="html5lib")
print(soup.decode("utf8"))