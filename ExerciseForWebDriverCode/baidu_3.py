from selenium import webdriver
import logging#捕捉客户端向服务器发送的POST请求，但无法获取服务器所返回的应答信息。

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.set_window_size(600,600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click    #点击百度一下按钮


driver.quit()