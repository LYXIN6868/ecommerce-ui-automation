import pytest

from common.basecase import BaseCase
from pages.cart import Cart
from pages.checkout import Checkout
from pages.inventory import Inventory
from pages.login import Login


class TestCheckout(BaseCase):
    def login(self):
        Login(self.driver).accountLogin()
        return Inventory(self.driver)

    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_01_checkoutSuccess(self):
        # 登录 -> 加购 -> 购物车 -> 结算 -> 下单
        inventoryPage = self.login()
        inventoryPage.chooseGoods(0)
        inventoryPage.waitCartCount(1)
        inventoryPage.enterCart()

        cartPage = Cart(self.driver)
        cartPage.waitPage()
        cartPage.checkout()

        checkoutPage = Checkout(self.driver)
        checkoutPage.waitStepOne()
        checkoutPage.fillInfo()
        checkoutPage.waitStepTwo()
        assert checkoutPage.getTotal().startswith('Total: $')

        checkoutPage.finishOrder()
        checkoutPage.waitComplete()
        assert 'Thank you for your order' in checkoutPage.getCompleteMsg()

    @pytest.mark.checkout
    def test_02_checkoutMissingFirstName(self):
        inventoryPage = self.login()
        inventoryPage.chooseGoods(0)
        inventoryPage.waitCartCount(1)
        inventoryPage.enterCart()

        cartPage = Cart(self.driver)
        cartPage.waitPage()
        cartPage.checkout()

        checkoutPage = Checkout(self.driver)
        checkoutPage.waitStepOne()
        checkoutPage.fillInfo('', 'San', '100000')
        assert 'First Name is required' in checkoutPage.checkErrorMsg()
