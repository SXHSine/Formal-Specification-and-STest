from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 初始化__init__()中定义驱动(driver)、基本的URL(base_url)和超时时间(timeout)等
# 定义open()方法用于打开URL网站，但它本身并未做这件事情，而是交由_open方法来实现。find_element()方法用于元素定位
class Page(object):
    '''
    基础类，用于页面对象类的继承
    '''

    login_url = 'http://'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
    
    def _open(self, url):
        new_url = self.base_url + url
        print ('end:'+new_url)
        self.driver.get(new_url)

    def open(self, url):
        self._open(url)
    
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
    
    def switch_frame(self, *loc):
        return self.driver.switch_to_frame(*loc)

# 对登录页面上的元素进行封装，使其成为更具体的操作方法
class LoginPage(Page):
    '''
    163邮箱登录页面模型
    '''

    # 定位器
    frame_loc = (By.ID, "x-URS-iframe")
    username_loc = (By.XPATH, "//input[contains(@class,'j-inputtext')]")
    password_loc = (By.XPATH, "//input[@class='j-inputtext dlpwd' and @name='password']")
    submit_loc = (By.ID, "dologin")

    # Action
    def frame(self):
        self.switch_frame(self.find_element(*self.frame_loc))

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()
# 将单个的元素操作组成一个完整的动作，包括：打开浏览器、输入用户名/密码、点击登录，该函数具有很强的可重用性
def test_user_login(driver, url, username, password):
    """
    测试获取的用户名/密码是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open(url)
    login_page.frame()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
# 接近于用户的操作行为。关心通过哪个浏览器打开邮箱网址、登录的用户名和密码是什么
def main():
    try:
        driver = webdriver.Chrome()
        url = 'mail.163.com'
        username = 'zhangwenqiang2008'
        password = '******'
        test_user_login(driver, url, username, password)
        sleep(10)
        # text = driver.find_element_by_xpath("//span[@id='spnUid']").text
        # assert(text == 'zhangwenqiang2008'), "用户名称不匹配，登录失败！"
    finally:
        # 关闭浏览器窗口
        driver.close()


if __name__ == '__main__':
    main()
