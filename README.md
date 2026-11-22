# 电商 UI 自动化测试框架

基于 **Selenium + pytest + Page Object + Allure** 的 Web UI 自动化测试框架，目标站点为公开电商演示站 [saucedemo](https://www.saucedemo.com/)。

框架覆盖登录、商品列表、商品详情、购物车、下单结算等核心业务流程，支持显式等待、失败自动截图、日志记录和 Allure 报告。

## 技术栈

- Python 3.10+
- Selenium 4.x
- pytest
- Allure
- python-dotenv

## 项目结构

```text
ecommerce-ui-automation/
├── common/
│   ├── pageObject.py       # 页面公共操作：等待、点击、输入、截图、下拉框
│   └── basecase.py         # 测试基类：驱动创建与关闭
├── pages/                  # Page Object 页面对象
│   ├── login.py            # 登录页
│   ├── inventory.py        # 商品列表页
│   ├── itemDetail.py       # 商品详情页
│   ├── cart.py             # 购物车页
│   └── checkout.py         # 结算页
├── testcase/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conf/                   # 站点地址、账号、等待时间、日志配置
├── utils/tools.py          # 通用工具（时间戳）
├── conftest.py             # 失败自动截图并附加到 Allure
├── pytest.ini
├── requirements.txt
└── .env.example
```

## 快速开始

### 1. 环境要求

- 已安装 Chrome 浏览器
- Python 3.10+
- Selenium 4.6+ 会自动通过 Selenium Manager 匹配 chromedriver，无需手动下载

### 2. 安装依赖

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. 配置

```bash
copy .env.example .env
```

默认使用 saucedemo 的 `standard_user / secret_sauce` 账号，一般不需要修改。

### 4. 运行用例

```bash
# 有界面模式（可以看到浏览器操作过程）
pytest

# 无头模式（适合 CI）
set HEADLESS=1
pytest

# 只跑冒烟用例
pytest -m smoke

# 只跑购物车模块
pytest -m cart
```

## 用例覆盖

| 模块 | 用例 | 校验点 |
|---|---|---|
| 登录 | 正确账号登录 | 跳转商品列表页，商品数量大于 0 |
| 登录 | 错误密码 | 提示用户名或密码不匹配 |
| 登录 | 锁定用户登录 | 提示用户已被锁定 |
| 商品列表 | 商品列表展示 | 商品数量为 6 |
| 商品列表 | 价格排序 | 选择价格从低到高后，价格列表升序 |
| 商品列表 | 进入商品详情 | 详情页商品名称与列表页一致，价格大于 0 |
| 购物车 | 加入购物车 | 角标数量为 1，购物车商品名称、数量正确 |
| 购物车 | 删除商品 | 删除后购物车商品数量为 0 |
| 结算 | 正常下单 | 填写收货信息、确认总价、提交订单，提示下单成功 |
| 结算 | 缺少必填项 | 不填 First Name，提示必填 |

共 10 条用例。

## 设计说明

- **Page Object 模式**：每个页面一个类，页面元素定位和业务操作封装在 `pages/`，用例只写业务步骤和断言。
- **公共操作封装**：`common/pageObject.py` 统一封装显式等待、点击、输入、文本获取、下拉框选择、截图等操作，避免 `sleep` 满天飞。
- **显式等待**：元素定位统一使用 `WebDriverWait`，并封装 `waitUrl` 等待页面跳转，降低用例不稳定。
- **失败截图**：`conftest.py` 在用例失败时自动截图，保存到 `screenshot/` 并附加到 Allure 报告。
- **配置外置**：站点地址、账号、超时时间、无头模式都通过 `.env` 配置，方便切换环境和 CI 运行。
- **日志记录**：页面操作和异常写入 `logs/ui_auto.log`，便于排查失败原因。

## 测试报告

```bash
pytest
allure serve allure-results
```

如果本机没有 Allure 命令行，可先安装：

```bash
# Windows 可用 scoop
scoop install allure
# 或下载 allure-commandline 后把 bin 目录加入 PATH
```

## 注意事项

- saucedemo 是公开演示站，请控制执行频率，不要并发压测。
- Selenium Manager 首次运行需要联网下载 chromedriver；如果网络受限，可手动下载对应版本 chromedriver，并在 `.env` 中通过 `CHROMEDRIVER=D:\tools\chromedriver.exe` 指定。
- 如果系统 PATH 中存在旧版 chromedriver，Selenium 可能会优先使用它导致版本不匹配，此时同样建议配置 `CHROMEDRIVER` 指向与 Chrome 版本一致的驱动。
- 用例之间使用独立的浏览器会话，互不影响，但会牺牲一些执行速度。

## 可写进简历的亮点

- 基于 Selenium + pytest + Page Object 搭建 UI 自动化框架，覆盖登录、商品、购物车、下单 4 个业务模块 10 条用例。
- 封装显式等待、页面跳转等待、截图、下拉框等公共操作，解决 UI 用例常见的元素定位不稳定问题。
- 通过 conftest 钩子实现用例失败自动截图并附加 Allure 报告，配合日志快速定位问题。
- 使用 .env 管理站点、账号、超时和无头模式配置，支持本地和有头/无头环境切换。

## License

MIT
