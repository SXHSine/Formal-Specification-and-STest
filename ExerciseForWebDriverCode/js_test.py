from selenium import webdriver
import os

driver = webdriver.Firefox()

file_path = 'file://' + os.path.abspath('D:/code/python/FormalSpecificationAndSTest/C4/upfile.html')
driver.get(file_path)

text = "here is input text"
js = "var sum=document.getElementById('input_text'); sum.value='" + text + "';"
driver.execute_script(js)

driver.quit()