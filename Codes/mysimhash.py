from simhash import Simhash
# f/4 is lenght in sexadecimal number system
print('%x'% Simhash('I am very happy',f=128).value)
print('%x'% Simhash('你好，世界　呼噜').value)
print('%x'% Simhash('你好，世界　呼噜 呼噜呼噜呼噜呼噜呼噜呼噜呼噜呼噜 呼噜').value)
