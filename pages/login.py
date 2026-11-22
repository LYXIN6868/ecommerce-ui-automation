from selenium.webdriver.common.by import By

from common.pageObject import PageObject
from conf.config import BASEURL, PASSWORD, USERNAME


class Login(PageObject):
    # 登录页面地址
    LOGINPATH = BASEURL
    # 用户名输入框
    USERINPUT = (By.ID, 'user-name')
    # 密码输入框
    PASSWORDINPUT = (By.ID, 'password')
    # 登录按钮
    LOGINBTN = (By.ID, 'login-button')
    # 错误提示
    ERRORMSG = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    # 账号密码登录业务
    def accountLogin(self, username=USERNAME, password=PASSWORD):
        self.get(self.LOGINPATH)
        self.send_keys(self.USERINPUT, username)
        self.send_keys(self.PASSWORDINPUT, password)
        self.click(self.LOGINBTN)

    # 获取登录错误提示
    def checkErrorMsg(self):
        return self.getText(self.ERRORMSG)
