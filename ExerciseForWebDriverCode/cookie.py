from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({'name':'sxh','value':'value_abc'})

for cookie in driver.get_cookies():
    print("%s -> %s"%(cookie['name'],cookie['value']))   #%s格式化一个对象为字符 
#例如开发人员开发一个功能，用户登录后，会将用户名写入浏览器cookie，
# 对应的key为username，我们可以通过get_cookies()打印value

# cookie = driver.get_cookies()#获取cookie信息
# print(cookie)#打印，以键值对的形式进行存储

driver.quit()