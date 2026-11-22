# 页面公共操作封装，所有 Page 类继承这个类
import os
import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from conf.config import SCREENSHOT_DIR, TIMEOUT
from conf.logConf import logger
from utils.tools import Tools

tools = Tools()


class PageObject:
    def __init__(self, driver):
        self.driver = driver

    # 页面获取
    def get(self, url):
        self.driver.get(url)

    # 元素获取封装
    def find_element(self, tuple1):
        return self.driver.find_element(*tuple1)

    def find_elements(self, tuple1):
        return self.driver.find_elements(*tuple1)

    # 等待元素可见
    def wait_element(self, tuple1, timeout=None):
        if timeout is None:
            timeout = TIMEOUT
        return WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
            expected_conditions.visibility_of_element_located(tuple1)
        )

    # 等待页面地址包含指定内容
    def waitUrl(self, url, timeout=None):
        if timeout is None:
            timeout = TIMEOUT
        return WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
            expected_conditions.url_contains(url)
        )

    # 判断元素是否存在（不等待）
    def isElementExist(self, tuple1):
        return len(self.driver.find_elements(*tuple1)) > 0

    # 点击行为
    def click(self, tuple1):
        try:
            ele = self.wait_element(tuple1)
        except Exception as result:
            logger.error(f"{tuple1} 元素定位失败：{result}")
            self.getScreenShot('click_error')
            raise
        else:
            ele.click()

    # 随机点击一个元素，返回点击元素的文本
    def randomClickEle(self, tuple1, limit=None):
        if limit is not None:
            elements = self.driver.find_elements(*tuple1)[0:limit + 1:1]
        else:
            elements = self.driver.find_elements(*tuple1)
        if not elements:
            raise Exception(f"{tuple1} 没有可点击的元素")
        ele = random.choice(elements)
        text = ele.text
        ele.click()
        return text

    # 下拉框按 value 选择
    def selectByValue(self, tuple1, value):
        Select(self.wait_element(tuple1)).select_by_value(value)

    # 写入值
    def send_keys(self, tuple1, value, isclear=True):
        ele = self.wait_element(tuple1)
        if isclear:
            ele.clear()
        ele.send_keys(value)

    # 获取元素文本
    def getText(self, tuple1):
        return self.wait_element(tuple1).text

    # 页面截图
    def getScreenShot(self, name=''):
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        filename = f"{SCREENSHOT_DIR}/{tools.gettime()}_{name}.png"
        self.driver.get_screenshot_as_file(filename)
        logger.info(f"截图已保存：{filename}")
        return filename

    # 浏览器回退操作
    def back(self):
        self.driver.back()

    # 浏览器刷新操作
    def refresh(self):
        self.driver.refresh()

    # 获取当前浏览器页面地址
    def getCurrentURL(self):
        return self.driver.current_url

    # 获取当前浏览器页面标题
    def getTitle(self):
        return self.driver.title
