from aip import AipNlp

APP_ID = '14812878'
API_KEY = 'HxGQXVmxbwHU6YtE3uKAqWCN'
SECRET_KEY = 'ujqAHGoIMXCXkzmrLED2KRw83qAsnYCC '

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
text = "苹果公司不是一家伟大的公司"
# text="会根据招标"
print(client.sentimentClassify(text))
print('\n')
print(client.lexer(text))
