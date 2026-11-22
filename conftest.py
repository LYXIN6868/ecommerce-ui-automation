import allure
import pytest

from common.pageObject import PageObject


# 用例失败时自动截图，并附加到 Allure 报告
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = getattr(item.instance, 'driver', None)
        if driver:
            try:
                page = PageObject(driver)
                filename = page.getScreenShot('fail')
                allure.attach.file(filename, name='失败截图', attachment_type=allure.attachment_type.PNG)
            except Exception as result:
                print('失败截图保存失败：', result)
