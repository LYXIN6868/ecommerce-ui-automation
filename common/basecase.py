from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from conf.config import CHROMEDRIVER, HEADLESS


# 测试用例基类：负责驱动的创建和关闭
class BaseCase:
    def setup_method(self):
        options = Options()
        if HEADLESS:
            options.add_argument('--headless=new')
        options.add_argument('--window-size=1440,900')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        # 配置了 CHROMEDRIVER 就用手动指定的驱动，否则交给 Selenium Manager 自动匹配
        if CHROMEDRIVER:
            self.driver = webdriver.Chrome(service=Service(CHROMEDRIVER), options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        if not HEADLESS:
            self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown_method(self):
        sleep(1)
        self.driver.quit()
