from selenium.webdriver.common.by import By

from common.pageObject import PageObject


class ItemDetail(PageObject):
    # 商品名称
    GOODSNAME = (By.CLASS_NAME, 'inventory_details_name')
    # 商品价格
    GOODSPRICE = (By.CLASS_NAME, 'inventory_details_price')
    # 加入购物车按钮
    ADDCARTBTN = (By.CSS_SELECTOR, 'button[data-test="add-to-cart"]')
    # 返回商品列表按钮
    BACKBTN = (By.ID, 'back-to-products')

    def waitPage(self):
        self.waitUrl('inventory-item.html')

    # 校验商品详情页名称
    def checkGoodsName(self):
        return self.getText(self.GOODSNAME)

    # 校验商品详情页价格
    def checkGoodsPrice(self):
        return float(self.getText(self.GOODSPRICE).replace('$', ''))

    # 加入购物车
    def addGoodsCart(self):
        self.click(self.ADDCARTBTN)

    # 返回商品列表
    def backToInventory(self):
        self.click(self.BACKBTN)
