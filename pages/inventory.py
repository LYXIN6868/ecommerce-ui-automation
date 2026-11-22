import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.pageObject import PageObject
from conf.config import TIMEOUT


class Inventory(PageObject):
    # 首页（商品列表页）
    GOODSLIST = (By.CLASS_NAME, 'inventory_item')
    GOODSNAME = (By.CLASS_NAME, 'inventory_item_name')
    GOODSPRICE = (By.CLASS_NAME, 'inventory_item_price')
    # 排序下拉框
    SORTBOX = (By.CSS_SELECTOR, 'select[data-test="product-sort-container"]')
    # 购物车入口和角标
    CARTBTN = (By.CLASS_NAME, 'shopping_cart_link')
    CARTBADGE = (By.CLASS_NAME, 'shopping_cart_badge')

    # 登录成功后页面会跳到 inventory.html
    def checkLogin(self):
        self.waitUrl('inventory.html')
        return self.getCurrentURL()

    # 商品数量
    def getGoodsCount(self):
        self.wait_element(self.GOODSNAME)
        return len(self.find_elements(self.GOODSLIST))

    # 商品名称列表
    def getGoodsNames(self):
        self.wait_element(self.GOODSNAME)
        return [ele.text for ele in self.find_elements(self.GOODSNAME)]

    # 商品价格列表
    def getGoodsPrices(self):
        self.wait_element(self.GOODSPRICE)
        return [float(ele.text.replace('$', '')) for ele in self.find_elements(self.GOODSPRICE)]

    # 商品排序：az / za / lohi / hilo
    def sortBy(self, value):
        self.selectByValue(self.SORTBOX, value)
        sleep(0.5)

    # 选择指定下标的商品加入购物车，返回商品名称
    def chooseGoods(self, index=0):
        self.wait_element(self.GOODSNAME)
        items = self.find_elements(self.GOODSLIST)
        item = items[index]
        goodsName = item.find_element(*self.GOODSNAME).text
        item.find_element(By.TAG_NAME, 'button').click()
        return goodsName

    # 随机选择一个商品加入购物车
    def randomChooseGoods(self):
        self.wait_element(self.GOODSNAME)
        item = random.choice(self.find_elements(self.GOODSLIST))
        goodsName = item.find_element(*self.GOODSNAME).text
        item.find_element(By.TAG_NAME, 'button').click()
        return goodsName

    # 进入指定商品的详情页，返回商品名称
    def enterGoodsDetail(self, index=0):
        self.wait_element(self.GOODSNAME)
        items = self.find_elements(self.GOODSLIST)
        item = items[index]
        goodsName = item.find_element(*self.GOODSNAME).text
        item.find_element(*self.GOODSNAME).click()
        return goodsName

    def _cartCount(self, driver=None):
        driver = driver or self.driver
        elements = driver.find_elements(*self.CARTBADGE)
        return int(elements[0].text) if elements else 0

    # 购物车角标数量
    def getCartCount(self):
        return self._cartCount()

    # 等待购物车角标变成指定数量
    def waitCartCount(self, count):
        WebDriverWait(self.driver, TIMEOUT, poll_frequency=0.5).until(
            lambda driver: self._cartCount(driver) == count
        )

    # 进入购物车页面
    def enterCart(self):
        self.click(self.CARTBTN)
