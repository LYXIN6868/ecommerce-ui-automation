import pytest

from common.basecase import BaseCase
from pages.inventory import Inventory
from pages.itemDetail import ItemDetail
from pages.login import Login


class TestInventory(BaseCase):
    # 每个用例都从登录开始
    def login(self):
        Login(self.driver).accountLogin()
        return Inventory(self.driver)

    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_01_goodsList(self):
        inventoryPage = self.login()
        assert inventoryPage.getGoodsCount() == 6

    @pytest.mark.inventory
    def test_02_sortByPrice(self):
        inventoryPage = self.login()
        # 价格从低到高排序后，价格列表应为升序
        inventoryPage.sortBy('lohi')
        prices = inventoryPage.getGoodsPrices()
        assert prices == sorted(prices)

    @pytest.mark.inventory
    def test_03_enterGoodsDetail(self):
        inventoryPage = self.login()
        goodsName = inventoryPage.enterGoodsDetail(0)
        detailPage = ItemDetail(self.driver)
        detailPage.waitPage()
        assert goodsName == detailPage.checkGoodsName()
        assert detailPage.checkGoodsPrice() > 0
