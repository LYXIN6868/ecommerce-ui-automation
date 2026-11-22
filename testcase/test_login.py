import pytest

from common.basecase import BaseCase
from conf.config import LOCKEDUSER, PASSWORD, USERNAME
from pages.inventory import Inventory
from pages.login import Login


class TestLogin(BaseCase):
    @pytest.mark.login
    @pytest.mark.smoke
    def test_01_successLogin(self):
        loginPage = Login(self.driver)
        loginPage.accountLogin()
        inventoryPage = Inventory(self.driver)
        assert 'inventory.html' in inventoryPage.checkLogin()
        assert inventoryPage.getGoodsCount() > 0

    @pytest.mark.login
    def test_02_errorPassword(self):
        loginPage = Login(self.driver)
        loginPage.accountLogin(USERNAME, 'wrong_password')
        assert 'do not match' in loginPage.checkErrorMsg()

    @pytest.mark.login
    def test_03_lockedUser(self):
        loginPage = Login(self.driver)
        loginPage.accountLogin(LOCKEDUSER, PASSWORD)
        assert 'locked out' in loginPage.checkErrorMsg()
