from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.set_window_size(600,600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click    #点击百度一下按钮
sleep(2)

driver.get_screenshot_as_file("D:/code/python/FormalSpecificationAndSTest/C4/baidu_img.png")
sleep(3)

driver.quit()