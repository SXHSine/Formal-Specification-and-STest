from selenium import webdriver
import os
#pip install selenium
#path配置
# driver = webdriver.Firefox(),版本有问题
#允许activeX控件，不然获取element动作会被阻止
driver = webdriver.Ie()
file_path = 'file://' + os.path.abspath('D:/code/python/FormalSpecificationAndSTest/C4/upfile.html')
driver.get(file_path)
driver.find_element_by_id("a").send_keys('upload_file.txt')
driver.quit()