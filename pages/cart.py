from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.pageObject import PageObject
from conf.config import TIMEOUT


class Cart(PageObject):
    # 购物车商品行
    CARTITEMS = (By.CLASS_NAME, 'cart_item')
    # 商品名称、价格、数量
    GOODSNAME = (By.CLASS_NAME, 'inventory_item_name')
    GOODSPRICE = (By.CLASS_NAME, 'inventory_item_price')
    QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    # 结算按钮、继续购物按钮
    CHECKOUTBTN = (By.ID, 'checkout')
    CONTINUEBTN = (By.ID, 'continue-shopping')

    def waitPage(self):
        self.waitUrl('cart.html')

    # 购物车商品种类数量
    def getGoodsCount(self):
        return len(self.find_elements(self.CARTITEMS))

    # 等待购物车商品数量变成指定值
    def waitGoodsCount(self, count):
        WebDriverWait(self.driver, TIMEOUT, poll_frequency=0.5).until(
            lambda driver: len(driver.find_elements(*self.CARTITEMS)) == count
        )

    # 购物车里的商品名称
    def getGoodsNames(self):
        self.wait_element(self.GOODSNAME)
        return [ele.text for ele in self.find_elements(self.GOODSNAME)]

    # 购物车里的商品价格
    def getGoodsPrices(self):
        self.wait_element(self.GOODSPRICE)
        return [float(ele.text.replace('$', '')) for ele in self.find_elements(self.GOODSPRICE)]

    # 商品数量
    def getQuantity(self):
        return self.getText(self.QUANTITY)

    # 删除指定商品，不传名称时删除第一个
    def removeGoods(self, goodsName=None):
        items = self.find_elements(self.CARTITEMS)
        if goodsName:
            target = [s for s in items if s.find_element(*self.GOODSNAME).text == goodsName][0]
        else:
            target = items[0]
        target.find_element(By.TAG_NAME, 'button').click()

    # 点击结算
    def checkout(self):
        self.click(self.CHECKOUTBTN)

    # 继续购物
    def continueShopping(self):
        self.click(self.CONTINUEBTN)
