from selenium import webdriver
import os

driver = webdriver.Firefox()

file_path = 'file://' + os.path.abspath('D:/code/python/FormalSpecificationAndSTest/C4/upfile.html')
driver.get(file_path)

driver.find_element_by_id("a").click()
os.system("upfile.exe")

driver.quit()