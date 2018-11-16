from selenium import webdriver
import time

chromedriver = "/Users/piento28/Downloads/chromedriver"
cookies = []
driver = webdriver.Chrome(chromedriver)
time.sleep(1)
driver.get("https://yuqing.bigcloudsys.cn/apps/nganalysis/home")
# print(driver.title)
# username
elem_user = driver.find_element_by_xpath('//input[@id="username"]')
elem_user.send_keys('dfswxcb')
elem_pwd = driver.find_element_by_xpath('//input[@id="password"]')
elem_pwd.send_keys('df111111')

commit = driver.find_element_by_xpath('//button[@type="submit"]')
commit.click()
time.sleep(1)

# for elem in driver.get_cookies():
#     print(elem)
print(driver.get_cookies()[0])
# 
#
#
#
#
#   if "微博-随时随地发现新鲜事" in driver.title:
# 32         for elem in driver.get_cookies():
# 33             cookie[elem["name"]] = elem["value"]
# 34         if len(cookie) > 0:
# 35             logger.warning("Get Cookie Successful: %s" % account)
# 36             cookies.append(cookie)
# 37             continue
# 38     else:
# 39         logger.warning("Get Cookie Failed: %s!" % account)
# UM_distinctid=167111949da9fa-0c2ab56879cf0d-35607401-fa000-167111949db6bc; CNZZDATA1259942426=1426370649-1542175078-%7C1542175078; sentiment_session=bce1f9a94c6bcf3383e4ca6bbc56305009c5b39d; yq_access_token=eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJjbXNzIiwiaWQiOiJNWTllSGVpbyIsImlwIjoiMTMuMjMxLjEyMi4xMzUiLCJpYXQiOjE1NDIxODAxMzQsImFwcCI6IllRIn0.W2J6aRVGgwYIkYNHA3dhNq3PPzAdILvTTidgD6DjNq0
#
#
# bce1f9a94c6bcf3383e4ca6bbc56305009c5b39d
# 1426370649-1542175078-%7C1542175078
# 167111949da9fa-0c2ab56879cf0d-35607401-fa000-167111949db6bc