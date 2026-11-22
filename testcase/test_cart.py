import pytest

from common.basecase import BaseCase
from pages.cart import Cart
from pages.inventory import Inventory
from pages.login import Login


class TestCart(BaseCase):
    def login(self):
        Login(self.driver).accountLogin()
        return Inventory(self.driver)

    @pytest.mark.cart
    @pytest.mark.smoke
    def test_01_addGoodsToCart(self):
        inventoryPage = self.login()
        goodsName = inventoryPage.chooseGoods(0)
        inventoryPage.waitCartCount(1)
        assert inventoryPage.getCartCount() == 1

        inventoryPage.enterCart()
        cartPage = Cart(self.driver)
        cartPage.waitPage()
        assert cartPage.getGoodsCount() == 1
        assert goodsName in cartPage.getGoodsNames()
        assert cartPage.getQuantity() == '1'

    @pytest.mark.cart
    def test_02_removeGoods(self):
        inventoryPage = self.login()
        goodsName = inventoryPage.chooseGoods(0)
        inventoryPage.waitCartCount(1)
        inventoryPage.enterCart()

        cartPage = Cart(self.driver)
        cartPage.waitPage()
        cartPage.removeGoods(goodsName)
        cartPage.waitGoodsCount(0)
        assert cartPage.getGoodsCount() == 0
