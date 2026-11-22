from selenium.webdriver.common.by import By

from common.pageObject import PageObject


class Checkout(PageObject):
    # 收货人信息
    FIRSTNAME = (By.ID, 'first-name')
    LASTNAME = (By.ID, 'last-name')
    POSTALCODE = (By.ID, 'postal-code')
    CONTINUEBTN = (By.ID, 'continue')
    # 订单确认
    TOTAL = (By.CLASS_NAME, 'summary_total_label')
    FINISHBTN = (By.ID, 'finish')
    # 下单完成
    COMPLETEMSG = (By.CLASS_NAME, 'complete-header')
    # 错误提示
    ERRORMSG = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def waitStepOne(self):
        self.waitUrl('checkout-step-one.html')

    def waitStepTwo(self):
        self.waitUrl('checkout-step-two.html')

    def waitComplete(self):
        self.waitUrl('checkout-complete.html')

    # 填写收货人信息并继续
    def fillInfo(self, firstName='Zhang', lastName='San', postalCode='100000'):
        self.send_keys(self.FIRSTNAME, firstName)
        self.send_keys(self.LASTNAME, lastName)
        self.send_keys(self.POSTALCODE, postalCode)
        self.click(self.CONTINUEBTN)

    # 获取订单总价
    def getTotal(self):
        return self.getText(self.TOTAL)

    # 提交订单
    def finishOrder(self):
        self.click(self.FINISHBTN)

    # 获取下单成功提示
    def getCompleteMsg(self):
        return self.getText(self.COMPLETEMSG)

    # 获取表单错误提示
    def checkErrorMsg(self):
        return self.getText(self.ERRORMSG)
