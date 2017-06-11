from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://192.168.128.101:8080/SearchingSystem/Index3.html")
for cookie in driver.get_cookies():
    print("%s -> %s"%(cookie['name'],cookie['value'])) 

driver.add_cookie({'name':'success','value':'true'})
# driver.add_cookie({'name':'passwd1','value':'admin'})

for cookie in driver.get_cookies():
    print("%s -> %s"%(cookie['name'],cookie['value'])) 

driver.get("http://192.168.128.101:8080/SearchingSystem/Index3.html")

driver.quit()