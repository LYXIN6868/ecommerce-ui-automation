import os

from dotenv import load_dotenv

load_dotenv()

# 目标站点：saucedemo 是公开的电商演示站，适合做 UI 自动化练习
BASEURL = os.getenv("BASEURL", "https://www.saucedemo.com/").rstrip('/') + '/'

USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
LOCKEDUSER = os.getenv("SAUCE_LOCKED_USER", "locked_out_user")

TIMEOUT = int(os.getenv("SELENIUM_TIMEOUT", "10"))
HEADLESS = os.getenv("HEADLESS", "0") == "1"
SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "screenshot")

# 可选：手动指定 chromedriver 路径；不填时由 Selenium Manager 自动匹配
CHROMEDRIVER = os.getenv("CHROMEDRIVER", "")
