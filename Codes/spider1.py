import urllib.request as request

Cookie = "UM_distinctid=1670c4dfd7aa63-07b97a0c944134-1e3f6654-fa000-1670c4dfd7b1f8; YQT_COOKIE_USER={%22username%22:%22dfswxcb%22}; CNZZDATA1259942426=1505081665-1542095949-%7C1542150991; sentiment_session=8b5c6a6e3d41bdb5152a4b44b9a2522095878cfb; yq_access_token=eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJjbXNzIiwiaWQiOiJNWTllSGVpbyIsImlwIjoiNDkuODMuOTIuMjA1IiwiaWF0IjoxNTQyMTU1NjM5LCJhcHAiOiJZUSJ9.zkklsdOseFJMc2Wbhs_znQMuCdRQte4gtMJwMpaQ3Ao"

url = "https://yuqing.bigcloudsys.cn/apps/analysis/topics/getYqList"

headers = {
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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

req = request.Request(url,None,headers)
# print(req)
response = request.urlopen(req)
print(response)
the_page = response.read()
# print(the_page.decode("utf8"))

file = open("out.txt", "w")
file.write(the_page.decode("utf8"))
file.close()