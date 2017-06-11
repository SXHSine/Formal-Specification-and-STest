from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_video_simple")

# video = driver.find_element_by_xpath("body/Setion[1]/div/video")
# video = driver.find_element_by_id("preview-player")
video = driver.find_element_by_tag_name("video")

time = driver.execute_script("return arguments[0].duration;",video)
print(time)
url = driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

print("start")
driver.execute_script("return arguments[0].play()",video)
# driver.execute_script(js)

# sleep(15)


print("start")
driver.execute_script("return arguments[0].play()",video)

print("stop")
driver.execute_script("arguments[0].pause()",video)

driver.quit()